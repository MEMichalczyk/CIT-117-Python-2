#SQL Database Interaction with Python GUI.
#By: Michael Michalczyk
#Date: 5/10/2025

import sqlite3
import csv
import tkinter
import tkinter.font

#GUI for output of data using the message widget.
class MyGUI:
    def __init__(self, report):
        self.main_window = tkinter.Tk()
        self.main_window.title("Retirement Report")
        
        #Set my font.
        myfont = tkinter.font.Font(family='Courier', size=10)
        
        # Create StringVar and assign the report
        self.text = tkinter.StringVar()
        self.text.set(report)
        
        # Use Message widget for multi-line text.
        self.message_widget = tkinter.Message(self.main_window,
                                              textvariable=self.text,
                                              width=600,
                                              font=myfont)
        self.message_widget.pack(padx=10, pady=10)
        
        # Quit button.
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Close',
                                          command=self.main_window.destroy)
        self.quit_button.pack(pady=(0, 10))
        
        # Start the mainloop.
        self.main_window.mainloop()
        
### FUNCTIONS ###
        
#createTable creates a table if it doesn't exist and clears any existing data from it.
#*definitions collects column definitions into a tuple.
#Existing data is deleted to prevent duplicates when the program is run multiple times.
def createTable(dbCursor, table_name, *definitions):
    dbCursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join(definitions)})")
    dbCursor.execute(f"DELETE FROM {table_name}")
    
#insertData is used to add data from a file to a created table.
#*columns collects column names into a tuple.
#Column names are joined with commas to form the SQL INSERT statement.
def insertData(filename, table_name, dbCursor, *columns):
    with open(filename, "r") as file:
        #Read the file.
        reader = csv.reader(file)
        #Skip header row.
        next(reader)
        
        #For each row in the CSV - Process the Values and execute the INSERT statement.
        for row in reader:
            #Store processed values for SQL.
            values_list = []
            for value in row:
                #Check if value is a number. Add it to the list.
                if value.replace('.', '', 1).isdigit():
                    values_list.append(value) 
                #Treat non-numeric values as strings and add quotes around them.
                else:
                    values_list.append(f"'{value}'")
            #Dynamic SQL INSERT statement. Column names and values (from values_list) joined with commas.
            insert = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES({', '.join(values_list)})"
            #Execute.
            dbCursor.execute(insert)
            
def main():
    
    #CONSTANTS
    PRINTLINE = "|-------------------------------------------------------------------|"
    
    #Part 1: Data creation, import and insertion.
    
    #Connect to SQLite database.
    dbConnection = sqlite3.connect("EmployeeSalary.db")
    #Create cursor object.
    dbCursor = dbConnection.cursor()
    
    #Create the tables.
    createTable(dbCursor, "Employee", "EmployeeID int", "Name text")
    createTable(dbCursor, "Pay", "EmployeeID int", "Year int", "Earnings real")
    createTable(dbCursor, "SocialSecurityMin", "Year int", "Minimum real")
    
    #Insert from Employee.
    insertData("Employee.txt", "Employee", dbCursor, "EmployeeID", "Name")
    #Insert from Pay.
    insertData("Pay.txt", "Pay", dbCursor, "EmployeeID", "Year", "Earnings")
    #Insert from SocialSecurityMinimum.
    insertData("SocialSecurityMinimum.txt", "SocialSecurityMin", dbCursor, "Year", "Minimum")
    #Commit inserts.
    dbConnection.commit()
    
    #Part 2: Data Reporting.
    
    #Select statement grabbing name, year, earnings, minimum.
    sSQLSelect = """SELECT e.Name, p.Year, p.Earnings, s.Minimum
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
ORDER BY e.Name"""
    
    #Use cursor to get data from the database.
    dbCursor.execute(sSQLSelect)
    
    #Report Start.
    report = []
    report.append(PRINTLINE)
    report.append(f"|{'Retirement Eligibility Based on Earnings':^67}|")
    report.append(PRINTLINE)
    report.append(f"| {'Name':^18} | {'Year':^4} | {'Earnings':^12} | {'Minimums':^12} | {'Qualify'} |")
    report.append(PRINTLINE)
    
    lastEmployee = ""
    sQualify = ""
    
    for row in dbCursor.fetchall():
        #Check if Earnings were >= the Minimum.
        if row[2] >= row[3]:
            sQualify = "Yes"
        else:
            sQualify = " No"
            
        #Separate each employee with a line.    
        currentEmployee = row[0]
        if currentEmployee != lastEmployee:
            if lastEmployee != "":
                report.append(PRINTLINE)

                
            lastEmployee = currentEmployee
            
        #Print row with Name, Year, Earnings, Minimum and the result Yes/No if that year qualified towards retirement.
        report.append(f"| {row[0]:<18} | {row[1]:^4} | {f'${row[2]:,.2f}':>12} | {f'${row[3]:,.2f}':>12} | {sQualify:^7} |")
        
    #Bottom Line of report.
    report.append(PRINTLINE)
    
    #Create and instance of the MyGUI. Add \n because the output went weird without it.
    my_gui = MyGUI("\n".join(report))
    
main()

