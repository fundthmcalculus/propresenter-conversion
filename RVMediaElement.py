from RVObject import RVObject
from NSColor import NSColor
from NSString import *
from RVScaleFactor import RVScaleFactor
from RVRect3D import RVRect3D
from shadow import shadow
import util
from formatutilities import rvnumberformat

import xml.etree.ElementTree as xmltree
import uuid


class RVElement(RVObject):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.UUID = str(uuid.uuid4())
        self.displayName = ""
        self.typeID = 0
        self.displayDelay = 0.000000
        self.locked = False
        self.persistent = False
        self.fromTemplate = False
        self.opacity = 1.000000
        self.bezelRadius = 0.000000
        self.rotation = 0.000000
        self.drawingFill = False
        self.drawingShadow = False
        self.drawingStroke = False

        self.position = None
        self.stroke = dict()
        self.shadow = None

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        # Deserialize from XML
        self.UUID = xmlelement.get("UUID")
        self.displayName = xmlelement.get('displayName')
        self.typeID = int(xmlelement.get('typeID'))
        self.displayDelay = float(xmlelement.get('displayDelay'))
        self.locked = xmlelement.get('locked').lower() == 'true'
        self.persistent = xmlelement.get('persistent').lower() == 'true'
        self.fromTemplate = xmlelement.get('fromTemplate').lower() == 'true'
        self.opacity = float(xmlelement.get('opacity'))
        self.bezelRadius = float(xmlelement.get('bezelRadius'))
        self.rotation = float(xmlelement.get('rotation'))
        self.drawingFill = xmlelement.get('drawingFill').lower() == 'true'
        self.drawingShadow = xmlelement.get('drawingShadow').lower() == 'true'
        self.drawingStroke = xmlelement.get('drawingStroke').lower() == 'true'

        xml_pos = xmlelement.find("./RVRect3D[@rvXMLIvarName='position']")
        self.position = RVRect3D(xml_pos)

        xml_shadow = xmlelement.find("./shadow")
        self.shadow = shadow(xml_shadow)

        xml_stroke = xmlelement.find("./dictionary[@rvXMLIvarName='stroke']")
        for cnode in xml_stroke:
            xml_key = cnode.get('rvXMLDictionaryKey')
            # Create the current object.
            self.stroke[xml_key] = util.createobject(cnode)

    def serializexml(self):
        xmlelement = xmltree.Element('RVMediaElement')
        self.serializexmlmedia(xmlelement)

        return xmlelement

    def serializexmlmedia(self, xmlelement):
        xmlelement.set("UUID", self.UUID)
        xmlelement.set('displayName', self.displayName)
        xmlelement.set('typeID', str(self.typeID))
        xmlelement.set('displayDelay', "{:.6f}".format(self.displayDelay))
        xmlelement.set('locked', str(self.locked).lower())
        xmlelement.set('persistent', str(self.persistent).lower())
        xmlelement.set('fromTemplate', str(self.fromTemplate).lower())
        xmlelement.set('opacity', "{:.6f}".format(self.opacity))
        xmlelement.set('bezelRadius', "{:.6f}".format(self.bezelRadius))
        xmlelement.set('rotation', "{:.6f}".format(self.rotation))
        xmlelement.set('drawingFill', str(self.drawingFill).lower())
        xmlelement.set('drawingShadow', str(self.drawingShadow).lower())
        xmlelement.set('drawingStroke', str(self.drawingStroke).lower())

        # Serialize child objects.
        if self.position is not None:
            xmlelement.append(self.position.serializexml())

        if self.shadow is not None:
            xmlelement.append(self.shadow.serializexml())

        xml_dict = self.createdictionary('stroke')
        for k, v in self.stroke.items():
            xml_value = v.serializexml()
            xml_value.set('rvXMLDictionaryKey', k)
            xml_dict.append(xml_value)

        xmlelement.append(xml_dict)


class RVMediaElement(RVElement):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.source = ""

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        # Deserialize from XML
        self.source = xmlelement.get('source', None)

    def serializexml(self):
        xmlelement = xmltree.Element('RVMediaElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('source', self.source)

        return xmlelement


class RVShapeElement(RVElement):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.fillColor = NSColor()

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        # Deserialize from XML
        self.fillColor = NSColor(xmlelement.get('fillColor'))

    def serializexml(self):
        xmlelement = xmltree.Element('RVShapeElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('fillColor', str(self.fillColor))

        return xmlelement


class RVTextCrawlerElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        self.fillColor = NSColor()
        self.adjustsHeightToFit = True
        self.useAllCaps = False
        self.verticalAlignment = 0
        self.revealType = 0
        self.textCrawlerType = 0
        self.rssParsingStyle = 0
        self.loopBehavior = 1
        self.textCrawlerSpeed = 2.808594
        self.textCrawlerSectionDelimiter = ""

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.fillColor = NSColor(xmlelement.get('fillColor'))
        self.adjustsHeightToFit = bool(xmlelement.get('adjustsHeightToFit'))
        self.useAllCaps = bool(xmlelement.get('useAllCaps'))
        self.verticalAlignment = int(xmlelement.get('verticalAlignment'))
        self.revealType = int(xmlelement.get('revealType'))
        self.textCrawlerType = int(xmlelement.get('textCrawlerType'))
        self.rssParsingStyle = int(xmlelement.get('rssParsingStyle'))
        self.loopBehavior = int(xmlelement.get('loopBehavior'))
        self.textCrawlerSpeed = float(xmlelement.get('textCrawlerSpeed'))
        self.textCrawlerSectionDelimiter = xmlelement.get('textCrawlerSectionDelimiter')

    def serializexml(self):
        xmlelement = xmltree.Element('RVLiveVideoElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('fillColor', str(self.fillColor))
        xmlelement.set('adjustsHeightToFit', str(self.adjustsHeightToFit).lower())
        xmlelement.set('useAllCaps', str(self.useAllCaps).lower())
        xmlelement.set('verticalAlignment', str(self.verticalAlignment))
        xmlelement.set('revealType', str(self.revealType))
        xmlelement.set('textCrawlerType', str(self.textCrawlerType))
        xmlelement.set('rssParsingStyle', str(self.rssParsingStyle))
        xmlelement.set('loopBehavior', str(self.loopBehavior))
        xmlelement.set('textCrawlerSpeed', "{:.6f}".format(self.textCrawlerSpeed))
        xmlelement.set('textCrawlerSectionDelimiter', self.textCrawlerSectionDelimiter)

        return xmlelement


class RVLiveVideoElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        self.scaleBehavior = 0
        self.flippedHorizontally = False
        self.flippedVertically = False
        self.scaleSize = RVScaleFactor()
        self.imageOffset = RVScaleFactor()
        self.videoFormatIndex = 0
        self.preserveAspectRatio = True
        self.audioVolume = 0
        self.rvXMLIvarName = "element"

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.scaleBehavior = int(xmlelement.get('scaleBehavior'))
        self.flippedHorizontally = bool(xmlelement.get('flippedHorizontally'))
        self.flippedVertically = bool(xmlelement.get('flippedHorizontally'))
        self.scaleSize = RVScaleFactor(xmlelement.get('scaleSize'))
        self.imageOffset = RVScaleFactor(xmlelement.get('imageOffset'))
        self.videoFormatIndex = int(xmlelement.get('videoFormatIndex'))
        self.preserveAspectRatio = bool(xmlelement.get('preserveAspectRatio'))
        self.audioVolume = float(xmlelement.get('audioVolume'))
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

    def serializexml(self):
        xmlelement = xmltree.Element('RVLiveVideoElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('scaleBehavior', str(self.scaleBehavior))
        xmlelement.set('flippedHorizontally', str(self.flippedHorizontally).lower())
        xmlelement.set('flippedVertically', str(self.flippedVertically).lower())
        xmlelement.set('scaleSize', str(self.scaleSize))
        xmlelement.set('imageOffset', str(self.imageOffset))
        xmlelement.set('videoFormatIndex', str(self.videoFormatIndex))
        xmlelement.set('preserveAspectRatio', str(self.preserveAspectRatio).lower())
        xmlelement.set('audioVolume', '{:.6f}'.format(self.audioVolume))
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)

        return xmlelement


class RVImageElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        self.fillColor = NSColor()
        self.scaleBehavior = 3
        self.flippedHorizontally = False
        self.flippedVertically = False
        self.scaleSize = RVScaleFactor()
        self.imageOffset = RVScaleFactor()
        self.format = ""
        self.manufactureName = ""
        self.manufactureURL = ""

        # Add child objects here.
        self.effects = list()

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.fillColor = NSColor(xmlelement.get('fillColor'))
        self.scaleBehavior = int(xmlelement.get('scaleBehavior'))
        self.flippedHorizontally = xmlelement.get('flippedHorizontally').lower() == 'true'
        self.flippedVertically = xmlelement.get('flippedVertically').lower() == 'true'
        self.scaleSize = RVScaleFactor(xmlelement.get('scaleSize'))
        self.imageOffset = RVScaleFactor(xmlelement.get('imageOffset'))
        self.format = xmlelement.get('format')
        self.manufactureName = xmlelement.get('manufactureName')
        self.manufactureURL = xmlelement.get('manufactureURL')

        xml_list = xmlelement.find("./array[@rvXMLIvarName='effects']")
        if xml_list is not None:
            for cnode in xml_list:
                self.effects.append(util.createobject(cnode))

    def serializexmlmedia(self,xmlelement):
        super().serializexmlmedia(xmlelement)
        xmlelement.set('fillColor', str(self.fillColor))
        xmlelement.set('scaleBehavior', str(self.scaleBehavior))
        xmlelement.set('flippedHorizontally', str(self.flippedHorizontally).lower())
        xmlelement.set('flippedVertically', str(self.flippedVertically).lower())
        xmlelement.set('scaleSize', str(self.scaleSize))
        xmlelement.set('imageOffset', str(self.imageOffset))
        xmlelement.set('format', self.format)
        xmlelement.set('rvXMLIvarName', 'element')
        xmlelement.set('manufactureName', self.manufactureName)
        xmlelement.set('manufactureURL', self.manufactureURL)

        # Make sure we aren't a RVVideoElement object.
        if type(self) is not RVVideoElement:
            xml_effects = self.createarray('effects')
            for cur_effect in self.effects:
                xml_effects.append(cur_effect.serializexml())

            xmlelement.append(xml_effects)

    def serializexml(self):
        xmlelement = xmltree.Element('RVImageElement')
        self.serializexmlmedia(xmlelement)

        return xmlelement


class RVVideoElement(RVImageElement):
    def __init__(self, xmlelement=None):

        self.imageOffset = RVScaleFactor()
        self.format = "H.264"
        self.audioVolume = 1.0
        self.playRate = 1.0
        self.frameRate = 0.0
        self.playbackBehavior = 1.0
        self.inPoint = 0
        self.outPoint = 900
        self.endPoint = 900
        self.timeScale = 30
        self.naturalSize = RVScaleFactor()
        self.fieldType = 0
        self.rvXMLIvarName = "element"

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.imageOffset = RVScaleFactor(xmlelement.get('imageOffset'))
        self.format = xmlelement.get('format')
        self.audioVolume = float(xmlelement.get('audioVolume'))
        self.playRate = float(xmlelement.get('playRate'))
        self.frameRate = float(xmlelement.get('frameRate'))
        self.playbackBehavior = float(xmlelement.get('playbackBehavior'))
        self.inPoint = float(xmlelement.get('inPoint'))
        self.outPoint = float(xmlelement.get('outPoint'))
        self.endPoint = float(xmlelement.get('endPoint'))
        self.timeScale = float(xmlelement.get('timeScale'))
        self.naturalSize = RVScaleFactor(xmlelement.get('naturalSize'))
        self.fieldType = float(xmlelement.get('fieldType'))
        self.rvXMLIvarName = xmlelement.get('rvXMLIvarName')

    def serializexml(self):
        xmlelement = xmltree.Element('RVVideoElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('imageOffset', str(self.imageOffset))
        xmlelement.set('format', self.format)
        xmlelement.set('audioVolume', '{:.6f}'.format(self.audioVolume))
        xmlelement.set('playRate', "{:.6f}".format(self.playRate))
        xmlelement.set('frameRate', "{:.6f}".format(self.frameRate))
        xmlelement.set('playbackBehavior', rvnumberformat(self.playbackBehavior))
        xmlelement.set('inPoint', rvnumberformat(self.inPoint))
        xmlelement.set('outPoint', rvnumberformat(self.outPoint))
        xmlelement.set('endPoint', rvnumberformat(self.endPoint))
        xmlelement.set('timeScale', rvnumberformat(self.timeScale))
        xmlelement.set('naturalSize', str(self.naturalSize))
        xmlelement.set('fieldType', rvnumberformat(self.fieldType))
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)

        return xmlelement


class RVTextElement(RVMediaElement):
    def __init__(self, xmlelement=None):
        self.adjustsHeightToFit = False
        self.verticalAlignment = 0
        self.revealType = 0
        self.fillColor = NSColor()

        self.RTFData = NSString()

        # Add child objects here.
        self.effects = list()

        super().__init__(xmlelement)

    def deserializexml(self, xmlelement):
        super().deserializexml(xmlelement)
        self.adjustsHeightToFit = xmlelement.get('adjustsHeightToFit').lower() == 'true'
        self.verticalAlignment = int(xmlelement.get('verticalAlignment'))
        self.revealType = int(xmlelement.get('revealType'))
        self.fillColor = NSColor(xmlelement.get('fillColor'))
        # Deserialize the RTF Data.
        rtf_xml = xmlelement.find("./NSString[@rvXMLIvarName='RTFData']")
        self.RTFData = NSString(xmlelement=rtf_xml)

    def serializexml(self):
        xmlelement = xmltree.Element('RVTextElement')
        super().serializexmlmedia(xmlelement)
        xmlelement.set('adjustsHeightToFit', str(self.adjustsHeightToFit).lower())
        xmlelement.set('verticalAlignment', str(self.verticalAlignment))
        xmlelement.set('revealType', str(self.revealType))
        xmlelement.set('fillColor', str(self.fillColor))
        xmlelement.append(self.RTFData.serializexml())

        return xmlelement


class RVAudioElement(RVObject):
    def __init__(self, xmlelement=None):
        # Default initialize all parameters.
        self.source = ""
        self.volume = 1.0
        self.playRate = 1.0
        self.loopBehavior = 0
        self.audioType = 0
        self.inPoint = 0.0
        self.outPoint = 1159.0
        self.displayName = ""
        self.artist = ""
        self.rvXMLIvarName = "element"

        if xmlelement is None:
            return

        self.deserializexml(xmlelement)

    def deserializexml(self, xmlelement):
        # Deserialize from XML
        self.source = xmlelement.get("source")
        self.volume = float(xmlelement.get("volume"))
        self.playRate = float(xmlelement.get("playRate"))
        self.loopBehavior = int(xmlelement.get("loopBehavior"))
        self.audioType = int(xmlelement.get("audioType"))
        self.inPoint = float(xmlelement.get("inPoint"))
        self.outPoint = float(xmlelement.get("outPoint"))
        self.displayName = xmlelement.get("displayName")
        self.artist = xmlelement.get("artist")
        self.rvXMLIvarName = xmlelement.get("rvXMLIvarName")

    def serializexml(self):
        xmlelement = xmltree.Element('RVAudioElement')
        xmlelement.set('source', self.source)
        xmlelement.set('volume', '{:.6f}'.format(self.volume))
        xmlelement.set('playRate', '{:.6f}'.format(self.playRate))
        xmlelement.set('loopBehavior', str(self.loopBehavior))
        xmlelement.set('audioType', str(self.audioType))
        xmlelement.set('inPoint', '{:.6f}'.format(self.inPoint))
        xmlelement.set('outPoint', '{:.6f}'.format(self.outPoint))
        xmlelement.set('displayName', self.displayName)
        xmlelement.set('artist', self.artist)
        xmlelement.set('rvXMLIvarName', self.rvXMLIvarName)

        return xmlelement