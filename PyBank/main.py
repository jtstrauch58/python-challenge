# Import os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as budget_file:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_file, delimiter=',')


#     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
#     # Read each row of data after the header into date and profit lists

    profit =[]
    dates = []

    for row in csvreader:
        dates.append(row[0]) 
        profit.append(row[1])

#   # Find number of financial records in file
    row_length = len(profit)

#   # Convert string list to integer array
    for x in range(row_length):
        profit[x]=int(profit[x])

#   # Calcuate sum, min, max of profits using list methods
    summ = sum(profit)
    minprofit = min(profit)
    maxprofit = max(profit)

#   # Find dates for min and max profits using index method
    mindate = dates[profit.index(minprofit)]
    maxdate = dates[profit.index(maxprofit)]

#   # Determine profit changes between each month
    prof_diff = 0
    for x in range(row_length-1):
        prof_diff = prof_diff + profit[x+1]-profit[x]

#   # Calculate average profit change
    avgprofit = prof_diff/ (row_length-1) 

#   # Print the results for the study

    print(" ")
    print("Financial Analysis")
    print("--------------------------------------------------")
    print("Total Months                : " + str(row_length))
    print("Total Profits               : " + "$" + '{:,}'.format(summ))
    print("Average Change              : " + "$" + format(avgprofit,'.2f'))
    print("Greatest increase in profits: " + maxdate + " $" + '{:,}'.format(maxprofit))
    print("Greatest decrease in profits: " + mindate + " $" + '{:,}'.format(minprofit))
    print("----")

# Set the output path

output_path = os.path.join(".", "analysis", "pybank_analysis.csv")

# open the csv file to write the data

with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

#     # Write the financial analysis report to the csv file

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------------'])
    csvwriter.writerow(['Total Months: ' + str(row_length)])
    csvwriter.writerow(['Total Profits: ' + '$' + '{:,}'.format(summ)])
    csvwriter.writerow(['Average Change: ' + '$' + format(avgprofit,'.2f')])
    csvwriter.writerow(['Greatest increase in profits: ' + maxdate + ' $' + '{:,}'.format(maxprofit)])
    csvwriter.writerow(['Greatest decrease in profits: ' + mindate + ' $' + '{:,}'.format(minprofit)])
    csvwriter.writerow(['```'])






