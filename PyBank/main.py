import os
import csv
path = os.getcwd()
#print(path)
date = [] # empty list by creating square brackets
profit_losses = []
with open("Resources/budget_data.csv",'r') as csvfile:
    data_reader = csv.reader(csvfile)
    for i in data_reader: # to remove titles 
        break
    for dt, pr_ls in data_reader:
        date.append(dt)
        profit_losses.append(int(pr_ls))
        
#print(date)
#print(profit_losses)  
total_months =len(date) #counting how many items in the data structure -passing date and we are counting how many items.
out_month = "Total Months: "+ str(total_months)
print(out_month)
total_pl = sum(profit_losses) #adding all the numerical values
total_profit = "Total $" + str(total_pl)
print(total_profit)
mean_pl = total_pl/total_months 
a_change = "Average Change $" + str(mean_pl )
print(a_change)
ma_profits = max(profit_losses)
ma_index = profit_losses.index(ma_profits)
ma_date = date[ma_index]
max_profits = "Greatest Increase in Profits :"+ma_date+" "+ str(ma_profits)
print(max_profits)
mi_profits = min(profit_losses)
mi_index = profit_losses.index(mi_profits) # refer. the profit losses list to ask about the index of the minimum value
mi_date = date[mi_index]
min_profts = "Greatest Decrease in Profits :"+mi_date+" "+ str(mi_profits)
print(min_profts)




