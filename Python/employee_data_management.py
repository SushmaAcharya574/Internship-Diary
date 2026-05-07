import csv

file = open("empDetails.csv", "w")
writer = csv.writer(file)
writer.writerow(['ename', 'sal', 'job', 'deptNo'])
data = [['Smith', 10000, 'clerk', 4],
        ['John', 25000, 'analyst', 5],
        ['Anok', 52000, 'data scientist', 2],
        ['Karan', 29000, 'designer', 1]]
writer.writerows(data)
file.seek(0)
reader = csv.reader(file)

totalSal = 0
for row in reader:
  print(row['ename'])
  totalSal += row['sal']*12
print(f"\nTotal annual salary : {totalSal}")
file.close()
