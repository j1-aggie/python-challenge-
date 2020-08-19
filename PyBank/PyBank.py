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
Monthly_changes = []
Greatest_Month_Increase = []
Greatest_Decrease_Month = []
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
Total_Months += 1

# Amount of Profit/Losses - Net
Net_Profit += int(row[1])

# Greatest increase 
Greatest_Increase_Profits = int(row[1])

# Greatest increase monthly
Greatest_Month_Increase = row[0]

# read each row after header
    for row in csvreader:
    
        # number of months in data
        Total_Months += 1 
        

    
# Set variable for output 
output_file = os.path.join("Final_Analysis.txt")
