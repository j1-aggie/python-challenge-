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
    row = next(csvreader)

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
# print out to python
print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(Total_Votes))
print("------------------------------------------------")
print(key + ":" "+ str(candidates_percent_vote[key])
print

# path to write txt file to 
output_file = os.path.join(',', 'Analysis', 'Final_Analysis_PyPoll.txt')

with open(output_file, 'w',) as txtfile:

# write to txt file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {Total_Votes}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.%}({khan_votes}")\n")
    txtfile.write(f"Correy: {correy_percent:.%} ({correy_votes}\n")
    txtfile.write(f"Li: {li_percent:.%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.%}({otooley_votes})\n")
    txtfile.write(f"--------------------------\n")