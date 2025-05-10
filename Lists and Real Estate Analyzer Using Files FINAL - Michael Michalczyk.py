#Real Estate Analyzer Using Lists and Files.
#By: Michael Michalczyk
#Date: 3/21/2025

#Import the csv
import csv

def main():

    #Add path for data file being used.
    path = "RealEstateData.csv"

    #Call getDataInput to get data.
    formData = getDataInput(path)

    #Price List
    price_list = []

    #City, Zip & Property Type Dictionaries.
    city_dict = {}
    zip_dict = {}
    proptype_dict = {}
    
    #Loop that reading each record from the formData List (Created from getDataInput).
    for column in formData:
        sCity = str(column[1].title())
        sZipcode = str(column[2])
        sPropType = str(column[7])
        fPrice = float(column[8])

        #Append to price list.
        price_list.append(fPrice)

        #Summary for Cities and price total.
        if sCity in city_dict:
            city_dict[sCity] += fPrice
        else:
            city_dict[sCity] = fPrice

        #Summary for Zip Codes and price total.
        if sZipcode in zip_dict:
            zip_dict[sZipcode] += fPrice
        else:
            zip_dict[sZipcode] = fPrice
            
        #Summary for Property Types and price total.
        if sPropType in proptype_dict:
            proptype_dict[sPropType] += fPrice
        else:
            proptype_dict[sPropType] = fPrice

    #Sort the price list.
    price_list.sort()

    #Get median using getMedian function.
    fMedian = getMedian(price_list)

    #Output Min/Max/Median/Total/AVG using Price List & fMedian.
    print (f"""\n-----------------------------------
|{f'Breakdown':^33}|
-----------------------------------""")
    print (getTotalOutput(price_list,fMedian))

    #Output by Type using Property Type Dictionary.
    print (f"""\n-----------------------------------
|{f'Summary By Property Type':^33}|
-----------------------------------""")
    getSpecificOutput(proptype_dict)
    
    #Output by City using City Dictionary.
    print (f"""\n-----------------------------------
|{f'Summary By City':^33}|
-----------------------------------""")
    getSpecificOutput(city_dict)

    #Output by Zip using Zip Dictionary.
    print (f"""\n-----------------------------------
|{f'Summary By Zip Code':^33}|
-----------------------------------""")
    getSpecificOutput(zip_dict)


### MYFUNCTIONS ###

#Create Function getDataInput (Skip header).
def getDataInput(path):
    data = []
    
    with open(path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    
    return data 

#Create Function getMedian.
def getMedian(data):
    data.sort()

    iLength = len(data)

    if (iLength) % 2 == 1:
        fMedian = data[iLength // 2]
    else:
        fMedian = ((data[(iLength) // 2]) + (data[(iLength) // 2 - 1])) / 2

    return fMedian

#Function for output of Min, Max, Total, Avg, Median.
def getTotalOutput (listIn, fMedianIn):
    sDisplay = f"""|Minimum         : {f'${min(listIn):,.2f}':>15}|
|Maximum         : {f'${max(listIn):,.2f}':>15}|
|Sum             : {f'${sum(listIn):,.2f}':>15}|
|Average         : {f'${sum(listIn)/len(listIn):,.2f}':>15}|
|Median          : {f'${fMedianIn:,.2f}':>15}|
-----------------------------------"""

    return sDisplay

#Function for output for different types from dictionaries.
def getSpecificOutput(dictIn):
    for x, total in dictIn.items():
        print (f"|{x:<16}: {f'${total:,.2f}':>15}|")
    print ("-----------------------------------")

main()
