from RVObject import RVObject

import xml.etree.ElementTree as xmltree


class shadow(RVObject):
    def __init__(self, xmlelement=None):
        self.rvXMLIvarName = "shadow"
        self.shadowtext = "0.000000|0 0 0 0.3333333432674408|{4, -4}"

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')
        self.shadowtext = xmlelement.text

    def serializexml(self):
        xmlelement = xmltree.Element('shadow')
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)
        xmlelement.text = self.shadowtext

        return xmlelement