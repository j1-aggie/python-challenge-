# pybank
# import the os module
import os

# module for reading csv file
import csv

# set the path for the data file
PyBankcsv = os.path.join('.' , 'Resources' , 'Budget_Data.csv')

# Set Variables
Total_Months = 0
Net_Profit = 0
Greatest_Increase_Profits = 0
Greatest_Decrease_Losses = 0
Month_changes = []
Avg_Changes = []
CountofMonths = []


# open and read the csv
with open(PyBankcsv, newline='') as csvfile:
    # reader specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # read header row first
    csv_header = next(csvreader)
    row = next(csvreader)


# calculate total number of months
previous_row = int(row[1])
total_months += 1

    for row in CSVreader:
        count = count + 1
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

    
# Set variable for output file
output_file = os.path.join("Final_Analysis.txt")
