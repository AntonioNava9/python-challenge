
import csv

data = csv.DictReader(open('./Resources/budget_data.csv'))
my_report = open('./Analysis/Report.txt', "w")

months = 0
total = 0
total_ch = 0
pre_rev = 0
inc = [0,'']
dec = [0,'']

for row in data:
    # revenue
    rev = int(row['Profit/Losses'])
    
    months += 1
    total += rev

    # change
    change = rev - pre_rev
    if pre_rev == 0:
        change = 0
    
    total_ch += change
    pre_rev = rev

    # Greatest Increase
    if change > inc[0]:
        inc[0] = change
        inc[1] = row['Date']

    # Greatest Decrease
    if change < dec[0]:
        dec[0] = change
        dec[1] = row['Date']


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[1]} (${inc[0]:,})
Greatest Decrease in Profits: {dec[1]} (${dec[0]:,})
'''

print(output)
my_report.write(output)

# import csv

# with open('./Resources/budget_data.csv') as data:

#     next(data)
    
#     for row in csv.reader(data):
#         print(row)