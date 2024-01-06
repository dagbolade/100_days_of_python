# list of names in the group
from prettytable import PrettyTable

group_names = ["sultan", "scholar", "Ateek", "haykay", "ibrahim", "ayodele", "sopurunkem", "seun jay", "adebisi",
               "festus", "ayobami", "samuel", "david", "chike", "ayuba", "noel phil", "fikun", "makinde"]
# import random
import random

# shuffle the names
random.shuffle(group_names)

# creat an empty list to store the names
grouped_names = []
index = 0

while index < len(group_names):
    group = group_names[index:index + 3]
    grouped_names.append(group)
    index += 3

labeled_groups = {}
group_labels = ["Group A", "Group B", "Group C", "Group D", "Group E", "Group F", "Group G"]
for i in range(len(grouped_names)):
    labeled_groups[group_labels[i]] = grouped_names[i]


def add_new_name(new_name):
    # Checking if the last group has less than 3 members
    if len(grouped_names[-1]) < 3:
        grouped_names[-1].append(new_name)
    else:
        # If the last group is full, start a new group
        grouped_names.append([new_name])
        # Check if a new label is needed
        if len(grouped_names) > len(group_labels):
            # Creating a new label using chr() to convert ASCII to characters and ord() to convert characters to ASCII
            # to get the next letter in the alphabet
            next_label = "Group " + chr(ord(group_labels[-1][-1]) + 1)
            group_labels.append(next_label)
    # Update the labeled_groups dictionary so that it contains the new name
    for i, group in enumerate(grouped_names):
        labeled_groups[group_labels[i]] = group


# Adding new names to the list
add_new_name("muslim tech bro")
add_new_name("bosco")
add_new_name("ayojaco")
add_new_name("bishop")
add_new_name("michael")

# Printing the group in a nice format instead of a dictionary
for group_label, names in labeled_groups.items():
    names_str = ", ".join(names)
    print(f"{group_label}: {names_str}")


