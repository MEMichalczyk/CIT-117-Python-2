#Real Estate Analyzer Using Lists and Files.
#By: Michael Michalczyk
#Date: 3/21/2025

import csv



###FUNCTIONS###

#Create Function getDataInput (Skip header).
def getDataInput():
    data = []
    
    with open('RealEstateData.csv', mode='r') as file:
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

def main():

    #Add path for data file being used.
    path = "RealEstateData.csv"

    #Call getDataInput to get data.
    formData = getDataInput()

    #Lists
    price_list = []

    #Dictionaries.
    city_dict = {}
    zip_dict = {}
    proptype_dict = {}
    
    #Code a loop that reads each record from list.
    for column in formData:
        city = str(column[1])
        proptype = str(column[7])
        price = float(column[8])
        zipcode = str(column[2])

        price_list.append(price)

        #Summary for Cities and price total.
        if city in city_dict:
            city_dict[city] += price
        else:
            city_dict[city] = price

        #Summary for Zip Codes and price total.
        if zipcode in zip_dict:
            zip_dict[zipcode] += price
        else:
            zip_dict[zipcode] = price
            
        #Summary for Property Types and price total.
        if proptype in proptype_dict:
            proptype_dict[proptype] += price
        else:
            proptype_dict[proptype] = price

    #Sort the price list.
    price_list.sort()

    #Get median using getMedian function.
    fMedian = getMedian(price_list)

    #Output Min/Max/Median/Total/AVG.
    print (f"""\n-----------------------------------
|{f'Breakdown':^33}|
-----------------------------------""")
    print (getTotalOutput(price_list,fMedian))

    #Output by Type.
    print (f"""\n-----------------------------------
|{f'Summary By Property Type':^33}|
-----------------------------------""")
    getSpecificOutput(proptype_dict)
    
    #Output by City.
    print (f"""\n-----------------------------------
|{f'Summary By City':^33}|
-----------------------------------""")
    getSpecificOutput(city_dict)

    #Output by Zip.
    print (f"""\n-----------------------------------
|{f'Summary By Zip Code':^33}|
-----------------------------------""")
    getSpecificOutput(zip_dict)

main()
