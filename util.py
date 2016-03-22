import NSColor
import NSNumber
import NSString
import RVBibleReference
import RVDateTime
import RVDisplaySlide
import RVEffect
import RVMediaCue
import RVMediaElement
import RVObject
import RVPresentationDocument
import RVRect3D
import RVScaleFactor
import RVSlideGrouping
import RVTimeline
import shadow

import types
import inspect


def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val


def allclasses():
    classes = list()
    for module in imports():
        classes.extend(inspect.getmembers(module ,inspect.isclass))

    return classes


def createobject(xmlelement):
    elementtype = xmlelement.tag

    # List of imported modules.
    importedclasses = allclasses()

    # Use reflection.
    for curclass in importedclasses:
        if curclass[0] == elementtype:
            return curclass[1](xmlelement)

    raise Exception("No class with the name '" + elementtype + "' exists or is imported.")
