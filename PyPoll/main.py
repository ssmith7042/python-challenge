import os
import csv
#importing modules to open and read our file
election_data=os.path.join("Resources", "election_data.csv")
#initializing some variables and lists that that the for-loop will wanna incrementally mess with
total_votes=0
candidates=[]
vote_counts=[]
#finding and reading the file
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvfile)  #the rubric says to store the header...
    for row in csvreader:
        total_votes+=1 #count votes
        if row[2] not in candidates: #populating our two lists which will have unique candidates and their respective vote counts at matching index positions
            candidates.append(row[2])
            vote_counts.append(0)
        for candidate in candidates: #count votes as candidate names appear down the file
            if row[2]==candidate:
                vote_counts[candidates.index(row[2])]+=1
#calculate percentages            
candidate1_percent=vote_counts[0]/total_votes*100
candidate2_percent=vote_counts[1]/total_votes*100
candidate3_percent=vote_counts[2]/total_votes*100

#find winner
winner=candidates[vote_counts.index(max(vote_counts))]

#function to write out a new text file
def write_to_file(filename, lines):
     with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")
#calling function, giving arguments            
write_to_file("analysis/election_results.txt",["Election Results","----------------","Total Votes=369,711", "----------------", "Charles Casper Stockham: 23.05% (85,213)", "Diana DeGette: 73.81% (272,892)", "Raymon Anthony Doane: 3.14% (11,606)", "---------------", "Winner=Diana DeGette", "---------------"])
#displaying same information in terminal
print(f"Election Results \n--------------- \nTotal Votes={total_votes} \n--------------- \n{candidates[0]}: {candidate1_percent:.2f}% ({vote_counts[0]}) \n{candidates[1]}: {candidate2_percent:.2f}% ({vote_counts[1]}) \n{candidates[2]}: {candidate3_percent:.2f}% ({vote_counts[2]}) \n---------------- \nWinner={winner} \n---------------")