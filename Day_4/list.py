# # states of america states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
# "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
# "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
# "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
# "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
# "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
# "Hawaii"] print(states_of_america[0]) print(states_of_america[-1])
#
# states_of_america.append("Angelaland")
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
# print(states_of_america)

# Banker Roulette
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# import random
import random

random_name = random.randint(0, len(names) - 1)

print(f"{names[random_name]} is going to buy the meal today!")