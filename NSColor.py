from RVObject import *

import xml.etree.ElementTree as xmltree


class NSColor(RVObject):
    def __init__(self,RGBAstring=None, R=0, G=0, B=0, A=1):
        # Create instance variables.
        if RGBAstring is not None and len(RGBAstring) > 0:
            toks = RGBAstring.split(" ")
            R = float(toks[0])
            G = float(toks[1])
            B = float(toks[2])
            A = float(toks[3])

        self.R = R
        self.G = G
        self.B = B
        self.A = A

    def __repr__(self):
        return str(self.R) + " " + str(self.G) + " " + str(self.B) + " " + str(self.A)

    def serializexml(self):
        xmlelement = xmltree.Element("NSColor")
        xmlelement.text = str(self)

        return xmlelement