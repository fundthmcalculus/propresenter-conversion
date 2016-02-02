from RVObject import RVObject
from RVColor import RVColor
from RVScaleFactor import RVScaleFactor

import xml.etree.ElementTree as xmltree
import uuid


class RVMediaElement(RVObject):
    def __init__(self, xmlelement=None):
        # TODO - Default initialize all parameters.
        self.UUID = uuid.uuid4()

    @staticmethod
    def createmediaelement(xmlelement):
        # TODO - Create the child objects.
        return RVImageElement(xmlelement)

    def deserializexml(self, xmlelement):
        # TODO - Deserialize from XML
        self.UUID = xmlelement.get("UUID")

    def serializexmlmedia(self,xmlelement):
        xmlelement.set("UUID", self.UUID)


class RVImageElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        super().__init__(xmlelement)

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
        self.fillColor = RVColor()
        self.scaleBehavior = 3
        self.flippedHorizontally = False
        self.flippedVertically = False
        self.scaleSize = RVScaleFactor()

        # Add child objects here.

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
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
        self.fillColor = RVColor(xmlelement.get('fillColor'))
        self.scaleBehavior = int(xmlelement.get('scaleBehavior'))
        self.flippedHorizontally = bool(xmlelement.get('flippedHorizontally'))
        self.flippedVertically = bool(xmlelement.get('flippedVertically'))
        self.scaleSize = RVScaleFactor(xmlelement.get('scaleSize'))

    def serializexml(self):
        xmlelement = xmltree.Element('RVImageElement')
        super().serializexmlmedia(xmlelement)
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
        xmlelement.set('fillColor', str(self.fillColor))
        xmlelement.set('scaleBehavior', str(self.scaleBehavior))
        xmlelement.set('flippedHorizontally', str(self.flippedHorizontally))
        xmlelement.set('flippedVertically', str(self.flippedVertically))
        xmlelement.set('scaleSize', str(self.scaleSize))

        # TODO - serialize child objects.

        return xmlelement

