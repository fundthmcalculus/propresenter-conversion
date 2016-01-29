from RVObject import RVObject


class RVTimeline(RVObject):
    def __init__(self,xmlelement=None):
        # Create all variables here.
        self.timeOffset = 0.000000
        self.duration = 0.000000
        self.selectedMediaTrackIndex = 0
        self.loop = False
        self.rvXMLIvarName = "timeline"

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self,xmlelement):
        self.timeOffset = float(xmlelement.get('timeOffset'))
        self.duration = float(xmlelement.get('duration'))
        self.selectedMediaTrackIndex = int(xmlelement.get('selectedMediaTrackIndex'))
        self.loop = bool(xmlelement.get('loop'))
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

    def serializexml(self,xmlelement):
        xmlelement.set('timeOffset', str(self.timeOffset))
        xmlelement.set('duration', str(self.duration))
        xmlelement.set('selectedMediaTrackIndex', str(self.selectedMediaTrackIndex))
        xmlelement.set('loop', str(self.loop))
        xmlelement.set('rvXMLIvarName', str(self.rvXMLIvarName))