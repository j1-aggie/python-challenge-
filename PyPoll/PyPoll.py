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

    # read each row of data 
    for row in csvreader:

        # find total votes

        Total_Votes += 1

        # find the list of candidates
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[rows[2]] = 1

        # defining the candidates dict
        for key, value in candidates.items():
            candidates_percent[key]=round((value/Total_Votes)*100,1)
        # finding the winner using dict
        for key in candidates.keys():
            if candidates[key] > votes_won:
                winner = key
                votes_won = candidates[key]

# print outs

print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(Total_Votes))
print("------------------------------------------------")
print(key + )


