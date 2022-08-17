import readJsonFiles


def joinRunwayJsonFiles(airportDetails, airportFiles):
    airport = airportDetails['airportName']
    if (len(airportDetails['runwaysTablePageNumber']) > 1):
        runwayFiles = readJsonFiles.getRunwayJsonFiles(airportDetails, airportFiles)
        for n in range(1,len(runwayFiles)):
            allRunways = runwayFiles[n-1].append(runwayFiles[n])
        return allRunways
    else: 
        return (readJsonFiles.getRunwayJsonFiles(airportDetails, airportFiles))

def joinTerminalJsonFiles(airportDetails, airportFiles):
    if (len(airportDetails['terminalStandsTablePageNumber']) > 1):
        terminalStandsFiles = readJsonFiles.getTerminalStandsFiles(airportDetails, airportFiles)
        for n in range(1,len(terminalStandsFiles)):
            allTerminalStands = terminalStandsFiles[n-1]+(terminalStandsFiles[n])
        return allTerminalStands
    else:
        return (readJsonFiles.getTerminalStandsFiles(airportDetails, airportFiles))

