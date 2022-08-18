from fileSystem import LoadFiles
import camelot

#%%
def executeCamelot(airportName, pdfName, pageNumber, tableNumber):

    fileName = pdfName.split('.pdf')[0]
    inputFiles = LoadFiles()
    basePath = inputFiles.getBasePath()
    inputFilesPath = basePath+'data/'+airportName+'/inputData/'
    jsonPath = basePath+'data/'+airportName+'/json/'
    inputFiles.createDirectoryIfNotExists(jsonPath)
    allTables = []
    if len(pageNumber) == 1:
        pdfTables = camelot.read_pdf(inputFilesPath+pdfName, pageNumber[0])
        pdfTables[int(tableNumber[0])].to_json(jsonPath+fileName+pageNumber[0]+'.json')
    else:
        for n in range(len(pageNumber)):
            allTables.append(camelot.read_pdf(
                inputFilesPath+pdfName, pageNumber[n]))
            allTables[n][int(tableNumber[n])].to_json(jsonPath+fileName+pageNumber[n]+'.json')

#%%
