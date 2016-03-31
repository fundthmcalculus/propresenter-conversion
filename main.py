# main.py
# Scott M. Phillips
# 31 December 2015
import sys
from directoryconversiongui import directoryconversiongui
from propresenterconverter import propresenterconverter


if __name__ == "__main__":
    # Check for command-line arguments.
    if len(sys.argv) > 1:
        propresenterconverter().convert()
    else:
        dcg = directoryconversiongui()
        dcg.show()
