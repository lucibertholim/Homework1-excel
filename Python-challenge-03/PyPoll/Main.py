import os
import csv

#opening csv file

csvpath=os.path.join("election_data.csv")

with open (csvpath, "r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

    voter_list=[]
    candidate_choice_list=[]
    for line in csvreader:
        voter_list.append(line[0])
        candidate_choice_list.append(line[2])
        
    number_votes= len(voter_list)
    candidates=set(candidate_choice_list)
    total_votes_correy=candidate_choice_list.count('Correy')
    total_votes_li=candidate_choice_list.count('Li')
    total_votes_otooley=candidate_choice_list.count("O'Tooley")
    total_votes_khan=candidate_choice_list.count('Khan')
    
    percent_votes_correy=(total_votes_correy/number_votes)*100
    percent_votes_li=(total_votes_li/number_votes)*100
    percent_votes_otooley=(total_votes_otooley/number_votes)*100
    percent_votes_khan=(total_votes_khan/number_votes)*100   
    
    
    
print (candidates)        
print(total_votes_correy)
print(percent_votes_correy)
print(total_votes_li)
print(percent_votes_li)
print(total_votes_otooley)
print(percent_votes_otooley)
print(total_votes_khan)
print(percent_votes_khan)
        
        