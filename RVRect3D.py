from RVObject import RVObject

import re
import xml.etree.ElementTree as xmltree


class RVRect3D(RVObject):
    def __init__(self, xmlelement=None):
        self.rvXMLIvarName = ""
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        self.extras = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

        # Pull out inside text.
        toks = xmlelement.text.replace("{", "").replace("}", "").split()

        self.x = float(toks[0])
        self.y = float(toks[1])
        self.width = float(toks[-2])
        self.height = float(toks[-1])

        self.extras = toks[2:-2]

    def serializexml(self):
        xmlelement = xmltree.Element("RVRect3D")
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)
        xmlelement.text = str(self)

        return xmlelement

    def __repr__(self):
        extras_str = " ".join(self.extras)
        if len(extras_str) > 0:
            extras_str = " " + extras_str

        return "{" + str(self.x) + " " + str(self.y) + extras_str + " " + str(self.width) + " " + str(self.height) + "}"
