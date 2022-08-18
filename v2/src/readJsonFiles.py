import fileSystem
fs = fileSystem.LoadFiles()


def getRunwayJsonFiles(airportDetails, airportFiles):
    airport = airportDetails['airportName']
    if len(airportDetails['runwaysTablePageNumber']) == 1:
        runwayFileName = fs.removeFileExtension(
            airportFiles['runways'], '.pdf')
        runwayFileName = runwayFileName + \
            airportDetails['runwaysTablePageNumber'][0]
        json = fs.readJson(airport, runwayFileName)
        return json
    else:
        runwaysFileNames = []
        jsonData = []
        for n in range(len(airportDetails['runwaysTablePageNumber'])):
            fileName = fs.removeFileExtension(airportFiles['runways'], '.pdf')
            runwaysFileNames.append(
                fileName+airportDetails['runwaysTablePageNumber'][n])
            jsonData.append(fs.readJson(airport, runwaysFileNames[n]))
        return jsonData


def getTerminalStandsFiles(airportDetails, airportFiles):
    airport = airportDetails['airportName']
    if (len(airportDetails['terminalStandsTablePageNumber']) == 1):
        terminalStandsFileName = fs.removeFileExtension(
            airportFiles['terminalStands'], '.pdf')
        terminalStandsFileName = terminalStandsFileName + \
            airportDetails['terminalStandsTablePageNumber'][0]
        json = fs.readJson(airport, terminalStandsFileName)
        return json
    else:
        terminalStandsFilesNames = []
        jsonData = []
        for n in range(len(airportDetails['terminalStandsTablePageNumber'])):
            terminalStandsFileName = fs.removeFileExtension(
                airportFiles['terminalStands'], '.pdf')
            terminalStandsFilesNames.append(
                terminalStandsFileName+airportDetails['terminalStandsTablePageNumber'][n])
            jsonData.append(fs.readJson(airport, terminalStandsFilesNames[n]))
        return jsonData
