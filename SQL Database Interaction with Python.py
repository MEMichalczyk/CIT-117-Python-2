#SQL Database Interaction with Python
#By: Michael Michalczyk
#Date: 5/10/2025

import sqlite3
import csv

### FUNCTIONS ###

#createTable creates a table if it doesn't exist and clears any existing data from it.
#*definitions collects column definitions (e.g., "Name text", "ID int") as arguments.
def createTable(dbCursor, table_name, *definitions):
    #Dynamic SQL CREATE query using .join method to make definitions into a single string.
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join(definitions)})")
    dbCursor.execute(f"DELETE FROM {table_name}")
    
#insertData is used to add data from a file to a created table.
#*columns collects column names (e.g., "ID", "Year", "Name") as arguments.
def insertData(dbCursor, filename, table_name, *columns):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        #Skip header row.
        next(reader)
        
        #For each row in the CSV - Process the Values and execute the INSERT statement.
        for row in reader:
            values_list = []
            for value in row:
                #Check if value is a number.
                if value.replace('.', '', 1).isdigit():
                    values_list.append(value) 
                #Treat non-numeric values as strings with quotes.
                else:
                    values_list.append(f"'{value}'")
                    
            #Dynamic SQL INSERT query using .join method to make the columns and values into a single string.
            insert = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES({', '.join(values_list)})"
            #Execute.
            dbCursor.execute(insert)
            
def main():
    
    #CONSTANTS
    PRINTLINE = "|-----------------------------------------------------------------------------|"
    
    ### Part 1: Data creation, import and insertion ###
    
    #Connect to SQLite database.
    dbConnection = sqlite3.connect("EmployeeSalary.db")
    #Create cursor object.
    dbCursor = dbConnection.cursor()
    
    #Create the tables.
    createTable(dbCursor, "Employee", "EmployeeID int", "Name text")
    createTable(dbCursor, "Pay", "EmployeeID int", "Year int", "Earnings real")
    createTable(dbCursor, "SocialSecurityMin", "Year int", "Minimum real")
    
    #Insert data into Employee, Pay, and SocialSecurityMin table.
    insertData(dbCursor, "Employee.txt", "Employee", "EmployeeID", "Name")
    insertData(dbCursor, "Pay.txt", "Pay", "EmployeeID", "Year", "Earnings")
    insertData(dbCursor, "SocialSecurityMinimum.txt", "SocialSecurityMin", "Year", "Minimum")
    
    #Commit inserts.
    dbConnection.commit()
    
    ### Part 2: Data Reporting ###
    
    #SQL Select statement joining together Employee, Pay, and SocialSecurityMin tables.
    #Retrieves Name, Year, Earnings, and Minimum.
    #Sorts the result by name.
    sSQLSelect = """SELECT e.Name, p.Year, p.Earnings, s.Minimum
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
ORDER BY e.Name"""
    
    #Execute the SQL SELECT statement using dbCursor.
    dbCursor.execute(sSQLSelect)
    
    #Report Header.
    print(PRINTLINE)
    print(f"|{'Retirement Eligibility Based on Earnings':^77}|")
    print(PRINTLINE)   
    print(f"| {'Employee Names':^20} | {'Year':^4} | {'Earnings':^16} | {'Minimums':^16} | {'Include'} |")
    print(PRINTLINE)
    
    lastEmployee = ""
    sQualify = ""
    
    #Check if Earnings were >= the Minimum for Include.
    for row in dbCursor.fetchall():     
        if row[2] >= row[3]:
            sQualify = "Yes"
        else:
            sQualify = "No"
        
        #Separate each employee with a line.
        currentEmployee = row[0]
        
        if currentEmployee != lastEmployee:
            if lastEmployee != "":
                print(PRINTLINE)
                
            lastEmployee = currentEmployee
            
        #Print row with Name, Year, Earnings, Minimum and the sQualify.
        #Text is left-aligned and numbers are right-aligned.
        print(f"| {row[0]:<20} | {row[1]} | {f'${row[2]:,.2f}':>16} | {f'${row[3]:,.2f}':>16} | {sQualify:<7} |")
    #Bottom Line of report.
    print(PRINTLINE)
    
main()
