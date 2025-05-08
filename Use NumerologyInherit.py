#Use Numerology Inherit
#By: Michael Michalczyk
#Date: 4/24/2025

#Import NumerologyNumerologyLifePathDetails Class.
from NumerologyLifePathDetails import NumerologyLifePathDetails

def main ():

    #Get the name of the client.
    sName = ""
    while len(sName) == 0:
        sName = input("Enter your name: ")

    #Get the DOB of the client.
    sDOB = ""
    while True:
        sDOB = input("Enter your DOB (mm-dd-yyyy): ")

        #Check if the DOB has - or / in it and that it is 10 characters long.
        if ('-' in sDOB or '/' in sDOB) and len(sDOB) == 10:
            break

        #If not, explain format needed for DOB.
        else:
            print("DOB must be mm-dd-yyyy or mm/dd/yyyy")

    #Create a numerology object with the client's name and DOB.
    numerology = NumerologyLifePathDetails(sName, sDOB)

    #Print out the data from numerology.
    print(numerology)
    
main()
