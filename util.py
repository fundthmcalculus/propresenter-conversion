from NSColor import *
from NSNumber import *
from RVBibleReference import *
from RVDateTime import *
from RVMediaElement import *
from RVObject import RVObject
from RVRect3D import RVRect3D
from RVScaleFactor import RVScaleFactor
from RVSlideGrouping import *
from RVTimeline import RVTimeline
from shadow import shadow
from RVEffect import *


def createobject(xmlelement):
    elementtype = xmlelement.tag

    # Use reflection.
    obj = globals()[elementtype](xmlelement)

    return obj
