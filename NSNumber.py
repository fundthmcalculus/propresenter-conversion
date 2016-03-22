from RVObject import RVObject

import xml.etree.ElementTree as xmltree


class NSNumber(RVObject):
    def __init__(self, xmlelement=None):
        self.hint = "float"
        self.value = 0

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.hint = xmlelement.get('hint')
        self.value = xmlelement.text

    def serializexml(self):
        xmlelement = xmltree.Element('NSNumber')
        xmlelement.set('hint', self.hint)
        xmlelement.text = self.value

        return xmlelement


class RVEffectFloatVariable(RVObject):
    def __init__(self, xmlelement=None):
        self.type = 1
        self.name = ""
        self.min = -1
        self.max = 1
        self.defValue = 0
        self.value = 0

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.type = float(xmlelement.get('type'))
        self.name = xmlelement.get('name')
        self.min = float(xmlelement.get('min'))
        self.max = float(xmlelement.get('max'))
        self.defValue = float(xmlelement.get('defValue'))
        self.value = float(xmlelement.get('value'))

    def serializexml(self):
        xmlelement = xmltree.Element('RVEffectFloatVariable')
        xmlelement.set('type', "{:.0f}".format(self.type))
        xmlelement.set('name', self.name)
        xmlelement.set('min', "{:.6f}".format(self.min))
        xmlelement.set('max', "{:.6f}".format(self.max))
        xmlelement.set('defValue', "{:.6f}".format(self.defValue))
        xmlelement.set('value', "{:.6f}".format(self.value))

        return xmlelement