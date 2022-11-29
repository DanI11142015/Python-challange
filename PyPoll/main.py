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
#reading in csv file 
with open("Resources/election_data.csv" , 'r') as csvfile :
    data_reader = csv.reader(csvfile)
    #skipping over the header row this data is not important
    header = next(data_reader)
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
#print(candidate_votes)

vote_count = 0
for index,candidate in enumerate(candidate_votes.keys()):
        vote_count += candidate_votes[candidate]
    
total_votes = sum(candidate_votes.values())
print("Election_results :")
print("------------------")
print("total votes")
print(total_votes)
print("-------------------")
# print(candidate_votes)
# print(candidate_votes.values())
#candidate is the key and candidate_votes is the dictionary 

    
winner = ''
max_votes = -1
for candidate in candidate_votes:
    indv_votes= candidate_votes [candidate]
    if indv_votes > max_votes:
        winner = candidate
        max_votes = indv_votes
    percent = (indv_votes/total_votes)*100
    print(f"{candidate} {indv_votes} {percent:.2f}%")
    
print('--------------------')
print('Winner: ',winner)



