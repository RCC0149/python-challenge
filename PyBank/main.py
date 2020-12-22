# Import Modules
import os
import csv

# Set Path For Resource File
csv_path = os.path.join("..", "Resources", "budget_data.csv")

Months = []
Profit_Losses = []
Changes = []

# Open The CSV File
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    # Row Loop
    for row in csv_reader:
        Months.append(row[0])
        Profit_Losses.append(row[1])

# The total number of months included in the dataset
length = len(Months)

# The net total amount of "Profit/Losses" over the entire period
total = 0
for number in Profit_Losses:
    total += int(number)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
i = 0
for i in range(length - 1):
    Changes.append(int(Profit_Losses[i + 1]) - int(Profit_Losses[i]))

change_total = 0
for delta in Changes:
    change_total += int(delta)

avg_change = change_total / (length - 1)

# The greatest increase in profits (date and amount) over the entire period
max_change = max(Changes)
j = Changes.index(max_change)
max_date = Months[j + 1]

# The greatest decrease in losses (date and amount) over the entire period
min_change = min(Changes)
k = Changes.index(min_change)
min_date = Months[k + 1]

# Set Path For Analysis File
output_path = os.path.join("..", "Analysis", "Analysis.txt") 

# Create The TXT File
txtwriter = open(output_path, "w")

# Write To TXT File
txtwriter.writelines('Financial Analysis \n')
txtwriter.writelines('------------------ \n')
txtwriter.writelines(f'Total Months: {length} \n')
txtwriter.writelines(f'Total: ${total} \n')
txtwriter.writelines(f'Average Change: ${round(avg_change, 2)} \n')
txtwriter.writelines(f'Greatest Increase In Profits: {max_date} (${max_change}) \n')
txtwriter.writelines(f'Greatest Decrease In Profits: {min_date} (${min_change}) \n')