# main.py
# Scott M. Phillips
# 31 December 2015
import sys
import argparse
from directoryconversiongui import directoryconversiongui
from propresenterconverter import propresenterconverter


def parsecommandline():
    parser = argparse.ArgumentParser(
        description='Convert Propresenter6 files from single to triple-wide configurations.',
        prog='propresenter-conversion', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--inputfile', type=str, default=None, help='Input file to convert')
    parser.add_argument('--outputfile', type=str, default=None, help='Output file to write to')
    parser.add_argument('--inputdir', type=str, default=None, help='Input directory to use for conversion')
    parser.add_argument('--outputdir', type=str, default=None, help='Output directory to use for conversion')

    # Parse all the arguments.
    cmdargs = parser.parse_args()

    return cmdargs


if __name__ == "__main__":
    args = parsecommandline()
    p6conv = propresenterconverter()
    if args.inputfile is not None and args.outputfile is not None:
        p6conv.processfile(args.inputfile, args.outputfile)

    if args.inputdir is not None and args.outputdir is not None:
        p6conv.processdirectory(args.inputdir, args.outputdir)
