import os
import csv

vote_csv_path = os.path.join( "..", "Resources", "election_data.csv")
voterid =[]
county=[]
candidate=[]
profchange=[]

with open(vote_csv_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader,None)
        for row in csvreader:
            
            voterid.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        
        num=len(voterid)
        ctr1 = 0
for record in vote_csv_path:
    if record[2] == 'Khan':
        ctr1 += 1
        ctr2 = 0
for record in vote_csv_path:
    if record[2] == 'Correy':
        ctr2 += 1
        ctr3 = 0
for record in vote_csv_path:
    if record[2] =='Li':
        ctr3 += 1
        ctr4 = 0
for record in vote_csv_path:
    if record[2] == 'OTooley':
        ctr4 += 1

        add1=sum(ctr1/num)*100
        add2=sum(ctr2/num)*100
        add3=sum(ctr3/num)*100
        add4=sum(ctr4/num)*100
        
        print("election results")
        print("__________________________")
        print (f"total votes: {str(num)}")
        print (f"Khan:{str(add1)}")
        print (f"Correy:{str(add2)}")
        print (f"Li:{str(add3)}")
        print (f"O'Tooley:{str(add4)}")