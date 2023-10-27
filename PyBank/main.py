import csv

def calculate_average_change(monthly_pL):
    total_change = 0
    for x in range(len(monthly_pL[1:2])):
        total_change += int(monthly_pL[x-1])-int(monthly_pL[x])
        print(int(monthly_pL[x-1]))
        print(int(monthly_pL[x]))
        print(int(monthly_pL[x-1])-int(monthly_pL[x]))
    return total_change/(len(monthly_pL)-1)

with open("PyBank/Resources/budget_data.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=",") 
    next(csv_reader) #skip column headers

    total_profit_loss = 0
    budget_data_list = []
    
    for line in csv_reader: #loop to increase total months count by 1 each line 
        total_profit_loss = total_profit_loss + int(line[1])#add each month's profit and losses together for each line
        budget_data_list.append(line[1])#add each month's profit/loss to the budget list 

    total_months = len(budget_data_list)  
    average_change = calculate_average_change(budget_data_list)

    #print each line 
    print("Financial Analysis") 
    print("----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}.00")
    print(f"Average Change: {average_change}")
