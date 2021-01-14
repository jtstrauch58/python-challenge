# Import os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as vote_file:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(vote_file, delimiter=',')


#     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
#     # Read each row of data after the header into date and profit lists

    voting_id =[]
    county = []
    candidate = []

    for row in csvreader:
        voting_id.append(row[0]) 
        county.append(row[1])
        candidate.append(row[2])

#   # Find number of financial records in file
    row_length = len(county)

#   # Convert candidate list to set and sort
    candidate_set = set(candidate)
    people = sorted(list(candidate_set), reverse=False)

#   # Count votes for each candidate
    votes = list(range(len(people)))
   
    for num, politicians in enumerate(people):
        votes[num] = candidate.count(politicians)
    

#   # Determine vote spread per candidate
    spread = list(range(len(people)))
    for num,counts in enumerate(votes):
        spread[num] = 100*counts/sum(votes)

#   # Sort vote count highest to lowest
    votes_sorted = sorted(votes, reverse=True)

#   Make an index converter to associate votes, vote percentage and candidate
    converter = []
    for num, count in enumerate(votes_sorted):
        for index, total in enumerate(votes):
            if total == count:
               converter.append(index)

    
# #   # Print the results for the study to the terminal

    print("Election Results")
    print("-----------------")
    print("Total Votes: " + '{:,}'.format(sum(votes)))
    print("-----------------")
    for y in range(len(votes_sorted)):
        print(people[converter[y]] + ': '+ format(spread[converter[y]],'.2f') + '% (' + '{:,}'.format(votes_sorted[y])+')')
    print("-----------------")
    print("Winner: " + people[converter[0]])
    print("-----------------")
    print("```")

# # Set the output path for the results file

output_path = os.path.join(".", "analysis", "pypol_analysis.csv")

# # open the csv file to write the data

with open(output_path, 'w', newline='') as csvfile:

# #     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

# #     # Write the election results report to the csv file

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Total Votes: ' + '{:,}'.format(sum(votes))])
    for y in range(len(votes_sorted)):
        csvwriter.writerow([people[converter[y]] + ': '+ format(spread[converter[y]],'.2f') + '% (' + '{:,}'.format(votes_sorted[y])+')'])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Winner: ' + people[converter[0]]])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['```'])








