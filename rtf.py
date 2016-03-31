

def addcolortotable(rtfstring, newcolor):
    # Find the color table.
    clrtblidx = rtfstring.find("\\colortbl")
    # Find the end of the table.
    endclrtblidx = rtfstring.find(";", clrtblidx)

    # Append to the end of the table the new color.
    return rtfstring[:endclrtblidx] + ";" + newcolor.RTFcolorstring() + rtfstring[endclrtblidx:]
