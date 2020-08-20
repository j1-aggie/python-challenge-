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
Greatest_Month_Increase = 0
Greatest_Month_Decrease = 0
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

# Setting variables for rows
    Greatest_Increase_Profits = int(row[1])
    Greatest_Month_Increase = row[0]
    

# read each row
    for row in csvreader:

        Total_Months += 1
        Net_Profit += int(row[1])

        # change from month to month
        revenue_change = int(row[1]) - previous_row
        Monthly_changes.append(revenue_change)
        previous_row = int(row[1])
        CountofMonths.append(row[0])

        # greatest increase
        if int(row[1]) > Greatest_Increase_Profits:
            Greatest_Increase_Profits = int(row[1])
            Greatest_Month_Increase = row[0]


        # greatest decrease
        if int(row[1]) < Greatest_Decrease_Losses:
            Greatest_Decrease_Losses = int(row[1])
            Greatest_Month_Decrease = row[0]

    

# average change with date
average_change = sum(Monthly_changes)/len(Monthly_changes)

highest = max(Monthly_changes)
lowest = min(Monthly_changes)

# output
    
# print out
print(f"Financial Analysis")
print(f"-----------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {Greatest_Month_Increase},(${highest})")
print(f"Greatest Decrease in Profits:, {Greatest_Month_Decrease}, (${lowest})")


#file to write to   
output_file = os.path.join('.', 'Analysis', 'Final_Analysis_PyBank.txt')

with open(output_file, 'w',) as txtfile:

# write new data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------------------\n")
    txtfile.write(f"Total Months: ${Total_Months}\n")
    txtfile.write(f"Total: ${Net_Profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {Greatest_Month_Increase}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {Greatest_Month_Decrease}, (${lowest})\n")