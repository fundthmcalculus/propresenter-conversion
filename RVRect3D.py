from RVObject import RVObject
from formatutilities import rvnumberformat

import xml.etree.ElementTree as xmltree


class RVRect3D(RVObject):
    def __init__(self, xmlelement=None):
        self.rvXMLIvarName = ""
        self.x = 0
        self.y = 0
        self.z = 0
        self.width = 0
        self.height = 0

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
        self.z = float(toks[2])
        self.width = float(toks[3])
        self.height = float(toks[4])

    def serializexml(self):
        xmlelement = xmltree.Element("RVRect3D")
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)
        xmlelement.text = str(self)

        return xmlelement

    def __repr__(self):

        return "{" + rvnumberformat(self.x) + " " + rvnumberformat(self.y) + " " + rvnumberformat(self.z) + " " + rvnumberformat(self.width) + " " + rvnumberformat(self.height) + "}"
