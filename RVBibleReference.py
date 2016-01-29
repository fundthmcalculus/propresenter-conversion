from RVObject import RVObject


class RVBibleReference(RVObject):
    def __init__(self, xmlelement=None):
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
        self.translationAbbreviation = xmlelement.get('translationAbbreviation')
        self.translationName = xmlelement.get('translationName')
        self.bookName = xmlelement.get('bookName')
        self.bookIndex = int(xmlelement.get('bookIndex'))
        self.chapterStart = int(xmlelement.get('chapterStart'))
        self.chapterEnd = int(xmlelement.get('chapterEnd'))
        self.verseStart = int(xmlelement.get('verseStart'))
        self.verseEnd = int(xmlelement.get('verseEnd'))
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

    def serializexml(self,xmlelement):
        xmlelement.set('translationAbbreviation', str(self.translationAbbreviation))
        xmlelement.set('translationName', str(self.translationName))
        xmlelement.set('bookName', str(self.bookName))
        xmlelement.set('bookIndex', str(self.bookIndex))
        xmlelement.set('chapterStart', str(self.chapterStart))
        xmlelement.set('chapterEnd', str(self.chapterEnd))
        xmlelement.set('verseStart', str(self.verseStart))
        xmlelement.set('verseEnd', str(self.verseEnd))
        xmlelement.set('rvXMLIvarName', str(self.rvXMLIvarName))

