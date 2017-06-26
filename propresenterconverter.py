import sys
import xml
import glob
import os
import multiprocessing
import math
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
        for idx, cslide in reversed(list(enumerate(allslides))):
            try:

                # self.center_highlight_TW(allslides, cslide, idx, old_width)
                self.walking_highlight_TW(allslides, idx, old_width)

            except Exception:
                # Do nothing
                pass


    def walking_highlight_TW(self, allslides, idx, old_width):
        # Do the walking highlight.
        # Adjust the master text appropriately
        previoustext = None
        nexttext = None
        base_X = allslides[idx].displayElements[0].position.x

        if idx > 0:
            previoustext = RVObject.copyobject(allslides[idx - 1].displayElements[0])
        if idx < len(allslides) - 1:
            nexttext = RVObject.copyobject(allslides[idx + 1].displayElements[0])

        allslides[idx].displayElements[0].position.x += old_width * (idx % 3)
        if idx > 0:
            try:
                # Move it back - because of the modulo operator, -1 -> +2
                previoustext.position.x = base_X + old_width * ((idx+2) % 3)
                # Grey it out.
                self.greyouttext(previoustext)
                allslides[idx].displayElements.append(previoustext)
            except Exception:
                # Do nothing
                pass
        if idx < len(allslides) - 1:
            try:
                # Move it over.
                nexttext.position.x = base_X + old_width * ((idx + 1) % 3)
                # Grey it out.
                self.greyouttext(nexttext)
                allslides[idx].displayElements.append(nexttext)
            except Exception:
                # Do nothing
                pass


    def center_highlight_TW(self, allslides, cslide, idx, old_width):
        # Adjust its current content to the middle.
        cslide.displayElements[0].position.x += old_width
        # Get the previous and next slide data (if they exist).
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
        # Make sure the directory exists.
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        # Write the file.
        rvxmltree.write(output_file, encoding="utf-8", xml_declaration=False)
        # Prepend the header.
        f = open(output_file,'r')
        contents = f.readlines()
        f.close()
        fid = open(output_file, 'w')
        contents.insert(0,'<?xml version="1.0" encoding="utf-8" ?>\n')
        fid.writelines(contents)
        fid.close()

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
            self.processfile(pro6file, outputdir + '/' + filenametpl[0] +'_TW'+ filenametpl[1])
            return ["", None]
        except Exception as e:
            return [filenamewext, e]

    def processdirectory(self, inputdir, outputdir):

        # Remove any trailing path separators.
        inputdir = self.removetrailingseparator(inputdir)
        outputdir = self.removetrailingseparator(outputdir)

        # Loop through the input directory and process every file.
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        failedfiles = pool.starmap(self.convertfile, zip(glob.glob(inputdir + '/*.pro6'), repeat(outputdir)))

        # Remove all empty file names.
        failedfiles = [f for f in failedfiles if len(f[0]) > 0]

        if len(failedfiles) > 0:
            print("The following files produced errors during conversion:")
            for f in failedfiles:
                print(f[0], ": ", f[1])
