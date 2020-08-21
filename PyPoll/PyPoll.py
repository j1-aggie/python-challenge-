# pypoll
# import the os module
import os

# module for reading csv file
import csv

# set the path for the data file
PyPollcsv = os.path.join('.', 'Resources', 'election_data')

# Set Variables
Total_Votes = 0
candidates = {}
candidates_percent_vote = {}
votes_won = 0
winner_name = ""


# open and read the csv
with open(PyPollcsv, newline='') as csvfile:
    # reader specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # read header row first
    csv_header = next(csvreader)
    row = next(csv reader)

    

    Total_Votes += 1


