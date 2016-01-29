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
        self.timeOffset = float(xmlelement.attrib['timeOffset'])
        self.duration = float(xmlelement.attrib['duration'])
        self.selectedMediaTrackIndex = int(xmlelement.attrib['selectedMediaTrackIndex'])
        self.loop = bool(xmlelement.attrib['loop'])
        self.rvXMLIvarName = xmlelement.attrib['rvXMLIvarName']