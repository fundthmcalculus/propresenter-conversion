import re


class RVDateTime:
    def __init__(self, datetimestring=None):
        self.year = 1993
        self.month = 10
        self.day = 19
        self.hour = 10
        self.minute = 43
        self.second = 10
        self.houroffset = -4
        self.minuteoffset = 0

        # Parse the string.
        if datetimestring is not None and len(datetimestring) > 0:
            toks = re.split('[\ \-T:]*', datetimestring)
            self.year = float(toks[0])
            self.month = float(toks[1])
            self.day = float(toks[2])
            self.hour = float(toks[3])
            self.minute = float(toks[4])
            self.second = float(toks[5])
            self.houroffset = float(toks[6])
            self.minuteoffset = float(toks[7])

    def __repr__(self):
        return "%04d:%02d:%02dT%02d:%02d:%02d-%02d:%02d" % (self.year, self.month, self.day,
            self.hour, self.minute, self.second, self.houroffset, self.minuteoffset)
