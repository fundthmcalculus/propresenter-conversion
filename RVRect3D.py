from RVObject import RVObject

import re


class RVRect3D(RVObject):
    def __init__(self, xmlelement=None):
        self.rvXMLIvarName = "position"

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

        # Pull out inside text.
        inner_text = re.split('\{*\}', xmlelement[0])
        toks = inner_text.split()

        self.x = float(toks[0])
        self.y = float(toks[1])
        self.width = float(toks[2])
        self.height = float(toks[3])


