import constants
from extractInfoFromJson import extractUsableDataFromJson
from geojson import FeatureCollection
extract = extractUsableDataFromJson()


class TransformTerminalData:

    def getCoordinates(self, data):
        coordinates = {}
        for n in data.keys():
            coordinates[n] = data[n][constants.terminalStandsTableHeaderKeys['2']]
        return coordinates

    def combineTerminalStandsPointsAndProperties(self, features, properties):
        collection = []
        for n in features.keys():
            del properties[n][constants.terminalStandsTableHeaderKeys['2']]
            features[n]['properties'] = properties[n]
            collection.append(features[n])
        return FeatureCollection(collection)

    def changeTerminalStandsDataKeys(self, data):
        del data[0]
        newData = {}
        for n in range(len(data)):
            newData[n] = dict(
                zip(constants.terminalStandsTableHeaderKeys.values(), data[n].values()))
        return newData

    def removeTerminalStandsInvalidData(self, data):
        listToDelete = []
        for n in range(len(data)):
            if not 'E' in (data[n]['Coordinates']):
                listToDelete.append(int(n))
            if 'STAND' in (data[n]['Stand']):
                listToDelete.append(int(n))
        for n in range(len(listToDelete)):
            data.pop(listToDelete[n])
        return data

    def cleanTerminalStandsData(self, data):
        for n in data.keys():
            if data[n][constants.terminalStandsTableHeaderKeys['6']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['6']]
                temp = extract.replaceNewline(temp, " ")
                data[n][constants.terminalStandsTableHeaderKeys['6']] = temp

            if data[n][constants.terminalStandsTableHeaderKeys['3']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['3']]
                temp = extract.removeExtraData(temp)
                data[n][constants.terminalStandsTableHeaderKeys['3']] = temp

            if data[n][constants.terminalStandsTableHeaderKeys['2']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['2']]
                temp = extract.removeUniCode(temp)
                temp = extract.replaceQuotes(temp, "")
                temp = extract.thresholdCoordinates(temp)
                data[n][constants.terminalStandsTableHeaderKeys['2']] = temp
        return data
