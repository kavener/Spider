import csv

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Joedan', 21])
