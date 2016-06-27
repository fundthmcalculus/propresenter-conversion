from NSColor import NSColor
from RVDateTime import RVDateTime
from RVObject import RVObject
from RVBibleReference import RVBibleReference
from RVSlideGrouping import RVSlideGrouping
from RVTimeline import RVTimeline

import xml.etree.ElementTree as xmltree


class RVPresentationDocument(RVObject):
    def __init__(self,xmlelement=None):
        # Create all variables here.
        self.versionNumber = 600
        self.docType = 0
        self.width = 1280
        self.height = 720
        self.usedCount = 0
        self.backgroundColor = NSColor()
        self.buildNumber = 15122
        self.drawingBackgroundColor = False
        self.CCLIDisplay = True
        self.lastDateUsed = RVDateTime()
        self.selectedArrangementID = ""
        self.category = "Default"
        self.resourcesDirectory = ""
        self.notes = ""
        self.os = 2
        self.CCLIAuthor = ""
        self.CCLIArtistCredits = ""
        self.CCLISongTitle = ""
        self.CCLIPublisher = ""
        self.CCLICopyrightYear = ""
        self.CCLISongNumber = ""
        self.chordChartPath = ""

        # Create child objects here.
        self.biblereference = None
        self.timeline = None
        self.arrangements = []
        self.groups = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self,xmlelement):
        """

        :type xmlelement: xml.etree.ElementTree.Element
        """
        # Load from each XML attribute.
        self.versionNumber = int(xmlelement.get('versionNumber'))
        self.docType = int(xmlelement.get('docType'))
        self.width = int(xmlelement.get('width'))
        self.height = int(xmlelement.get('height'))
        self.usedCount = int(xmlelement.get('usedCount'))
        self.backgroundColor = NSColor(RGBAstring=xmlelement.get('backgroundColor'))
        self.buildNumber = int(xmlelement.get('buildNumber', default=str(self.buildNumber)))
        self.drawingBackgroundColor = xmlelement.get('drawingBackgroundColor').lower() == 'true'
        self.CCLIDisplay = xmlelement.get('CCLIDisplay').lower() == 'true'
        self.lastDateUsed = RVDateTime(datetimestring=xmlelement.get('lastDateUsed'))
        self.selectedArrangementID = xmlelement.get('selectedArrangementID')
        self.category = xmlelement.get('category')
        self.resourcesDirectory = xmlelement.get('resourcesDirectory')
        self.notes = xmlelement.get('notes')
        self.os = int(xmlelement.get('os', default=str(self.buildNumber)))
        self.CCLIAuthor = xmlelement.get('CCLIAuthor')
        self.CCLIArtistCredits = xmlelement.get('CCLIArtistCredits')
        self.CCLISongTitle = xmlelement.get('CCLISongTitle')
        self.CCLIPublisher = xmlelement.get('CCLIPublisher')
        self.CCLICopyrightYear = xmlelement.get('CCLICopyrightYear')
        self.CCLISongNumber = xmlelement.get('CCLISongNumber')
        self.chordChartPath = xmlelement.get('chordChartPath')

        xml_timeline = xmlelement.find("RVTimeline")
        if xml_timeline is not None:
            self.timeline = RVTimeline(xml_timeline)

        # Build the bible reference.
        xml_biblereference = xmlelement.find("RVBibleReference")
        if xml_biblereference is not None:
            self.biblereference = RVBibleReference(xml_biblereference)

        # Use XPath to find the arrangements object and the groups object
        xml_arrangements = xmlelement.find("./*[@rvXMLIvarName='arrangements']")
        xml_groups = xmlelement.find("./*[@rvXMLIvarName='groups']")

        # Create the slide groups.
        for xml_group in xml_groups:
            self.groups.append(RVSlideGrouping(xml_group))

    def serializexml(self):
        xmlelement = xmltree.Element('RVPresentationDocument')
        xmlelement.set('versionNumber', str(self.versionNumber))
        xmlelement.set('docType', str(self.docType))
        xmlelement.set('drawingBackgroundColor', str(self.drawingBackgroundColor).lower())
        xmlelement.set('width', str(self.width))
        xmlelement.set('height', str(self.height))
        xmlelement.set('usedCount', str(self.usedCount))
        xmlelement.set('backgroundColor', str(self.backgroundColor))
        xmlelement.set('buildNumber', str(self.buildNumber))
        xmlelement.set('CCLIDisplay', str(self.CCLIDisplay).lower())
        xmlelement.set('lastDateUsed', str(self.lastDateUsed))
        xmlelement.set('selectedArrangementID', str(self.selectedArrangementID))
        xmlelement.set('category', str(self.category))
        xmlelement.set('resourcesDirectory', str(self.resourcesDirectory))
        xmlelement.set('notes', str(self.notes))
        xmlelement.set('os', str(self.os))
        xmlelement.set('CCLIAuthor', str(self.CCLIAuthor))
        xmlelement.set('CCLIArtistCredits', str(self.CCLIArtistCredits))
        xmlelement.set('CCLISongTitle', str(self.CCLISongTitle))
        xmlelement.set('CCLIPublisher', str(self.CCLIPublisher))
        xmlelement.set('CCLICopyrightYear', str(self.CCLICopyrightYear))
        xmlelement.set('CCLISongNumber', str(self.CCLISongNumber))
        xmlelement.set('chordChartPath', str(self.chordChartPath))

        # Serialize back out to xml.
        if self.timeline is not None:
            xmlelement.append(self.timeline.serializexml())

        if self.biblereference is not None:
            xmlelement.append(self.biblereference.serializexml())

        # Serialize the groups list.
        rvGroupsArrayElement = self.createarray('groups')
        for cslidegroup in self.groups:
            rvGroupsArrayElement.append(cslidegroup.serializexml())
        xmlelement.append(rvGroupsArrayElement)

        # Serialize the arrangements list.
        rvArrangementsArrayElement = self.createarray('arrangements')
        xmlelement.append(rvArrangementsArrayElement)

        return xmlelement
