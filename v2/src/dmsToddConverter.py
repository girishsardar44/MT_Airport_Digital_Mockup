# %% all imports
import re
from math import copysign
# %%
# Converts Degrees Minutes and Seconds to Longitude and Latitude (aka: Decimal Degrees).
def convertDmsToDd(a):
    dd, alphabets = splitNumbersAndCharacters(a)
    dd = str(dd)
    deg = dd[0:2]
    mins = dd[2:4]
    secs = dd[4:]
    if(alphabets == "N") or (alphabets == "S"):
        latitude = int(deg) + float(mins)/60 + float(secs)/3600
        return (latitude) if alphabets == "N" else (copysign(latitude, -1))
    if(alphabets == "E") or (alphabets == "W"):
        longitude  = int(deg) + float(mins)/60 + float(secs)/3600
        return (longitude) if alphabets == "E" else (copysign(longitude, -1))
# %% Separates Numbers and characters from the Geo Points. 
def splitNumbersAndCharacters(dd):
    num = (re.split('(\D)',dd)[0:3])
    if num[1] == '.':
       numbers = num[0] + num[1] + num[2]
    else :
        numbers = num[0]
    characters = re.split('(\d)', dd)[-1]
    return numbers, characters
#%%
def validateCoordinates(coordinates):
    identifiers = ['latitude','longitude']
    for selector in identifiers:
        coordinates[selector] = removeWhiteSpace(coordinates[selector])
        numbers = coordinates[selector].split('.')
        length = len(numbers[0])
        if length > 6 :
            newCoordinate = numbers[0][1:]
            coordinates[selector] = newCoordinate+'.'+numbers[1]
    return coordinates
#%% 
def removeWhiteSpace(string):
    if ' ' in str(string):
        dum = string.replace(' ', "")
        return dum
    else:
        return string
