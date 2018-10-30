import os
import csv

#opening csv file

csvpath=os.path.join("budget_data.csv")

with open (csvpath, "r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    

    
    profit_losses=0 
    change_list=[]
    date_list=[]
    start_value=867884
    for line in csvreader:
# Calculating total profi + losses
        profit_losses= profit_losses + int(line[1])
#Calculating change every month and adding to a list (change_list)
# after each loop, start value is defined as the current line[1], to be used in next loop
        change=int(line[1])-start_value
        change_list.append(change)
        start_value=int(line[1])
# Adding dates to a list of dates (date_list)
        date_list.append(line[0])
        
#Calculating total months based on date_list       
    number_months=len(date_list) 

#Calculating total change based on change_list     
    total_change= sum(change_list)
    
#Calculating average change in "Profit/Losses" between months     
    average_change = total_change/(number_months - 1)

#Determining greatest increase and decrease    
    greatest_profit=(max(change_list))
    greatest_losses=(min(change_list))
   

    print ("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(number_months))
    print ("Total: $" + str(profit_losses))
    print ("Average  Change: $" + str(average_change))
    print("Greatest Increase in Profits: $" + str(greatest_profit))
    print ("Greatest Decrease in Profits: $" + str(greatest_losses))            
        
    
  
        
        
        
'''
## questions
#how to format number decimal
#how to input date in front of greatest profit and losses
with open (csvpath, "r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
        
    for line in csvreader: 
    
        if int(line[1])==greatest_profit:
            greatest_profit_date=str(line[0])
        elif int(line[1])==greatest_losses:
            greatest_losses_date=str(line[0])
'''