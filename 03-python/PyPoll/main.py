import os
import csv

election_data_csv = os.path.join("Resources","election_data.csv")

#open&read csv

with open(election_data_csv, newline="") as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    #read the header row first
    next (csv_reader)
   
    #Define variables
    vote_dict={}
    max_vote=int()
    winner=str()
    vote_percent=float()
    
    #read through each row of data after the header
    for row in csv_reader:
        if row[2] not in vote_dict.keys():
            vote_dict[row[2]]=0
        vote_dict[row[2]]+=1
    # find total votes
    total_votes=sum(vote_dict.values())

    print("Election Results\n--------------------------\n" +
    "Total Votes: "+ str(total_votes)+
    "\n--------------------------")
   
    #print votes & find winner
    max_vote = max(vote_dict.values())
    for (key,value) in vote_dict.items():
        # calculate vote percentage
        vote_percent=value/total_votes
        #find winner
        if value==max_vote:
            winner=key
        print (key+": "+str("{:.3%}".format(vote_percent))+" "+str("({})".format(value)))
    print ("--------------------------")
    print ("Winner: "+ winner)
        
 # print to file       
output_path=os.path.join("PyPollResult.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Election Results\n--------------------------\n")
    txtfile.write("Total Votes: "+ str(total_votes))
    txtfile.write("\n--------------------------\n")
    for (key,value) in vote_dict.items():
        vote_percent=value/total_votes
        if value==max_vote:
            winner=key
        txtfile.write(key+": "+str("{:.3%}".format(vote_percent))+" "+str("({})".format(value))+"\n")
    txtfile.write("\n--------------------------")
    txtfile.write("\nWinner: "+  winner)       


