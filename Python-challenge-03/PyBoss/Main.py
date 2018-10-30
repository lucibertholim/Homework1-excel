import os
import csv

#opening csv file

csvpath=os.path.join("employee_data.csv")
new_disctionary={}
with open (csvpath, "r", newline="") as csvfile:
    csvreader=csv.DictReader(csvfile)
    for row in csvreader:
        print(row['Emp ID'], row['Name'], row['SSN'], row['State'])
        
        
       