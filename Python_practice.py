from __future__ import print_function
from ast import If
from email.errors import InvalidMultipartContentTransferEncodingDefect
from itertools import count
from operator import truediv
from os import remove


print ("Hello World")
# creates a variable with a string "Son"
title="Son" 
# creates a variable with an integer 80
years=80
# creates a variable with the boolean value of True
expert_status= True

print("Heung Min"+ title)

counties= ["Arapahoe","Denver","Jefferson"]
print(counties)
counties.append("El Paso")
print(counties)
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
counties_dict={}
counties_dict["Arapahoe"]= 422829
print(counties_dict)
counties_dict["Denver"]= 463353
counties_dict["Jefferson"]= 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
## Dictionaries where the keys are "county" and "registered_voters" and 
## each country and its corresponding registered voters are the values for those keys
## county is the key and what follows is the value
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
print(voting_data)
print(len(voting_data))
voting_data.append({"country":"El Paso","registered_voters":461149})
print(voting_data)
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
print(voting_data)
voting_data.insert(3,{"county":"Denver","registered_voters":463353})
print(voting_data)
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print(voting_data)
# my_votes=int(input("How many votes did you get in the election?"))
# print(my_votes)
# total_votes=int(input("What is the total votes in the election?"))
# percentage_votes=(my_votes/total_votes)*100
# print("I received"+str(percentage_votes)+"% of the total votes.")

# == is a comparison operator or boolena operator, which means equal to.
# since the second item in the counties list in counties is denver, the condition is met
# and will display denver in the terminal
if counties[1]=='Denver':
    print(counties[1])
counties= ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties") 
else:
    print("Arapahoe or El Paso is not in the list of counties") 

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")
for county in counties:
    print(county)

print(counties_dict)

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))
for county, registered_voters in counties_dict.items():
    print(county, registered_voters) 

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Only print the name
for county_dict in voting_data:
    print(county_dict['county'])

print(county+"county has"+str(voters)+"registered voters")

for county, voters in counties_dict.items():
    print(f"{county}county has{voters}registered voters")

candidate_votes= int(input("How many votes did the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the election?"))
message_to_candidate= (
        f"you received {candidate_votes} number of votes"
        f"The total number of votes in the elction was {total_votes}"
        f"You received {candidate_votes/total_votes*100:.2f}% of the total votes")
print(message_to_candidate)