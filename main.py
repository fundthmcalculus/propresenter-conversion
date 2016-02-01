# main.py
# Scott M. Phillips
# 31 December 2015
import sys
import xml.etree.ElementTree
import glob
import os
from RVPresentationDocument import RVPresentationDocument


def getarg(argkey):
    argkey = argkey.lower()
    # Search for an argument which starts with a "-", and then find the following argument.
    for iarg,carg in enumerate(sys.argv):
        carg = carg.lower()
        if carg[1:] == argkey.lower() and carg.startswith("-"):
            # Check for a value following this one.
            if iarg == len(argkey) or sys.argv[iarg+1].startswith("-"):
                return True
            else:
                return sys.argv[iarg+1]

    return None


def processfile(input_file,output_file):
    # Open the file as an XML document, since that is what it is.
    xmlroot = xml.etree.ElementTree.parse(input_file).getroot()
    # We know this is an element of type: "RVPresentationDocument"
    rvdoc = RVPresentationDocument(xmlroot)

    # Write back out.
    rvxml = rvdoc.serializexml()
    # Pretty-print
    indent(rvxml)
    rvxmltree = xml.etree.ElementTree.ElementTree(rvxml)
    rvxmltree.write(output_file)


def deserializexml(xmlelement, rvobject):
    # Take the current object and find all variables.
    for curvar in vars(rvobject).keys():
        # See if there is an attribute with this type.
        if curvar in xmlelement.keys():
            setattr(rvobject, curvar, xmlelement.attrib[curvar])

    return rvobject


def removetrailingseparator(folderpath):
    if folderpath.endswith("/") or folderpath.endswith("\\"):
        return folderpath[:-1]
    else:
        return folderpath


def indent(elem, level=0):
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
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def main():
    # Get the command-line arguments.
    inputdir = getarg('inputdir')
    outputdir = getarg('outputdir')

    inputfile = getarg('inputfile')
    outputfile = getarg('outputfile')

    if inputfile is not None:
        processfile(inputfile, outputfile)
        return

    # Remove any trailing path separators.
    inputdir = removetrailingseparator(inputdir)
    outputdir = removetrailingseparator(outputdir)

    # Loop through the input directory and process every file.
    for pro6file in glob.glob(inputdir + '/*.pro6'):
        # Take the input file and make the output file.
        filenamewext = os.path.basename(pro6file)
        filenametpl = os.path.splitext(filenamewext)
        # Process the file
        processfile(pro6file, outputdir + '/' + filenametpl[0] + '_out' + filenametpl[1])


if __name__ == "__main__":
    main()