from RVObject import *

import xml.etree.ElementTree as xmltree
import base64


class NSString(RVObject):
    def __init__(self,xmlelement=None, datastring=""):
        # Create instance variables.
        self.data = datastring
        self.rvXMLIvarName = ""
        if xmlelement is not None:
            self.data = xmlelement.text
            self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

    def __repr__(self):
        return self.data

    def getdecoded(self):
        return base64.b64decode(self.data).decode("utf-8")

    def setdecoded(self, s):
        self.data = base64.b64encode(bytes(s, "utf-8")).decode("utf-8")

    def serializexml(self):
        xmlelement = xmltree.Element("NSString")
        xmlelement.text = str(self)
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)

        return xmlelement