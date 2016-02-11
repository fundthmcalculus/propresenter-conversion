from RVObject import *

import xml.etree.ElementTree as xmltree
import uuid
import util


class RVEffect(RVObject):
    def __init__(self,xmlelement=None):
        self.UUID = str(uuid.uuid4())
        self.displayName = ''

        self.effectVariables = list()

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.UUID = xmlelement.get('UUID')
        self.displayName = xmlelement.get('displayName')

        xml_array = xmlelement.find("./array[@rvXMLIvarName='effectVariables']")
        for cxml in xml_array:
            self.effectVariables.append(util.createobject(cxml))

    def serializexml(self):
        xmlelement =xmltree.Element('RVEffect')
        xmlelement.set('UUID', self.UUID)
        xmlelement.set('displayName', self.displayName)

        xml_array = self.createarray('effectVariables')
        for ceffect in self.effectVariables:
            xml_array.append(ceffect.serializexml())
        xmlelement.append(xml_array)

        return xmlelement