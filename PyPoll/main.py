import csv

TotalVotes = 0 
 


# Files to Load
input = "election.csv"

votes = 0
winnervotes = 0

candidates = []
num_votes = 0
vote_counts = []


with open(input, newline='') as input:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(input, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

#The total number of votes cast
        TotalVotes = TotalVotes + 1
        
print(TotalVotes)
#A complete list of candidates who received votes

candidate = row[2]
            if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)
#The percentage of votes each candidate won
percentages = []
max_votes = vote_counts[0]
max_index = 0

count = row[0]
print(vote_counts)
print(candidates)
#The total number of votes each candidate won
    for count in range(len(candidates)):
        vote_percentage = (vote_counts[count]/num_votes)*100
        percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
        winner = candidates[max_index]

#The winner of the election based on popular vote.

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")
