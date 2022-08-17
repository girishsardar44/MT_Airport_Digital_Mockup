from executeCamelot import executeCamelot
from askUserInputs import AskUserInput
import fileSystem as fs
import dmsToddConverter as dmstoDd
import constants
import joinJsonFiles
from coordinatesFromThreshold import findLongitudeLatitude2
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
#%%Camelot
executeCamelot(airportDetails['airportName'], airportFiles['runways'],airportDetails['runwaysTablePageNumber'], airportDetails['runwaysTableNumber'])

#%% Runway json
airport = airportDetails['airportName']
runwayFileName = files.removeFileExtension(airportFiles['runways'], '.pdf')
airportJson = airport+'json'

# json =  files.readJson(airportDetails['airportName'], runwayFileName)
# dummy = convertToGeoJson.convertToGeoJson(json)
# print(dummy)
 # Todo execute cleaning json and convert to geojson for runways
#%%
# page - 2, table - 0 
terminalStandsFileName = files.removeFileExtension(airportFiles['terminalStands'], '.pdf')
executeCamelot(airport, airportFiles['terminalStands'], airportDetails['terminalStandsTablePageNumber'],airportDetails['terminalStandsTableNumber'])
# 
# get json and separate usable data from 

#%%
obstaclesFilesName = files.removeFileExtension(airportFiles['obstacles'],'.csv')
print(obstaclesFilesName)
files.csvToJson(airportDetails['airportName'], obstaclesFilesName)
#%%%
allRunways = joinJsonFiles.joinRunwayJsonFiles(airportDetails, airportFiles)
allTerminalStands = joinJsonFiles.joinTerminalJsonFiles(airportDetails, airportFiles)

runwaysGeoJson = cgj.convertRunwaysToGeoJson(allRunways)
terminalStandsGeoJson = cgj.convertTerminalStandsJsonToGeojson(allTerminalStands)

# print(terminalStandsGeoJson)
print(runwaysGeoJson)
