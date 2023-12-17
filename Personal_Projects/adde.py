my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

if my_list:
    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    average = total_score / total_weight
else:
    average = 0


print("Average: {:0.2f}".format(average))