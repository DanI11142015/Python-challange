import csv
import os

path = os.getcwd()
print(path)
total_votes = 0
# county =[]
candidate = {}
candidate_votes = {}
winner_candidate = ""
winner_can_votes = 0

with open("Resources/election_data.csv" , 'r') as csvfile :
    data_reader = csv.reader(csvfile)
    header = next(data_reader)
    print(header)
    for row in data_reader :
        total_votes = total_votes + 1
        candidate = row[2]
        # print(candidate)
        # if key in dict already
        if candidate in candidate_votes.keys() :
            candidate_votes[candidate] += 1
        else :
            #create a new key by using square brackets []
            # setup a new key with the Value of 1
            candidate_votes[candidate] = 1
print(candidate_votes)
print(candidate_votes.keys())
#print('\n'.join(list(candidate_votes.keys()))
vote_count = 0
for index,candidate in enumerate(candidate_votes.keys()):
    #print(f"{index+1}. {candidate}. ")
    vote_count += candidate_votes[candidate]
    
total_votes = sum(candidate_votes.values())
print("total votes")
print(total_votes)
#print(vote_count)