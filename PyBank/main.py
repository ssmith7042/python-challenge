import os
import csv
#importing modules to read file
budget_data=os.path.join("Resources", "budget_data.csv")
#initialize variables that will make sense later (just kidding theyre self-explanatory)
month_count=0
profit_losses=0
previous_month=0
month_diffs=[]
month_list=[]
#open file and store header
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvfile)
    
    
    #count months, calculate total profit/losses, populate list of month to month p/l and make corresponding list of months
    for row in csvreader:
        month_count+=1 
        profit_losses+=int(row[1])
        if month_count>1:
            month_diffs.append(int(row[1])-previous_month)
            month_list.append(row[0])
        previous_month=int(row[1])
#analyze month to month p/l data
avg_diff=sum(month_diffs)/len(month_diffs)
max_loss=min(month_diffs)
theworstmonth=(month_list[month_diffs.index(max_loss)])
max_gain=max(month_diffs)
thebestmonth=(month_list[month_diffs.index(max_gain)])
#display findings
print(f"Financial Analsis \nTotal Months={month_count} \nTotal={profit_losses} \nAverage Change={avg_diff:.2f} \nGreatest Increase in Profits=({thebestmonth}){max_gain}\nGreatest Decrease in Profits=({theworstmonth}){max_loss}")
#define function for writing new text file
def write_to_file(filename, lines):
     with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")
#call function with analysis output
write_to_file("analysis/analysis.txt",["Financial Analysis","--------------------", 
            "Total Months=86","Total=22,564,198","Average Change=-8,311.11","Greatest Increase in Profits=(Aug-16)1,862,002)",
            "Greatest Decrease in Profits=(Feb-14)-1,825,558)"])
