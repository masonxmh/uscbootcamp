import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")
#open&read csv

with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #read the header row first 
    next (csv_reader)
    #read through each row of data after the header
    
    date_list =[]
    profit_losses_list =[]
    diff_list=[]
    
    
    
    for row in csv_reader:
        date_list.append(row[0])
        total_month = len(date_list)
               
        profit_losses_list.append(int(row[1]))
        net_total = sum(profit_losses_list)
        
        
        
    for i in range(len(profit_losses_list)-1):  
        diff_list.append(profit_losses_list[i+1]-profit_losses_list[i])
    average=sum(diff_list)/len(diff_list)
    round_average=round(average,2)
    
    
    profitdiff_max=max(diff_list)
    max_date = date_list[diff_list.index(profitdiff_max)+1]
    profitdiff_min=min(diff_list)
    min_date = date_list[diff_list.index(profitdiff_min)+1]
    
    
    
    P=("Financial Analysis\n------------------------\n" +
           "Total Months: "+ str(total_month)+
           "\nTotal: $"+str(net_total)+
           "\nAverage Change: $" + str(round_average)+
           "\nGreatest Increase in Profits:"+max_date+
           " ($"+str(profitdiff_max)+")"+
           "\nGreatest Decrease in Profits:"+min_date+" ($"+
           str(profitdiff_min)+")")
    print(P)


output_path=os.path.join("financial_analysis.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n------------------------\n")
    txtfile.write("Total Months: "+ str(total_month))
    txtfile.write("\nTotal: $"+str(net_total))
    txtfile.write("\nAverage Change: $" + str(round_average)+"\nGreatest Increase in Profits:"+max_date+" ($"+str(profitdiff_max)+")")
    txtfile.write("\nGreatest Decrease in Profits:"+min_date+" ($"+
           str(profitdiff_min)+")")