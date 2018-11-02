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
    
    percent_votes_correy=round(((total_votes_correy/number_votes)*100), 3)
    percent_votes_li=round(((total_votes_li/number_votes)*100), 3)
    percent_votes_otooley=round(((total_votes_otooley/number_votes)*100), 3)
    percent_votes_khan=round(((total_votes_khan/number_votes)*100), 3)
    
    total_votes_candidates=[percent_votes_correy, percent_votes_li, percent_votes_otooley, percent_votes_khan]
    winner_votes= max(total_votes_candidates)                       
    
    
    if winner_votes==percent_votes_correy:
        winner= "Correy"
    elif winner_votes==percent_votes_li:
        winner= "Li"
    elif winner_votes==percent_votes_otooley:
        winner= "O'Tooley"
    elif winner_votes==percent_votes_khan:
        winner= "Khan"
        
print ("  -------------------------")    
print ("Election Results")
print("  -------------------------")
print("Total Votes: " + str(number_votes))
print("  -------------------------")
print("Khan: "+str(percent_votes_khan)+"% ("+str(total_votes_khan)+")")
print("Correy: "+str(percent_votes_correy)+"% ("+str(total_votes_correy)+")")
print("Li: "+str(percent_votes_li)+"% ("+str(total_votes_li)+")")
print("O'Tooley: "+str(percent_votes_otooley)+"% ("+str(total_votes_otooley)+")")
print("  -------------------------")
print("Winner: "+ winner)
print("  -------------------------")
    
with open('pypool_result.txt', 'w+') as f:     
    
    print (("  -------------------------"), file=f)     
    print (("Election Results"), file=f)
    print(("  -------------------------"), file=f)
    print (("Total Votes: " + str(number_votes)), file=f)
    print(("  -------------------------"), file=f)
    print(("Khan: "+str(percent_votes_khan)+"% ("+str(total_votes_khan)+")"), file=f)
    print(("Correy: "+str(percent_votes_correy)+"% ("+str(total_votes_correy)+")"), file=f)
    print(("Li: "+str(percent_votes_li)+"% ("+str(total_votes_li)+")"), file=f)
    print(("O'Tooley: "+str(percent_votes_otooley)+"% ("+str(total_votes_otooley)+")"), file=f)
    print(("  -------------------------"), file=f)
    print(("Winner: "+ winner), file=f)
    print(("  -------------------------"), file=f)

    f.close()