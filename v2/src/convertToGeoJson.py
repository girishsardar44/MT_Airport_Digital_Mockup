import json
from extractInfoFromJson import extractUsableDataFromJson
from constants import tableHeaderKeys
from cleanJsonData import cleanData
from clubThresholdAndproperties import createGeoJsonPointFeatures, combinePointAndProperties
# from geojson import Point, Feature, FeatureCollection
from convertThresholds import getThresholds, convertThresholds
extract = extractUsableDataFromJson()
jsonData = extract.loadJson(fileNameWithExtension="coruna_AD.json")


def createKeysArray(start=0, end=10, stepSize=1):
    keys = []
    for n in range(start, end, stepSize):
        keys.append(str(n))
    return keys


def changeDataKeys(data):
    del data[0]
    newData = {}
    for n in range(len(data)):
        newData[n] = dict(zip(tableHeaderKeys.values(), data[n].values()))
    return (newData)


k = changeDataKeys(data=jsonData)
m = cleanData(k)
n = getThresholds(m)
u = convertThresholds(n)
y = createGeoJsonPointFeatures(u)
z = combinePointAndProperties(y,k)
print(z)

# l = json.dumps()
# print((l))

# m= extract.dimensions(k[1][tableHeaderKeys['3']])
# print(m)
# print(k[1][tableHeaderKeys['0']])
