import constants
from extractInfoFromJson import extractUsableDataFromJson
from geojson import FeatureCollection

extract = extractUsableDataFromJson()


class TransformRunwayData:

    def getRunwayThresholds(self, data):
        thresholdPoints = {}
        for n in range(len(data)):
            thresholdPoints[n] = data[n]['Threshold']
        return thresholdPoints

    def removeRunwayInvalidData(self, data):
        for n in range(len(data)):
            if data[n][constants.runwayTableHeaderKeys['2']] == "" or 'Direction' in data[n][constants.runwayTableHeaderKeys['2']]:
                del data[n]
            else:
                return data
        return data

    def combineRunwayPointAndProperties(self, features, properties):
        collection = []
        for n in range(len(features)):
            del properties[n]['Threshold']
            features[n]['properties'] = properties[n]
            collection.append(features[n])
        return FeatureCollection(collection)

    def changeRunwayDataKeys(self, data):
        del data[0]
        newData = {}
        for n in range(len(data)):
            newData[n] = dict(
                zip(constants.runwayTableHeaderKeys.values(), data[n].values()))
        return (newData)

    def cleanRunwayData(self, data):
        for n in range(len(data)):
            if data[n][constants.runwayTableHeaderKeys['0']]:
                temp = data[n][constants.runwayTableHeaderKeys['0']]
                data[n][constants.runwayTableHeaderKeys['0']
                        ] = extract.removeExtraData(temp)

            if data[n][constants.runwayTableHeaderKeys['1']]:
                temp = data[n][constants.runwayTableHeaderKeys['1']]
                data[n][constants.runwayTableHeaderKeys['1']
                        ] = extract.direction(temp)

            if data[n][constants.runwayTableHeaderKeys['2']]:
                temp = data[n][constants.runwayTableHeaderKeys['2']]
                temp = extract.removeExtraData(temp)
                data[n][constants.runwayTableHeaderKeys['2']
                        ] = extract.dimensions(temp)

            if data[n][constants.runwayTableHeaderKeys['3']]:
                temp = data[n][constants.runwayTableHeaderKeys['3']]
                temp = extract.thresholdCoordinates(temp)
                data[n][constants.runwayTableHeaderKeys['3']] = temp

            if data[n][constants.runwayTableHeaderKeys['4']]:
                temp = data[n][constants.runwayTableHeaderKeys['4']]
                temp = extract.replaceNewline(temp, " ")

            if data[n][constants.runwayTableHeaderKeys['5']]:
                temp = data[n][constants.runwayTableHeaderKeys['5']]
                temp = extract.removeSpanishCharacters(temp)
                data[n][constants.runwayTableHeaderKeys['5']] = temp

            if data[n][constants.runwayTableHeaderKeys['6']]:
                temp = data[n][constants.runwayTableHeaderKeys['6']]
                temp = extract.removeExtraData(temp)
                data[n][constants.runwayTableHeaderKeys['6']
                        ] = extract.dimensions(temp)

            if data[n][constants.runwayTableHeaderKeys['7']]:
                temp = data[n][constants.runwayTableHeaderKeys['7']]
                temp = extract.removeExtraData(temp)
                data[n][constants.runwayTableHeaderKeys['7']
                        ] = extract.dimensions(temp)

            if data[n][constants.runwayTableHeaderKeys['8']]:
                temp = data[n][constants.runwayTableHeaderKeys['8']]
                temp = extract.removeSpanishCharacters(temp)
                data[n][constants.runwayTableHeaderKeys['8']] = temp

            if data[n][constants.runwayTableHeaderKeys['9']]:
                temp = data[n][constants.runwayTableHeaderKeys['9']]
                temp = extract.removeExtraData(temp)
                data[n][constants.runwayTableHeaderKeys['9']] = temp

            if data[n][constants.runwayTableHeaderKeys['10']]:
                temp = data[n][constants.runwayTableHeaderKeys['10']]
                temp = extract.replaceNewline(temp, " ")
                temp = extract.removeExtraData(temp)
                data[n][constants.runwayTableHeaderKeys['10']] = temp
        return data
