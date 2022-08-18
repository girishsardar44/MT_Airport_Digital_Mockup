import re
from geojson import Point, Feature
from extractInfoFromJson import extractUsableDataFromJson
from dmsToddConverter import validateCoordinates, convertDmsToDd
extract = extractUsableDataFromJson()


class TransformDataCommon:

    def convertCoordinatesToDMS(self, coordinates):
        identifiers = ['latitude', 'longitude']
        for n in coordinates.keys():
            coordinates[n] = validateCoordinates(coordinates[n])
            coordinates[n][identifiers[0]] = convertDmsToDd(
                coordinates[n][identifiers[0]])
            coordinates[n][identifiers[1]] = convertDmsToDd(
                coordinates[n][identifiers[1]])
        return coordinates

    def createKeysArray(self, start=0, end=10, stepSize=1):
        keys = []
        for m in range(start, end, stepSize):
            keys.append(str(m))
        return keys

    def createGeoJsonPointFeatures(self, coordinates):
        features = {}
        for n in coordinates.keys():
            features[n] = Feature(geometry=Point(
                (coordinates[n]['longitude'], coordinates[n]['latitude']), precision=15))
        return features
