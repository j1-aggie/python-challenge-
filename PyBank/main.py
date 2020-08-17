# pybank
# import the os module
import os

# module for reading csv file
import csv

csvpath = os.path.join('..', 'Resources', 'BudgetData.csv')

with open(csvpath, 'r') as csvfile: