from RVObject import RVObject
from RVColor import RVColor
import uuid

class RVSlideGrouping(RVObject):
    def __init__(self,xmlelement=None):
        self.name = ""
        self.uuid = str(uuid.uuid4())
        self.color = RVColor()

        # Create child objects here.
        self.slides = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)


    def deserializexml(self,xmlelement):
        self.name = xmlelement.get('name')
        self.uuid = xmlelement.get('uuid')
        self.color = RVColor(xmlelement.get('color'))

        # Use XPath to find the slides object.
        xml_slides = xmlelement.find("./*[@rvXMLIvarName='slides']")

        for xml_slide in xml_slides:
            # TODO - Create the actual slide objects.
            self.slides.append(RVDisplaySlide(xml_slide))

    def serializexml(self,xmlelement):
        xmlelement.set('name', self.name)
        xmlelement.set('uuid', self.uuid)
        xmlelement.set('color', str(self.color))

        # TODO - Serialize the child objects back out to XML