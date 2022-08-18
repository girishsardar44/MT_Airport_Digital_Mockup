from executeCamelot import executeCamelot
from askUserInputs import AskUserInput
import fileSystem as fs
import joinJsonFiles
import convertToGeoJson as cgj


#%%  Raw inputs
userInputs = AskUserInput()
airportDetails = userInputs.askUserAirportDetails()
airportDetails = userInputs.askUserRunwayDetails(airportDetails)
airportDetails = userInputs.askUserTerminalStandDetails(airportDetails)
#%% Files & Paths
files = fs.LoadFiles()
basePath = files.getBasePath()
airportFiles = files.listInputFiles(airportDetails['airportName'])
airportFiles = files.findAllInputFiles(airportFiles)

#%% Runways
executeCamelot(airportDetails['airportName'], airportFiles['runways'],airportDetails['runwaysTablePageNumber'], airportDetails['runwaysTableNumber'])
airport = airportDetails['airportName']
runwayFileName = files.removeFileExtension(airportFiles['runways'], '.pdf')
allRunways = joinJsonFiles.joinRunwayJsonFiles(airportDetails, airportFiles)
runwaysGeoJson = cgj.convertRunwaysToGeoJson(allRunways)
#%% Terminals
executeCamelot(airport, airportFiles['terminalStands'], airportDetails['terminalStandsTablePageNumber'],airportDetails['terminalStandsTableNumber'])
terminalStandsFileName = files.removeFileExtension(airportFiles['terminalStands'], '.pdf')
allTerminalStands = joinJsonFiles.joinTerminalJsonFiles(airportDetails, airportFiles)
terminalStandsGeoJson = cgj.convertTerminalStandsJsonToGeojson(allTerminalStands)

#%% Obstacles
obstaclesFilesName = files.removeFileExtension(airportFiles['obstacles'],'.csv')
files.csvToJson(airportDetails['airportName'], obstaclesFilesName)
obstaclesJsonData = files.readJson(airportDetails['airportName'], obstaclesFilesName)
obstaclesGeoJson = cgj.convertObstaclesJsonToGeoJson(obstaclesJsonData)

#%% Write GeoJson Files

