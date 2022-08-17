
class AskUserInput:

    def askUserAirportDetails(self):
        airport={}
        airport['airportName'] = input('Enter Airport Directory Name (Case Sensitive): ')
        return airport

    def askUserRunwayDetails(self,airportName):
        airportName['runwaysTablePageNumber'] = list(input('Enter the Runways table page Number/ Numbers use : '))
        airportName['runwaysTableNumber']= list(input('Enter table number / numbers in the corresponding Runways page : '))
        return airportName

    def askUserTerminalStandDetails(self,airport):
        airport['terminalStandsTablePageNumber'] = list(input('Enter the Terminals Stands table page Number/ Numbers use : '))
        airport['terminalStandsTableNumber'] = list(input('Enter table number/ numbers in the corresponding terminals Stand page : '))
        return airport

    

# au = AskUserInput()

# ad = au.askUserAirportDetails()
# ad = au.askUserRunwayDetails(ad)
# ad = au.askUserTerminalStandDetails(ad)

# print(((ad['terminalStandsTablePageNumber'][0])))