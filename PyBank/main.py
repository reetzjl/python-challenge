import csv

# Files to Load
input = "budget-data.csv"


# Variables to Track
TotalMonths = 0
TotalRevenue = 0
PrevRevenue = 0

Date = 0    
RevenueChange = 0 

MaxIncr = {"Date":"",
            "RevenueChange":0}

MaxDecr = {"Date":"",
            "RevenueChange":0}



# Read Files
with open(input, newline='') as input:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(input, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        ##The total number of months included in the dataset
        ##The total net amount of "Profit/Losses" over the entire period
        TotalMonths = TotalMonths + 1
        TotalRevenue = TotalRevenue + int(row[1])

        #second part of for loop
        Date = row[0]
        if Date == "Jan-10":
            PrevRevenue = int(row[1])
        else:
            Revenue = int(row[1])
            RevenueChange = Revenue - PrevRevenue
            PrevRevenue = Revenue
            
            if RevenueChange > MaxIncr["RevenueChange"]:
                MaxIncr["Date"] = Date
                MaxIncr["RevenueChange"] = RevenueChange

            if RevenueChange < MaxDecr["RevenueChange"]:
                MaxDecr["Date"] = Date
                MaxDecr["RevenueChange"] = RevenueChange
            
##The average change in "Profit/Losses" between months over the entire period
average  = TotalRevenue / TotalMonths


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total Revenue: {TotalRevenue}")
print({0}: {1}".format("Average Change",average))
print(f"Greatest Increase in Profits: {MaxIncr}"")
print(f"Greatest Decrease in Profits: {MaxDecr}")