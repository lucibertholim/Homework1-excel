import os
import csv

# string for the split function
import string

#datetime for formating date
from datetime import datetime

# US state dictionary to translate US States to Two letter codes
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#opening csv file

csvpath=os.path.join("employee_data.csv")
new_disctionary={}
with open (csvpath, "r", newline="") as csvfile:
    csvreader=csv.DictReader(csvfile)
    for row in csvreader:
        
# Formating date and calling new variable for date DOB2 
       (row["DOB"]) = datetime.strptime((row["DOB"]), '%Y-%m-%d')
       DOB2 = (row["DOB"]).strftime('%m/%d/%Y')
       
# Formating SSN to hide the first five numbers
       x=(row["SSN"])
       SSN2= ("***-**"+str(x[6:]))

#Using state dictionary to translate US States to Two letter codes
       State2=us_state_abbrev[(row["State"])]
       
# Creating a dictionary for new variables inside the loop
       employee_dictionary = {
                   "Emp ID": row["Emp ID"],
                   "First Name": row["Name"].split(" ")[0].strip(),
                   "Last Name": row["Name"].split(" ")[1].strip(),
                   "DOB": str(DOB2),
                   "SSN": str(SSN2),
                   "State": str(State2),
                   }        
       
# Writing dictionary to csv file
       with open("employee_data2.csv", 'w') as csvfile:
           fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
           writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
       
           writer.writeheader()
           
           writer.writerow(employee_dictionary)