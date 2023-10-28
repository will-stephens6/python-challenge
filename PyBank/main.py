import csv

# Define a function to calculate the average change in profit/loss.
def calculate_average_change(monthly_pL):
    total_change = 0
    for x in range(1,len(monthly_pL)):#loop through starting at second row 
        total_change += int(monthly_pL[x][1])-int(monthly_pL[x-1][1]) #formula to find the monthly change 
    return total_change/(len(monthly_pL)-1) #return the avg change  

# Define a function to find the month with the greatest increase in profit.
def find_greatest_change(monthly_pL):
    greatest_change = ["",0]
    for x in range(1,len(monthly_pL)):#loop through starting at second row  
        current_change = int(monthly_pL[x][1])-int(monthly_pL[x-1][1]) #formula to find the monthly change 
        if current_change > greatest_change[1]: #check if current change is greater than current greatest change
            greatest_change[1] = current_change
            greatest_change[0] = monthly_pL[x][0]
    return greatest_change #return the greatest change month

# Define a function to find the month with the greatest decrease in profit.
def find_smallest_change(monthly_pL):
    smallest_change = ["",0]
    for x in range(1,len(monthly_pL)):#loop through starting at second row  
        current_change = int(monthly_pL[x][1])-int(monthly_pL[x-1][1]) #formula to find the monthly change 
        if current_change < smallest_change[1]:
            smallest_change[1] = current_change
            smallest_change[0] = monthly_pL[x][0]
    return smallest_change 


with open("PyBank/Resources/budget_data.csv", mode="r") as file: #open the csv
    csv_reader = csv.reader(file, delimiter=",") #use csv reader to read to the file 
    next(csv_reader) #skip column headers

    total_profit_loss = 0
    budget_data_list = [] #store budget data as a list for later 
    
    for line in csv_reader: #loop to increase total months count by 1 each line 
        total_profit_loss = total_profit_loss + int(line[1])#add each month's profit and losses together for each line
        budget_data_list.append(line)#add each month's profit/loss to the budget list 

    total_months = len(budget_data_list) #calculate total number of months 
    average_change = calculate_average_change(budget_data_list) #calculate average 
    greatest_change = find_greatest_change(budget_data_list) #calculate greatest increase 
    smallest_change = find_smallest_change(budget_data_list) #calculate greatest decrease

    #print each line 
    print("Financial Analysis") 
    print("----------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}.00")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Change: {greatest_change[0]} (${round(greatest_change[1],2)})")
    print(f"Smallest Change: {smallest_change[0]} (${round(smallest_change[1],2)})")

 # Write to a .txt file 
    with open("PyBank/analysis/financial_analysis.txt", "w") as result_file:
        result_file.write("Financial Analysis\n")
        result_file.write("----------------------------\n")
        result_file.write(f"Total Months: {total_months}\n")
        result_file.write(f"Total: ${total_profit_loss}\n")
        result_file.write(f"Average Change: ${round(average_change, 2)}\n")
        result_file.write(f"Greatest Increase in Profits: {greatest_change[0]} (${greatest_change[1]})\n")
        result_file.write(f"Greatest Decrease in Profits: {smallest_change[0]} (${smallest_change[1]})\n")
