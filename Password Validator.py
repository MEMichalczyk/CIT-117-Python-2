#Password Validator
#By: Michael Michalczyk
#2/21/2025

def main ():

    #Named constants.
    SPECIALCHARS = ['!', '@', '#', '$', '%', '^']
    PASSMIN = 8
    PASSMAX = 12
    PASSRESTRICT = "pass"
    RULES = (f"""
Password Rules:

1. Must contain {PASSMIN} - {PASSMAX} characters.
2. Must contain 1 digit.
3. Must contain 1 capital letter.
4. Must contain 1 lower case letter.
5. It can't contain your initials.
6. It must contain a special character: {' '.join(SPECIALCHARS)}.
7. It can't have repeating characters.
8. It can't have "{PASSRESTRICT}" in the password.""")

    #Welcome.
    print (f"""\n -------------------------------------
{f'|  Welcome to the Password Validator  |':^30}
 -------------------------------------""")
    
    #Loop asking for name.
    #Can take multiple names or just one. (Doesn't check one)
    sFullName = ""
    while len(sFullName) == 0:
        sFullName = input("\nEnter your name (H for Help): ")
        if sFullName.upper() == "H":
            sFullName = ""
            print (RULES)

    #Split names into list. Save 1 name entry in variable.
    sNames = [] 
    sNames = sFullName.split()

    #Save initials of the name entered.
    sInitials = ""
    
    for sNamePart in sNames:
        sInitials += sNamePart[0]

    #Start the loop and ask for a valid password.
    bPassValid = False
    
    while bPassValid != True:
        #Ask for new password.
        sPassword = input("\nEnter new password: ")

        #Password check variables. Checked at end.
        bLengthCheck = False
        bStartPassCheck = False
        bUpperCheck = False
        bLowerCheck = False
        bNumCheck = False
        bSpecialCheck = False
        bInitialsCheck = False
        bNameCheck = False
        bDuplicates = False

        #Check length of password.
        iPassLength = len(sPassword)
        
        if iPassLength < PASSMIN or iPassLength > PASSMAX:
            bLengthCheck = False
        else:
            bLengthCheck = True

        #Check if starts with pass/Pass.
        #Isolate first 4 to check for "pass".
        sStartPass = sPassword[0:4]
        
        if sStartPass.lower() == PASSRESTRICT:
            bStartPassCheck = False
        else:
            bStartPassCheck = True

        #Check for multiple chars used.
        sUsedChars = []
        iCountDupe = []
        
        for chars in sPassword:
            #Convert characters to lower case.
            sLowerChars = chars.lower()

            #Track unique character counts.
            #Check characters in used, if not add it and update with count of 1.
            if sLowerChars not in sUsedChars:
                sUsedChars.append(sLowerChars)
                iCountDupe.append(1)
            else:
                #Find the index and increase the count of dupes found.
                iIndex = sUsedChars.index(sLowerChars)
                iCountDupe[iIndex] += 1
                bDuplicates = True

            #Check if upper case.
            if chars.isupper():
                bUpperCheck = True

            #Check if lower case.    
            if chars.islower():
                bLowerCheck = True

            #Check if it has numbers    
            if chars.isnumeric():
                bNumCheck = True

            #Check if special characters exist !@#$%^.    
            if chars in SPECIALCHARS:
                bSpecialCheck = True

            #Check for length of initials.
            if len(sInitials) < 2:
                bInitialsCheck = False
            else:
                if sInitials.lower() in sPassword.lower():
                    bInitialsCheck = True
              
        #Output to screen if invalid check. Checking True/False.
        if not bLengthCheck:
            print (f"Password must be between {PASSMIN} and {PASSMAX} characters.")
            
        if not bStartPassCheck:
            print (f"Password can’t start with {PASSRESTRICT.capitalize()}.")

        if not bUpperCheck:
            print ("Password must contain at least 1 uppercase letter.")
        
        if not bLowerCheck:
            print ("Password must contain at least 1 lowercase letter.")     

        if not bNumCheck:
            print ("Password must contain at least 1 number.") 

        if not bSpecialCheck:
            print (f"Password must contain at least 1 of these special characters: {' '.join(SPECIALCHARS)}.")

        if bInitialsCheck:
            print (f"Password must not contain the users initials: {sInitials.upper()}")

        if bDuplicates:
            print (f"""These characters appear more than once:
-------------""")
            #Get the amount of times the loop needs to run.
            #Find the index for sUsedChars to get location of characters.
            #(Thank god for the palindrome example!)
            for iIndex in range(len(sUsedChars)):
                #Check the characters at the index of iCountDupe.
                #Print to screen if greater than 1.
                if iCountDupe[iIndex] > 1:
                    print (f"{f'|{sUsedChars[iIndex].upper()}':<2}: {f'{iCountDupe[iIndex]}':>2} {f'Times|':<7}")
            print ("-------------")
            
        #Check for True/False and output successful password.
        #These MUST be True to pass.
        if (bLengthCheck
            and bStartPassCheck
            and bUpperCheck
            and bLowerCheck
            and bNumCheck
            and bSpecialCheck

        #These MUST be False to pass.
            and not bInitialsCheck
            and not bDuplicates):

        #Make bPassValid True to break the loop and output success.
            bPassValid = True
            print (f"\nThe password {sPassword} is valid and OK to use!")

main()
