from dmsToddConverter import validateCoordinates, convertDmsToDd


def getThresholds(data):
    thresholdPoints = {}
    for n in range(len(data)):
        thresholdPoints[n] = data[n]['Threshold']
    return thresholdPoints


def convertThresholds(thresholds):
    temp = {}
    identifiers = ['latitude', 'longitude']
    for n in range(len(thresholds)):
        temp[n] = validateCoordinates(thresholds[n])
        temp[n][identifiers[0]] = convertDmsToDd(temp[n][identifiers[0]])
        temp[n][identifiers[1]] = convertDmsToDd(temp[n][identifiers[1]])
    return temp
