from RVObject import *

import xml.etree.ElementTree as xmltree


class array(RVObject):
    def __init__(self,xmlelement=None):
        self.rvXMLIvarName = ''

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')
