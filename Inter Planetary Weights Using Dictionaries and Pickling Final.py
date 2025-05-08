#Inter Planetary Weights Using Dictionaries and Pickling
#By: Michael Michalczyk
#Date: 3/1/2025

#Import Pickle
import pickle

def main ():
    
    #Create a dictionary that has conversion factors for each planet.
    #Key = Planet Name, Value = gravity relative to earth.
    dictPlanets = {
        'Mercury':0.38,
        'Venus':0.91,
        'our Moon':0.165,
        'Mars':0.38,
        'Jupiter':2.34,
        'Saturn':0.93,
        'Uranus':0.92,
        'Neptune':1.12,
        'Pluto':0.066,
        }

    #Dictionary to store a persons weight history from mmPlanetaryWeights.
    dictPlanetHistory = {}

    #Attempt to open the pickling file that stored previous values.
    #Check "eof" reached.
    eof = False
    try:
        #Name has to be mmPlanetaryWeights.db
        input_file = open('mmPlanetaryWeights.db', 'rb')
        #Try/except if file exists or not
        while not eof:
            try:
                #Transfer content of .db into a dictionary called dictPlanetHistory.
                dictPlanetHistory = pickle.load(input_file)
            #If not move on.
            except EOFError:
                eof = True

        input_file.close()
            
    #If no file found - (first run) skip and continue.
    except FileNotFoundError:
        pass

    #Check if there is history to pull up.
    if dictPlanetHistory:
        #Prompt if user wants to see history y/n.
        sViewHist = input("Would you like to see the history Y/N: ").lower()
        if sViewHist != 'n':
            #Print out history.
            for name, weights in dictPlanetHistory.items():
                print (f"\nHere is {name}'s weights on our Solar System's planets:")
                print ("-------------------------------------")
                for planet, weight in weights.items():
                    print (f"| {'Weight on ' + planet + ':':19} {weight:10.2f} lbs|")
                print ("-------------------------------------")

                    
    #Loop with prompt for unique name not already in dictPlanetHistory.
    while True:
        sName = input(f"\nWhat is your name (enter key to quit): ").title()

        #Blank name exits loop.
        if sName == "":
            break
        
        if sName in dictPlanetHistory:
            print (f"{sName} is already in the history file. Enter a unique name.")
            continue
        
        #Prompt for valid number - try/except till valid (greater than 0).
        while True:
            try:
                fWeight = float(input("What is your weight: "))
                if fWeight >= 1:
                    break
                else:
                    print ("Enter a valid number.")
            except ValueError:
                print ("Enter a valid number.")

        #Declare another dictionary dictPersonWeights.
        dictPersonWeights = {}

        #Start of print out.
        print (f"\n{sName} here are your weights on our Solar System's planets:")
        print ("-------------------------------------")
        #Loop use surface gravity from dictPlanets to output weights.
        for planet, factor in dictPlanets.items():
            fPlanetWeight = factor * fWeight
            #Add Planet Name and Computed Weight to dictPersonWeights.
            dictPersonWeights[planet] = fPlanetWeight
            #Format the printing so that it is aligned correctly.
            print (f"| {'Weight on ' + planet + ':':19} {fPlanetWeight:10.2f} lbs|")
        print ("-------------------------------------")
        
        #Add the persons name and dictPersonWeights to the dictPlanetHistory.
        dictPlanetHistory[sName] = dictPersonWeights

        #Save updated dictPlanetHistory to pickled file.
        output_file = open('mmPlanetaryWeights.db', 'wb')
        pickle.dump(dictPlanetHistory, output_file)
        output_file.close()

main()
