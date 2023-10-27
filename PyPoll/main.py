import csv

with open("PyPoll/Resources/election_data.csv", mode="r") as file: #open the csv
    csv_reader = csv.reader(file, delimiter=",") #use csv reader to read to the file 
    next(csv_reader) #skip column headers

    total_votes = 0
    candidates_votes = {}
    
    for ballot in csv_reader:
        total_votes += 1 
        if ballot[2] in candidates_votes:
            candidates_votes[ballot[2]] += 1
        else:
            candidates_votes[ballot[2]] = 1

    for candidate,votes in candidates_votes.items():
        print("Election Results")
        print(f"{candidate} %{(votes/total_votes)*100} {votes}")
    
    winner = next(iter(candidates_votes))
    for candidate,votes in candidates_votes.items():
        if candidates_votes[winner] < candidates_votes[candidate]:
            winner = candidate

    print(f"Winner: {winner}")
        


        