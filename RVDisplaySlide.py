from RVObject import RVObject
from RVColor import RVColor
import uuid


class RVDisplaySlide(RVObject):
    def __init__(self,xmlelement=None):
        self.backgroundColor = RVColor()
        self.highlightColor = RVColor()
        self.drawingBackgroundColor = False
        self.enabled = True
        self.hotKey = ""
        self.label = ""
        self.UUID = str(uuid.uuid4())
        self.chordChartPath = ""
        self.notes = ""
        self.socialItemCount = 1

        # TODO - Create child objects here.

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self,xmlelement):
        self.backgroundColor = RVColor(xmlelement.get('backgroundColor'))
        self.highlightColor = RVColor(xmlelement.get('highlightColor'))
        self.drawingBackgroundColor = bool(xmlelement.get('drawingBackgroundColor'))
        self.enabled = bool(xmlelement.get('enabled'))
        self.hotKey = xmlelement.get('hotKey')
        self.label = xmlelement.get('label')
        self.UUID = xmlelement.get('UUID')
        self.chordChartPath = xmlelement.get('chordChartPath')
        self.notes = xmlelement.get('notes')
        self.socialItemCount = xmlelement.get('socialItemCount')

        # TODO - Deserialize child objects

    def serializexml(self,xmlelement):
        xmlelement.set('backgroundColor', str(self.backgroundColor))
        xmlelement.set('highlightColor', str(self.highlightColor))
        xmlelement.set('drawingBackgroundColor', str(self.drawingBackgroundColor))
        xmlelement.set('enabled', str(self.enabled))
        xmlelement.set('hotKey', self.hotKey)
        xmlelement.set('label', self.label)
        xmlelement.set('UUID', self.UUID)
        xmlelement.set('chordChartPath', self.chordChartPath)
        xmlelement.set('notes', self.notes)
        xmlelement.set('socialItemCount', self.socialItemCount)

        # TODO - Serialize child objects.