

def rvnumberformat(number, formatstring=None):
    numberstring = str(number)
    if formatstring is not None:
        numberstring = formatstring.format(number)

    # Check for existence of decimal place.
    if '.' not in numberstring:
        return numberstring

    return numberstring.rstrip('0').rstrip('.')