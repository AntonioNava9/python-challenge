
import csv

data = csv.DictReader(open('./Resources/budget_data.csv'))

months = 0
total = 0

for row in data:
    months += 1
    total += int(row['Profit/Losses'])















output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

print(output)


# import csv

# with open('./Resources/budget_data.csv') as data:

#     next(data)
    
#     for row in csv.reader(data):
#         print(row)