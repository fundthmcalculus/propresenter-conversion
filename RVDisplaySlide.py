from RVObject import RVObject
from NSColor import NSColor
from RVMediaCue import RVMediaCue
import uuid
import util

import xml.etree.ElementTree as xmltree


class RVDisplaySlide(RVObject):
    def __init__(self, xmlelement=None):
        self.backgroundColor = NSColor()
        self.highlightColor = NSColor()
        self.drawingBackgroundColor = False
        self.enabled = True
        self.hotKey = ""
        self.label = ""
        self.UUID = str(uuid.uuid4())
        self.chordChartPath = ""
        self.notes = ""
        self.socialItemCount = 1

        # Create child objects here.
        self.cues = []
        self.mediacue = None
        self.displayElements = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        self.backgroundColor = NSColor(xmlelement.get('backgroundColor'))
        self.highlightColor = NSColor(xmlelement.get('highlightColor'))
        self.drawingBackgroundColor = xmlelement.get('drawingBackgroundColor').lower() == 'true'
        self.enabled = xmlelement.get('enabled').lower() == 'true'
        self.hotKey = xmlelement.get('hotKey')
        self.label = xmlelement.get('label')
        self.UUID = xmlelement.get('UUID')
        self.chordChartPath = xmlelement.get('chordChartPath')
        self.notes = xmlelement.get('notes')
        self.socialItemCount = xmlelement.get('socialItemCount')

        # Deserialize child objects
        xml_cues = xmlelement.find("./*[@rvXMLIvarName='cues']")
        if xml_cues is not None:
            for xml_cue in xml_cues:
                # Create the actual slide objects.
                self.cues.append(util.createobject(xml_cue))

        xml_cue = xmlelement.find("RVMediaCue")
        if xml_cue is not None:
            self.mediacue = RVMediaCue(xml_cue)

        xml_displayelements = xmlelement.find("./*[@rvXMLIvarName='displayElements']")
        if xml_displayelements is not None:
            for xml_dispelem in xml_displayelements:
                self.displayElements.append(util.createobject(xml_dispelem))

    def serializexml(self):
        xmlelement = xmltree.Element('RVDisplaySlide')
        xmlelement.set('backgroundColor', str(self.backgroundColor))
        xmlelement.set('highlightColor', str(self.highlightColor))
        xmlelement.set('drawingBackgroundColor', str(self.drawingBackgroundColor).lower())
        xmlelement.set('enabled', str(self.enabled).lower())
        xmlelement.set('hotKey', self.hotKey)
        xmlelement.set('label', self.label)
        xmlelement.set('UUID', self.UUID)
        xmlelement.set('chordChartPath', self.chordChartPath)
        xmlelement.set('notes', self.notes)
        xmlelement.set('socialItemCount', self.socialItemCount)

        # Serialize child objects.
        xml_cue_array = self.createarray('cues')
        for c_cue in self.cues:
            xml_cue_array.append(c_cue.serializexml())

        xmlelement.append(xml_cue_array)

        if self.mediacue is not None:
            xmlelement.append(self.mediacue.serializexml())

        xml_elements = self.createarray('displayElements')
        for c_dispelem in self.displayElements:
            xml_elements.append(c_dispelem.serializexml())
        xmlelement.append(xml_elements)

        return xmlelement