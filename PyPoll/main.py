import csv

with open("PyPoll/Resources/election_data.csv", mode="r") as file: #open the csv
    csv_reader = csv.reader(file, delimiter=",") #use csv reader to read to the file 
    next(csv_reader) #skip column headers

    total_votes = 0
    candidates_votes = {}
    
    for ballot in csv_reader:#look through the csv 
        total_votes += 1 #finds total of rows which is total votes 
        if ballot[2] in candidates_votes: #conditional to count 2nd index 
            candidates_votes[ballot[2]] += 1 
        else:
            candidates_votes[ballot[2]] = 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")


    for candidate, votes in candidates_votes.items():
        vote_percentage = (votes / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    
    winner = max(candidates_votes, key=candidates_votes.get)
    print(f"Winner: {winner}")
    print("-------------------------")

#write file to txt
with open("PyPoll/analysis/election_analysis.txt", "w") as result_file:
    result_file.write("Election Results\n")
    result_file.write("-------------------------\n")
    result_file.write(f"Total Votes: {total_votes}\n")
    result_file.write("-------------------------\n")

    for candidate, votes in candidates_votes.items():
        vote_percentage = (votes / total_votes) * 100
        result_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    result_file.write("-------------------------\n")
    result_file.write(f"Winner: {winner}\n")
    result_file.write("-------------------------\n")




        