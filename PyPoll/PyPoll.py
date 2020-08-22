# pypoll
# import the os module
import os

# module for reading csv file
import csv

# set the path for the data file
PyPollcsv = os.path.join('.', 'Resources', 'election_data.csv')

# Set Variables
Total_Votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# open and read the csv
with open(PyPollcsv, newline='') as csvfile:
    # reader specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    # read header row first
    csv_header = next(csvfile)
    
    # read each row of data 
    for row in csvreader:

        # find total votes

        Total_Votes += 1

        # number of votes for each candidate
        if (row[2] == "Khan"):
            khan_votes +=1
        elif (row[2] =="Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    # percentage of votes for each candidate
    kahn_percent = khan_votes / Total_Votes
    correy_votes = correy_votes / Total_Votes
    li_votes = li_votes / Total_Votes
    otooley_votes = otooley_votes / Total_Votes

    # calculate winner of election
    winner_name = max(khan_votes, correy_votes, li_votes, otooley_votes)


    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

# print outs
# print out to python
print(f"Election Results")
print(f"------------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------------------------")
print(f"Kahn: {kahn_percent:.%}({khan_votes})")
print(f"Correy: {correy_percent:.%}({correy_votes})")
print(f"Li: {li_percent:.%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.%}({otooley_votes})")
print(f"-----------------------------------------------")
print(f"Winner: {winner_name}")
print(f"-----------------------------------------------")

# path to write txt file to 
output_file = os.path.join(',', 'Analysis', 'Final_Analysis_PyPoll.txt')

with open(output_file, 'w',) as txtfile:

# write to txt file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: ${Total_Votes}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.%}({otooley_votes})\n")
    txtfile.write(f"--------------------------\n")