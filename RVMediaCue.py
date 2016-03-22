from RVObject import RVObject
import util

import uuid

import xml.etree.ElementTree as xmltree


class RVAudioCue(RVObject):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.UUID = str(uuid.uuid4())
        self.displayName = ""
        self.actionType = 0
        self.enabled = False
        self.timeStamp = 0.000000
        self.delayTime = 0.000000

        # Add child objects here.
        self.mediaelement = None

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

        xml_mediaelement = xmlelement[0]
        self.mediaelement = util.createobject(xml_mediaelement)

    def serializexmlmedia(self,xmlelement):
        xmlelement.set('UUID', str(self.UUID))
        xmlelement.set('displayName', self.displayName)
        xmlelement.set('actionType', str(self.actionType))
        xmlelement.set('enabled', str(self.enabled).lower())
        xmlelement.set('timeStamp', "{:.6f}".format(self.timeStamp))
        xmlelement.set('delayTime', "{:.6f}".format(self.delayTime))
        # Serialize back into XML structure.

        if self.mediaelement is not None:
            xmlelement.append(self.mediaelement.serializexml())

    def serializexml(self):
        xmlelement = xmltree.Element('RVAudioCue')
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
