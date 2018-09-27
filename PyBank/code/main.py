import os
import csv

bank_csv_path = os.path.join( "..", "Resources", "budget_data.csv")
totaltrans =[]
months=[]
average=[]
profchange=[]

with open(bank_csv_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader,None)
        for row in csvreader:
            
            totaltrans.append(float(row[1]))
            months.append(row[0])
        
        num=len(months)
        total=sum(totaltrans)
        for i in range(1):
            while  i <= len(totaltrans)-2:
                profchange.append(totaltrans[i+1]-totaltrans[i])
                i=i+1
                add=sum(profchange)
                average=(add/85)
                maxprof=max(profchange)
                minprof=min(profchange)
                
                
            print("financial analysis")
            print("__________________________")
            print (f"total months: {str(num)}")
            print (f"total:$ {str(total)}")
            print (f"average change:${str(average)}")
            print (f"Greatest Increase in Profits:$ {str(maxprof)}")
            print (f"Greatest Decrease in Profits:$ {str(minprof)}")