import os 
import csv

Budget2 = os.path.join('raw_data', 'budget_data_2.csv')

total_month = 0
total_revenue = 0
prev_revenue = 0
revenue_change_list = 0
month_of_change = 0
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
revenue_avg = 0

with open(Budget2, newline='') as csvfile:

    csv_reader = csv.DictReader(csvfile, delimiter=',')
    print(csv_reader)
    
    for row in csv_reader:
        
        total_month = total_month + 1
        total_revenue = total_revenue + int(row["Revenue"])
        prev_revenue = int(row["Revenue"])
        revenue_change = int(row["Revenue"]) - prev_revenue
        
        revenue_change_list = revenue_change_list + revenue_change
        month_of_change = month_of_change + [row["Date"]]
        if (revenue_change > greatest_increase[1]):
           greatest_increase[0] = row["Date"]
           greatest_increase[1] = revenue_change
       # save greatest decrease in revenue and month
        if (revenue_change < greatest_decrease[1]):
           greatest_decrease[0] = row["Date"]
           greatest_decrease[1] = revenue_change

# calculate the average revenue
    revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
# output Summary
    output = (
        f"\Financial Analysis\n"
        f"---------------------\n"
        f"Total Months: {total_months}\n")

print(output)
        






