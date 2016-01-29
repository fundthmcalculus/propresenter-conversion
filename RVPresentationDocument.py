from RVColor import RVColor
from RVDateTime import RVDateTime
from RVObject import RVObject
from RVBibleReference import RVBibleReference


class RVPresentationDocument(RVObject):
    def __init__(self,xmlelement=None):
        # Create all variables here.
        self.versionNumber = 600
        self.docType = 0
        self.width = 1280
        self.height = 720
        self.usedCount = 0
        self.backgroundColor = RVColor()
        self.drawingBackgroundColor = False
        self.CCLIDisplay = True
        self.lastDateUsed = RVDateTime()
        self.selectedArrangementID = ""
        self.category = "Default"
        self.resourcesDirectory = ""
        self.notes = ""
        self.CCLIAuthor = ""
        self.CCLIArtistCredits = ""
        self.CCLISongTitle = ""
        self.CCLIPublisher = ""
        self.CCLICopyrightYear = ""
        self.CCLISongNumber = ""
        self.chordChartPath = ""

        # Create child objects here.
        self.biblereference = []
        self.arrangements = []
        self.groups = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

        # Loop through the child XML nodes and build those.
        for xmlbiblereference in xmlelement.findall("RVBibleReference"):
            # Create the Bible reference object.
            self.biblereference = RVBibleReference(xmlbiblereference)

        # Use XPath to find the arrangements object and the groups object
        xml_arrangements = xmlelement.find(".//[@rvXMLIvarName='arrangements']")
        xml_groups = xmlelement.find(".//[@rvXMLIvarName='groups']")

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
        self.backgroundColor = RVColor(RGBAstring=xmlelement.get('backgroundColor'))
        self.CCLIDisplay = bool(xmlelement.get('CCLIDisplay'))
        self.lastDateUsed = RVDateTime(datetimestring=xmlelement.get('lastDateUsed'))
        self.selectedArrangementID = xmlelement.get('selectedArrangementID')
        self.category = xmlelement.get('category')
        self.resourcesDirectory = xmlelement.get('resourcesDirectory')
        self.notes = xmlelement.get('notes')
        self.CCLIAuthor = xmlelement.get('CCLIAuthor')
        self.CCLIArtistCredits = xmlelement.get('CCLIArtistCredits')
        self.CCLISongTitle = xmlelement.get('CCLISongTitle')
        self.CCLIPublisher = xmlelement.get('CCLIPublisher')
        self.CCLICopyrightYear = xmlelement.get('CCLICopyrightYear')
        self.CCLISongNumber = xmlelement.get('CCLISongNumber')
        self.chordChartPath = xmlelement.get('chordChartPath')

    def serializexml(self,xmlelement):
        xmlelement.set('versionNumber', str(self.versionNumber))
        xmlelement.set('docType', str(self.docType))
        xmlelement.set('width', str(self.width))
        xmlelement.set('height', str(self.height))
        xmlelement.set('usedCount', str(self.usedCount))
        xmlelement.set('backgroundColor', str(self.backgroundColor))
        xmlelement.set('CCLIDisplay', str(self.CCLIDisplay))
        xmlelement.set('lastDateUsed', str(self.lastDateUsed))
        xmlelement.set('selectedArrangementID', str(self.selectedArrangementID))
        xmlelement.set('category', str(self.category))
        xmlelement.set('resourcesDirectory', str(self.resourcesDirectory))
        xmlelement.set('notes', str(self.notes))
        xmlelement.set('CCLIAuthor', str(self.CCLIAuthor))
        xmlelement.set('CCLIArtistCredits', str(self.CCLIArtistCredits))
        xmlelement.set('CCLISongTitle', str(self.CCLISongTitle))
        xmlelement.set('CCLIPublisher', str(self.CCLIPublisher))
        xmlelement.set('CCLICopyrightYear', str(self.CCLICopyrightYear))
        xmlelement.set('CCLISongNumber', str(self.CCLISongNumber))
        xmlelement.set('chordChartPath', str(self.chordChartPath))
