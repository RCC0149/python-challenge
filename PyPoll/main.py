# Import Modules
import os
import csv

# Set Path For Resource File
csv_path = os.path.join("..", "Resources", "election_data.csv")

# List Assignments
Voter_IDs = []
Counties = []
Voted_For = []
Candidates = []
Votes = []
Percent = []

# Open The CSV File
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Bypassing The Headers
    csv_header = next(csv_reader)

    # Row Loop Appending Data To Lists
    for row in csv_reader:
        Voter_IDs.append(row[0])
        Counties.append(row[1])
        Voted_For.append(row[2])

# The total number of votes cast
total_votes = len(Voter_IDs)

# A complete list of candidates who received votes
for name in Voted_For:
    if name not in Candidates:
        Candidates.append(name)

# The number and percentage of votes for each candidate
running = len(Candidates)

i = 0
for i in range(running):
    Votes.append(Voted_For.count(Candidates[i]))
    Percent.append((Votes[i] / total_votes) * 100)

# The winner of the election based on popular vote.
most_votes = max(Votes)
j = Votes.index(most_votes)
winner = Candidates[j]

# Print Analysis To Terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

k = 0
for k in range(running):
    print(f'{Candidates[k]}: {round(Percent[k], 3)}% ({Votes[k]})')

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Set Path For Analysis File
output_path = os.path.join("..", "Analysis", "Analysis.txt") 

# Create The TXT File
txtwriter = open(output_path, "w")

# Write Analysis To TXT File
txtwriter.writelines('Election Results \n')
txtwriter.writelines('------------------------- \n')
txtwriter.writelines(f'Total Votes: {total_votes} \n')
txtwriter.writelines('------------------------- \n')

l = 0
for l in range(running):
    txtwriter.writelines(f'{Candidates[l]}: {round(Percent[l], 3)}% ({Votes[l]}) \n')

txtwriter.writelines('------------------------- \n')
txtwriter.writelines(f'Winner: {winner} \n')
txtwriter.writelines('------------------------- \n')