#Numerology Class File
#By: Michael Michalczyk
#Date: 4/27/2025

class Numerology:

    # Constants.
    VOWELS = "AEIOU"

    def __init__(self, sName, sDOB):
        self.__sName = sName
        self.__sDOB = sDOB

        #Break the date into different variables to be used in life paths. Month/Day/Year
        self.__iMonth = int(self.__sDOB[0:2])
        self.__iDay = int(self.__sDOB[3:5])
        self.__iYear = int(self.__sDOB[6:10])

        #Temp Variables to hold the numbers for Vowels and Consonants.
        iVowels = 0
        iConsonants = 0

        # Process the name only once to calculate the vowels and the consonants.
        # Loop through each character in _sName.
        for char in self.__sName.upper().replace(" ", ""):
            if char.isalpha():
                if char in self.VOWELS:
                    iVowels += self.__convertCharToInt(char)
                else:
                    iConsonants += self.__convertCharToInt(char)

        #Six private variables for life paths.
        #All pass through new getSingleDigit to make sure no greater than 9.
        self.__iSoulNum = self.__getSingleDigit(iVowels)
        self.__iPersonalityNum = self.__getSingleDigit(iConsonants)
        self.__iLifePathNum = self.__getSingleDigit(self.__iMonth + self.__iDay + self.__iYear)
        self.__iAttitudeNum = self.__getSingleDigit(self.__iMonth + self.__iDay)
        self.__iBirthdayNum = self.__getSingleDigit(self.__iDay)
        self.__iPowerNameNum = self.__getSingleDigit(self.__iSoulNum + self.__iPersonalityNum)

    #New converting Char to Int! (based on Prof C. suggestions).
    def __convertCharToInt(self, char):
        #Check if character is alphabetical.
        if char.isalpha():
            
            #Convert to uppercase and get the ASCII of the character.
            #Subtract 65 to start from 0.
            #Use the modulus 9 to make sure numbers wrap back around to 1 after 9.
            #Add 1 to start at 1 (65 - 65 would = 0. A has a value of 1.)
            return ((ord(char.upper()) - 65) % 9 + 1)
        
        #If the character isnt alphabetical or a letter it returns 0.
        return 0

    #New reduce number to single digit (based on Prof C. suggestions).
    def __getSingleDigit(self, iNumber):
        #Keep looping while more than one digit.
        while iNumber >= 10:

            #(iNum % 10) gives you the last digit of the number.
            #(iNum // 10) removes the last digit and gives you the first one.
            #Then you add them together.
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber

    #Getters
    def getName(self):
        return self.__sName

    def getBirthDate(self):
        return self.__sDOB

    def getAttitude(self):
        return self.__iAttitudeNum

    def getBirthDay(self):
        return self.__iBirthdayNum

    def getLifePath(self):
        return self.__iLifePathNum

    def getSoul(self):
        return self.__iSoulNum

    def getPersonality(self):
        return self.__iPersonalityNum

    def getPowerName(self):
        return self.__iPowerNameNum

    #__str__ method for output!
    def __str__(self):
        return (f"""
{'Test Name:'} {self.getName().title()}
{'Test DOB:'} {self.getBirthDate().replace("-", "/")}
-------------------------------------
{'Life Path Number:'} {self.getLifePath():>5}
{'Birth Day Number:'} {self.getBirthDay():>5}
{'Attitude Day Number:'} {self.getAttitude():>2}
{'Soul Number:'} {self.getSoul():>10}
{'Personality Number:'} {self.getPersonality():>3}
{'Power Name Number:'} {self.getPowerName():>4}
-------------------------------------""")
