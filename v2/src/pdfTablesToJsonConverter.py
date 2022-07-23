from curses import raw
import camelot
import os
import dmsToddConverter
import json
#%%  Raw inputs
pdfName = input('Enter PDF Name: ')
tablePageNumber = input('Enter the Runways table page Number: ')
tableNumber = input('Enter table number in the page : ')
#%%
currentDirectory = os.path.abspath(__file__)
basePath = currentDirectory.split('src')[0]
pdfDirectory = basePath+'data/pdfs/'
jsonDirectory = basePath+'data/json/'
jsonPath = jsonDirectory+pdfName+'.json'
pdfPath = pdfDirectory+pdfName+'.pdf'
#%%
runwayDetailsTable = camelot.read_pdf(pdfPath, pages=tablePageNumber)
runwayDetailsTable[int(tableNumber)].to_json(jsonPath)
#%%
with open(jsonPath) as f:
    runwayDetailsJson = json.load(f)
print(len(runwayDetailsJson))
