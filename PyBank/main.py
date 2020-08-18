# pybank
# import the os module
import os

# module for reading csv file
import csv

# Set Variables
Total_Months = 0
Net_Profit = 0
Greatest_Increase_Profits = 0
Greatest_Decrease-Losses = 0
Month_changes = []
Avg_Changes = []
Date = []



# set the path for the data file
PyBankcsv = os.path.join('Resources', 'Budget_Data.csv')

# reading the csv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in CSVreader:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

    
