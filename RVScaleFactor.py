from formatutilities import rvnumberformat


class RVScaleFactor:
    def __init__(self, scalestring=None, xscale=1, yscale=1):
        self.xscale = xscale
        self.yscale = yscale

        if scalestring is not None:
            scalestring = scalestring.replace("{","").replace("}","").replace(",","")
            toks = scalestring.split()
            self.xscale = float(toks[0])
            self.yscale = float(toks[1])

    def __repr__(self):
        return "{" + rvnumberformat(self.xscale) + ", " + rvnumberformat(self.yscale) + "}"