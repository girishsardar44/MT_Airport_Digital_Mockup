# %% all imports
import re
from math import copysign
# %%
# Converts Degrees Minutes and Seconds to Longitude and Latitude.
def convertDmsToDd(a):
    dd, alphabets = splitNumbersAndCharacters(a)
    dd= str(dd)
    deg = dd[0:2]
    min = dd[2:4]
    sec = dd[4:]
    if(alphabets == "N") or (alphabets == "S"):
        latitude = int(deg) + float(min)/60 + float(sec)/3600
        return (latitude) if alphabets == "N" else (copysign(latitude, -1))
    if(alphabets == "E") or (alphabets == "W"):
        longitude  = int(deg) + float(min)/60 + float(sec)/3600
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
# dms co-ordinates of Coruna Aerodrome.
a = "431730.11N"
b = "082308.74W"
# c = "431807N"
# d = "082238W"
e = "431830.91N"
f = "082218.84W"
print(convertDmsToDd(a),convertDmsToDd(b))
print(convertDmsToDd(e),convertDmsToDd(f))
# print(convertDmsToDd(c),convertDmsToDd(d))
