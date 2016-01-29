from RVObject import RVObject


class RVBibleReference(RVObject):
    def __init__(self,xmlelement=None):
        # Create variables.
        self.translationAbbreviation = ""
        self.translationName = ""
        self.bookName = ""
        self.bookIndex = 0
        self.chapterStart = 0
        self.chapterEnd = 0
        self.verseStart = 0
        self.verseEnd = 0
        self.rvXMLIvarName = "bibleReference"


        self.deserializexml(xmlelement)

    def deserializexml(self,xmlelement):
        """

        :type xmlelement: xml.etree.ElementTree.Element
        """
        self.translationAbbreviation = xmlelement.attrib['translationAbbreviation']
        self.translationName = xmlelement.attrib['translationName']
        self.bookName = xmlelement.attrib['bookName']
        self.bookIndex = int(xmlelement.attrib['bookIndex'])
        self.chapterStart = int(xmlelement.attrib['chapterStart'])
        self.chapterEnd = int(xmlelement.attrib['chapterEnd'])
        self.verseStart = int(xmlelement.attrib['verseStart'])
        self.verseEnd = int(xmlelement.attrib['verseEnd'])
        self.rvXMLIvarName = xmlelement.attrib['rvXMLIvarName']


