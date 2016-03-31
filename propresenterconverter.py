import sys
import xml
import glob
import os
import multiprocessing
from itertools import repeat

from RVPresentationDocument import RVPresentationDocument
from RVObject import RVObject
from NSColor import NSColor
import rtf


class propresenterconverter:
    def __init__(self, arglist=sys.argv):
        self.arglist = arglist

    def getarg(self, argkey):
        argkey = argkey.lower()
        # Search for an argument which starts with a "-", and then find the following argument.
        for iarg, carg in enumerate(self.arglist):
            carg = carg.lower()
            if carg[1:] == argkey.lower() and carg.startswith("-"):
                # Check for a value following this one.
                if iarg == len(argkey):
                    return True
                else:
                    return self.arglist[iarg+1]

        return None

    def processfile(self, input_file, output_file):
        # Print which file is being processed.
        print("Converting {0}...".format(input_file))
        # Open the file as an XML document, since that is what it is.
        xmlelemtree = xml.etree.ElementTree.parse(input_file)
        xmlroot = xmlelemtree.getroot()

        # self.writexml(xmlroot, output_file=input_file.replace(".pro6", "_in.pro6"))

        # We know this is an element of type: "RVPresentationDocument"
        rvdoc = RVPresentationDocument(xmlroot)

        # Convert all slides to triple-wide.
        self.converttotriplewide(rvdoc)

        # Write back out.
        rvxml = rvdoc.serializexml()
        self.writexml(rvxml, output_file)

    def converttotriplewide(self, rvdoc):
        # Adjust the width.
        old_width = rvdoc.width
        # Convert to new width.
        rvdoc.width *= 3

        # Get every slide.
        allslides = [cslide for cgroup in rvdoc.groups for cslide in cgroup.slides]

        # Loop through each one
        for idx, cslide in enumerate(allslides):
            try:

                # Adjust its current content to the middle.
                cslide.displayElements[0].position.x += old_width

                # TODO - Get the previous and next slide data (if they exist).
                if idx > 0:
                    try:
                        previoustext = RVObject.copyobject(allslides[idx - 1].displayElements[0])
                        # Move it back.
                        previoustext.position.x -= old_width
                        # Grey it out.
                        self.greyouttext(previoustext)
                        cslide.displayElements.append(previoustext)
                    except Exception:
                        # Do nothing
                        pass

                if idx < len(allslides) - 1:
                    try:
                        nexttext = RVObject.copyobject(allslides[idx + 1].displayElements[0])
                        # Move it over.
                        nexttext.position.x += 2 * old_width
                        # Grey it out.
                        self.greyouttext(nexttext)
                        cslide.displayElements.append(nexttext)
                    except Exception:
                        # Do nothing
                        pass

            except Exception:
                # Do nothing
                pass

    def greyouttext(self, textelement):
        # Get the rtf string.
        rtfstring = textelement.RTFData.getdecoded()
        # Insert the new grey color.
        greylevel = 0.3
        rtfstring = rtf.addcolortotable(rtfstring, NSColor(R=greylevel, G=greylevel, B=greylevel))

        # Store back in encoded format.
        textelement.RTFData.setdecoded(rtfstring)

    def writexml(self, rvxml, output_file):
        # Pretty-print
        self.indent(rvxml)

        # Remove all invalid attributes.
        self.removeinvalidxml(rvxml)

        # Create the tree
        rvxmltree = xml.etree.ElementTree.ElementTree(rvxml)
        rvxmltree.write(output_file, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def removeinvalidxml(rvxml):
        # Check all attributes.
        for cattr in rvxml.keys():
            if rvxml.get(cattr) is None:
                rvxml.attrib.pop(cattr)

        for celem in rvxml.getchildren():
            propresenterconverter.removeinvalidxml(celem)

    @staticmethod
    def deserializexml(xmlelement, rvobject):
        # Take the current object and find all variables.
        for curvar in vars(rvobject).keys():
            # See if there is an attribute with this type.
            if curvar in xmlelement.keys():
                setattr(rvobject, curvar, xmlelement.attrib[curvar])

        return rvobject

    @staticmethod
    def removetrailingseparator(folderpath):
        if folderpath.endswith('/') or folderpath.endswith('\\'):
            return folderpath[:-1]
        else:
            return folderpath

    def indent(self, elem, level=0):
        """
        Source: https://norwied.wordpress.com/2013/08/27/307/
        :param elem: [xml.etree.Element]
        :param level: [int] depth into tree
        :return: Nothing
        """
        i = "\n" + level * "    "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def convertfile(self, pro6file, outputdir):
        # Take the input file and make the output file.
        filenamewext = os.path.basename(pro6file)
        filenametpl = os.path.splitext(filenamewext)
        # Process the file
        try:
            self.processfile(pro6file, outputdir + '/' + filenametpl[0] + filenametpl[1])
            return ["", None]
        except Exception as e:
            return [filenamewext, e]

    def convert(self):
        # Get the command-line arguments.
        inputdir = self.getarg('inputdir')
        outputdir = self.getarg('outputdir')

        inputfile = self.getarg('inputfile')
        outputfile = self.getarg('outputfile')

        if inputfile is not None:
            self.processfile(inputfile, outputfile)
            return

        # Remove any trailing path separators.
        inputdir = self.removetrailingseparator(inputdir)
        outputdir = self.removetrailingseparator(outputdir)

        # Loop through the input directory and process every file.
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        failedfiles = pool.starmap(self.convertfile, zip(glob.glob(inputdir + '/*.pro6'),repeat(outputdir)))

        # Remove all empty file names.
        failedfiles = [f for f in failedfiles if len(f[0]) > 0]

        if len(failedfiles) > 0:
            print("The following files produced errors during conversion:")
            for f in failedfiles:
                print(f[0], ": ", f[1])
