# Empty DAYS dictionary to store the hours and minutes worked each day
DAYS = {}

# Constants for hours/mins/overtime.
TOTALHOURS = 0
TOTALMINUTES = 0
fOVER_TIME_HOURS = 40.0
fHalfTimeHours = 0.0

print ("Weekly Hour and pay Calculator\n")
print ("Enter times in HH:MM format only!\n")

# Loop through each day of the week asking for HH:MM

for DAY in ['Monday   ', 'Tuesday  ', 'Wednesday', 'Thursday ', 'Friday   ', 'Saturday ', 'Sunday   ']:
    
    # Ask the user for input for hours and minutes worked for the current day
    sTime = input(f"Enter the hours and minutes worked on {DAY}: ")
    
    # Split the input by colon ':' to separate hours and minutes
    sHours, sMinutes = sTime.split(':')
    
    # Convert the hours and minutes to integers
    iHours = int(sHours)
    iMinutes = int(sMinutes)
    
    # Store the hours and minutes worked for the current day in the dictionary
    DAYS[DAY] = {'hours': iHours, 'minutes': iMinutes}
    
    # Update total hours and minutes
    TOTALHOURS += iHours
    TOTALMINUTES += iMinutes

#Ask for rate
fPayRate = float(input("Enter your hourly rate: "))

#Break down left over minutes into hours and mins.

TOTALHOURS += TOTALMINUTES // 60
TOTALMINUTES %= 60

#convert into decimals and add together.

fDecimalMin = TOTALMINUTES / 60

fTotalTime = TOTALHOURS + fDecimalMin
fTotalDisplay = fTotalTime

# 2. Determine Over Time and Double Time:

if fTotalTime > fOVER_TIME_HOURS:
    fHalfTimeHours = fTotalTime - fOVER_TIME_HOURS
    fTotalTime -= fHalfTimeHours
  

# 3. Calculate pay:
fRegularPay    = fTotalTime * fPayRate
fHalfTimePay   = fHalfTimeHours * (fPayRate * 1.5)
fTotalPay = fRegularPay + fHalfTimePay 

# 4. Output:
print(f"\nYou worked {fTotalDisplay:.1f} hours this week.")
print(f"{fHalfTimeHours:.1f} of those were overtime hours.")
print(f"\nRegular Pay is       : ${fRegularPay:,.2f}")
print(f"Time and Half Pay is : ${fHalfTimePay:,.2f}")
print(f"Total gross Pay is   : ${fTotalPay:,.2f}")

input("\nEnter any key to quit.")
