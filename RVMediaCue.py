from RVObject import RVObject
import util

import uuid

import xml.etree.ElementTree as xmltree

class RVBaseCue(RVObject):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.UUID = str(uuid.uuid4())
        self.displayName = ""
        self.actionType = 0
        self.enabled = False
        self.timeStamp = 0.000000
        self.delayTime = 0.000000

        if xmlelement is None:
            return

        # Load variables from XML.
        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        # Deserialize from XML.
        self.UUID = xmlelement.get('UUID')
        self.displayName = xmlelement.get('displayName')
        self.actionType = int(xmlelement.get('actionType'))
        self.enabled = xmlelement.get('enabled').lower() == 'true'
        self.timeStamp = float(xmlelement.get('timeStamp'))
        self.delayTime = float(xmlelement.get('delayTime'))

    def serializexmlmedia(self,xmlelement):
        xmlelement.set('UUID', str(self.UUID))
        xmlelement.set('displayName', self.displayName)
        xmlelement.set('actionType', str(self.actionType))
        xmlelement.set('enabled', str(self.enabled).lower())
        xmlelement.set('timeStamp', "{:.6f}".format(self.timeStamp))
        xmlelement.set('delayTime', "{:.6f}".format(self.delayTime))

    def serializexml(self):
        xmlelement = xmltree.Element('RVBaseCue')
        self.serializexmlmedia(xmlelement)

        return xmlelement


class RVSlideTimerCue(RVBaseCue):
    def __init__(self, xmlelement=None):
        self.loopToBeginning = False
        self.duration = 7.0

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.loopToBeginning = bool(xmlelement.get('loopToBeginning'))
        self.duration = float(xmlelement.get('duration'))

    def serializexml(self):
        xmlelement = xmltree.Element('RVSlideTimerCue')
        self.serializexmlmedia(xmlelement)
        xmlelement.set('loopToBeginning', str(self.loopToBeginning).lower())
        xmlelement.set('duration', '{:.6f}'.format(self.duration))

        return xmlelement


class RVAudioCue(RVBaseCue):
    def __init__(self, xmlelement=None):
        self.mediaelement = None

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)

        try:
            xml_mediaelement = xmlelement[0]
            self.mediaelement = util.createobject(xml_mediaelement)
        except:
            a = 1
            pass


    def serializexmlmedia(self, xmlelement):
        super().serializexmlmedia(xmlelement)
        if self.mediaelement is not None:
            xmlelement.append(self.mediaelement.serializexml())


    def serializexml(self):
        xmlelement = xmltree.Element('RVAudioCue')
        self.serializexmlmedia(xmlelement)

        return xmlelement


class RVLiveVideoCue(RVBaseCue):
    def __init__(self, xmlelement=None):
        self.behavior = 0
        self.alignment = 0
        self.dateAdded = ""

        self.livevideoelement = None

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)

        self.behavior = int(xmlelement.get('behavior'))
        self.alignment = int(xmlelement.get('alignment'))
        self.dateAdded = xmlelement.get('dateAdded')

        xml_livevideoelement = xmlelement[0]
        self.livevideoelement = util.createobject(xml_livevideoelement)

    def serializexml(self):
        xmlelement = xmltree.Element('RVLiveVideoCue')
        self.serializexmlmedia(xmlelement)

        xmlelement.set('behavior', str(self.behavior))
        xmlelement.set('alignment', str(self.alignment))
        xmlelement.set('dateAdded', self.dateAdded)

        if self.livevideoelement is not None:
            xmlelement.append(self.livevideoelement.serializexml())

        return xmlelement


class RVClearCue(RVBaseCue):
    def __init__(self, xmlelement=None):
        super().__init__(xmlelement)

    def serializexml(self):
        xmlelement = xmltree.Element('RVClearCue')
        self.serializexmlmedia(xmlelement)

        return xmlelement


class RVMediaCue(RVAudioCue):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.behavior = 1
        self.nextCueUUID = ""
        self.alignment = 4
        self.dateAdded = ""
        self.tags = ""
        self.rvXMLIvarName = "backgroundMediaCue"

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        # Deserialize from XML.
        self.UUID = xmlelement.get('UUID')
        self.displayName = xmlelement.get('displayName')
        self.actionType = int(xmlelement.get('actionType'))
        self.enabled = xmlelement.get('enabled').lower() == 'true'
        self.timeStamp = float(xmlelement.get('timeStamp'))
        self.delayTime = float(xmlelement.get('delayTime'))
        self.behavior = int(xmlelement.get('behavior'))
        self.nextCueUUID = xmlelement.get('nextCueUUID')
        self.alignment = int(xmlelement.get('alignment'))
        self.dateAdded = xmlelement.get('dateAdded')
        self.tags = xmlelement.get('tags')
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

        xml_mediaelement = xmlelement[0]
        self.mediaelement = util.createobject(xml_mediaelement)

    def serializexml(self):
        xmlelement = xmltree.Element('RVMediaCue')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('behavior', str(self.behavior))
        xmlelement.set('nextCueUUID', self.nextCueUUID)
        xmlelement.set('alignment', str(self.alignment))
        xmlelement.set('dateAdded', self.dateAdded)
        xmlelement.set('tags', self.tags)
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)
        # TODO - Serialize back into XML structure.

        return xmlelement
