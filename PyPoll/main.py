
import csv, os

my_report = open('./Analysis/Report.txt', "w")
data_file = os.path.join('Resources','election_data.csv')

total = 0
winner = [0,'']
candidates = {}

with open(data_file) as data:
    
    csvreader = csv.reader(data, delimiter=',')
    csv_header = next(csvreader)
    rows = csv.reader(data)    
    
    for row in rows:
        total += 1
        candidate = row[2]
        if candidate not in candidates.keys():
            candidates[candidate] = 0
        candidates[candidate] += 1

output = f'''
Election Results
-------------------------
Total Votes: {total:,}
-------------------------
'''

for candidate in candidates.keys():
    if winner[0] < candidates[candidate]:
        winner[0] = candidates[candidate]
        winner[1] = candidate

    output += f'{candidate}: {candidates[candidate]/total*100:.3f}% ({candidates[candidate]:,})\n'

output += f'''-------------------------
Winner: {winner[1]}
-------------------------'''

print(output)
my_report.write(output)