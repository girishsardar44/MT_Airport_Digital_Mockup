from constants import tableHeaderKeys
from extractInfoFromJson import extractUsableDataFromJson

extract = extractUsableDataFromJson()


def cleanData(data):
    for n in range(len(data)):
        if data[n][tableHeaderKeys['0']]:
            temp = data[n][tableHeaderKeys['0']]
            data[n][tableHeaderKeys['0']] = extract.removeExtraData(temp)

        if data[n][tableHeaderKeys['1']]:
            temp = data[n][tableHeaderKeys['1']]
            data[n][tableHeaderKeys['1']] = extract.direction(temp)

        if data[n][tableHeaderKeys['2']]:
            temp = data[n][tableHeaderKeys['2']]
            temp = extract.removeExtraData(temp)
            data[n][tableHeaderKeys['2']] = extract.dimensions(temp)

        if data[n][tableHeaderKeys['3']]:
            temp = data[n][tableHeaderKeys['3']]
            temp = extract.thresholdCoordinates(temp)
            data[n][tableHeaderKeys['3']] = temp

        if data[n][tableHeaderKeys['4']]:
            temp = data[n][tableHeaderKeys['4']]
            temp = extract.replaceNewline(temp, " ")

        if data[n][tableHeaderKeys['5']]:
            temp = data[n][tableHeaderKeys['5']]
            temp = extract.removeSpanishCharacters(temp)
            data[n][tableHeaderKeys['5']] = temp

        if data[n][tableHeaderKeys['6']]:
            temp = data[n][tableHeaderKeys['6']]
            temp = extract.removeExtraData(temp)
            data[n][tableHeaderKeys['6']] = extract.dimensions(temp)

        if data[n][tableHeaderKeys['7']]:
            temp = data[n][tableHeaderKeys['7']]
            temp = extract.removeExtraData(temp)
            data[n][tableHeaderKeys['7']] = extract.dimensions(temp)

        if data[n][tableHeaderKeys['8']]:
            temp = data[n][tableHeaderKeys['8']]
            temp = extract.removeSpanishCharacters(temp)
            data[n][tableHeaderKeys['8']] = temp

        if data[n][tableHeaderKeys['9']]:
            temp = data[n][tableHeaderKeys['9']]
            temp = extract.removeExtraData(temp)
            data[n][tableHeaderKeys['9']] = temp

        if data[n][tableHeaderKeys['10']]:
            temp = data[n][tableHeaderKeys['10']]
            temp = extract.replaceNewline(temp, " ")
            temp = extract.removeExtraData(temp)
            data[n][tableHeaderKeys['10']] = temp

    return data
