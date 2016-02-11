from RVObject import RVObject
from NSColor import NSColor
from RVScaleFactor import RVScaleFactor
from RVRect3D import RVRect3D
from shadow import shadow
import util

import xml.etree.ElementTree as xmltree
import uuid


class RVMediaElement(RVObject):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.UUID = uuid.uuid4()
        self.displayName = ""
        self.typeID = 0
        self.displayDelay = 0.000000
        self.locked = False
        self.persistent = False
        self.fromTemplate = False
        self.opacity = 1.000000
        self.source = ""
        self.bezelRadius = 0.000000
        self.rotation = 0.000000
        self.drawingFill = False
        self.drawingShadow = False
        self.drawingStroke = False

        self.position = None
        self.stroke = dict()
        self.shadow = None

    def deserializexml(self, xmlelement):
        # Deserialize from XML
        self.UUID = xmlelement.get("UUID")
        self.displayName = xmlelement.get('displayName')
        self.typeID = int(xmlelement.get('typeID'))
        self.displayDelay = float(xmlelement.get('displayDelay'))
        self.locked = bool(xmlelement.get('locked'))
        self.persistent = bool(xmlelement.get('persistent'))
        self.fromTemplate = bool(xmlelement.get('fromTemplate'))
        self.opacity = float(xmlelement.get('opacity'))
        self.source = xmlelement.get('source')
        self.bezelRadius = float(xmlelement.get('bezelRadius'))
        self.rotation = float(xmlelement.get('rotation'))
        self.drawingFill = bool(xmlelement.get('drawingFill'))
        self.drawingShadow = bool(xmlelement.get('drawingShadow'))
        self.drawingStroke = bool(xmlelement.get('drawingStroke'))

        xml_pos = xmlelement.find("./RVRect3D[@rvXMLIvarName='position']")
        self.position = RVRect3D(xml_pos)

        xml_shadow = xmlelement.find("./shadow")
        self.shadow = shadow(xml_shadow)

        xml_stroke = xmlelement.find("./dictionary[@rvXMLIvarName='stroke']")
        for cnode in xml_stroke:
            xml_key = cnode.get('rvXMLDictionaryKey')
            # Create the current object.
            self.stroke[xml_key] = util.createobject(cnode)

    def serializexmlmedia(self,xmlelement):
        xmlelement.set("UUID", self.UUID)
        xmlelement.set('displayName', self.displayName)
        xmlelement.set('typeID', str(self.typeID))
        xmlelement.set('displayDelay', str(self.displayDelay))
        xmlelement.set('locked', str(self.locked))
        xmlelement.set('persistent', str(self.persistent))
        xmlelement.set('fromTemplate', str(self.fromTemplate))
        xmlelement.set('opacity', str(self.opacity))
        xmlelement.set('source', self.source)
        xmlelement.set('bezelRadius', str(self.bezelRadius))
        xmlelement.set('rotation', str(self.rotation))
        xmlelement.set('drawingFill', str(self.drawingFill))
        xmlelement.set('drawingShadow', str(self.drawingShadow))
        xmlelement.set('drawingStroke', str(self.drawingStroke))

        # Serialize child objects.
        if self.position is not None:
            xmlelement.append(self.position.serializexml())

        if self.shadow is not None:
            xmlelement.append(self.shadow.serializexml())

        xml_dict = self.createdictionary('stroke')
        for k,v in self.stroke.items():
            xml_value = v.serializexml()
            xml_value.set('rvXMLDictionaryKey', k)
            xml_dict.append(xml_value)

        xmlelement.append(xml_dict)


class RVImageElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        super().__init__(xmlelement)

        self.fillColor = NSColor()
        self.scaleBehavior = 3
        self.flippedHorizontally = False
        self.flippedVertically = False
        self.scaleSize = RVScaleFactor()

        # Add child objects here.
        self.position = None
        self.stroke = dict()
        self.shadow = None
        self.effects = list()

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.fillColor = NSColor(xmlelement.get('fillColor'))
        self.scaleBehavior = int(xmlelement.get('scaleBehavior'))
        self.flippedHorizontally = bool(xmlelement.get('flippedHorizontally'))
        self.flippedVertically = bool(xmlelement.get('flippedVertically'))
        self.scaleSize = RVScaleFactor(xmlelement.get('scaleSize'))

        xml_list = xmlelement.find("./array[@rvXMLIvarName='effects']")
        for cnode in xml_list:
            self.effects.append(util.createobject(cnode))

    def serializexml(self):
        xmlelement = xmltree.Element('RVImageElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('fillColor', str(self.fillColor))
        xmlelement.set('scaleBehavior', str(self.scaleBehavior))
        xmlelement.set('flippedHorizontally', str(self.flippedHorizontally))
        xmlelement.set('flippedVertically', str(self.flippedVertically))
        xmlelement.set('scaleSize', str(self.scaleSize))

        xml_effects = self.createarray('effects')
        for cur_effect in self.effects:
            xml_effects.append(cur_effect.serializexml())

        xmlelement.append(xml_effects)

        return xmlelement


class RVTextElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        super().__init__(xmlelement)

        self.adjustsHeightToFit = False
        self.verticalAlignment = 0
        self.revealType = 0

        # Add child objects here.
        self.effects = list()

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.adjustsHeightToFit = bool(xmlelement.get('adjustsHeightToFit'))
        self.verticalAlignment = int(xmlelement.get('verticalAlignment'))
        self.revealType = int(xmlelement.get('revealType'))

    def serializexml(self):
        xmlelement = xmltree.Element('RVImageElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('adjustsHeightToFit', self.adjustsHeightToFit)
        xmlelement.set('verticalAlignment', self.verticalAlignment)
        xmlelement.set('revealType', self.revealType)

        return xmlelement

