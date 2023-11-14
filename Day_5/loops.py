fruits = ['Apple', 'Peach', 'Pear']
# accessing elements in a list

for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')
    print(fruits)
print(fruits)

# calculate average height
student_heights = input("Input a list of student heights ").split()
height = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

for heights in student_heights:
    height += heights
# Write your code below this row 👇
average_height = round(height / len(student_heights))
print(f"total height = {height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {average_height}")
