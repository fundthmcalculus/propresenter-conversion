from RVObject import RVObject

import xml.etree.ElementTree as xmltree


class RVTimeline(RVObject):
    def __init__(self,xmlelement=None):
        # Create all variables here.
        self.timeOffset = 0.000000
        self.duration = 0.000000
        self.selectedMediaTrackIndex = 0
        self.loop = False
        self.rvXMLIvarName = "timeline"

        # Child objects.
        self.timeCues = []
        self.mediaTracks = []

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self,xmlelement):
        self.timeOffset = float(xmlelement.get('timeOffset'))
        self.duration = float(xmlelement.get('duration'))
        self.selectedMediaTrackIndex = int(xmlelement.get('selectedMediaTrackIndex'))
        self.loop = xmlelement.get('loop').lower() == 'true'
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

        # Add the time cues object
        xml_timecues = xmlelement.find("./*[@rvXMLIvarName='timeCues']")
        for xml_timecue in xml_timecues:
            # TODO - Support time cues.
            a = 1

        xml_mediatracks = xmlelement.find("./*[@rvXMLIvarName='mediaTracks']")
        for xml_mediatracks in xml_mediatracks:
            # TODO - Support media tracks.
            a = 1

    def serializexml(self):
        xmlelement = xmltree.Element('RVTimeline')
        xmlelement.set('timeOffset', "{:.6f}".format(self.timeOffset))
        xmlelement.set('duration', "{:.6f}".format(self.duration))
        xmlelement.set('selectedMediaTrackIndex', str(self.selectedMediaTrackIndex))
        xmlelement.set('loop', str(self.loop).lower())
        xmlelement.set('rvXMLIvarName', str(self.rvXMLIvarName))

        # Add the child nodes.
        timecueselement = self.createarray('timeCues')
        xmlelement.append(timecueselement)

        mediatrackselement = self.createarray('mediaTracks')
        xmlelement.append(mediatrackselement)

        return xmlelement
