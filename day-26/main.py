import random
import pandas

# List Comprehension
# new_list = [item for item in list]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

new_list = [n * 2 for n in range(0, 5)]

# List Comprehension with test
# [item for item in list if test]
names = ["Alan", "Charlie", "Jake"]
short_names = [name for name in names if len(name) <= 4]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]

# Dict Comprehension
names = ["Alan", "Charlie", "Jake"]
student_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)

# Iterating Over a Pandas DataFrame
student_dict = {
    "student": ["Alice", "Bob", "Charlie"],
    "score": [56, 78, 90]
}

# Loop
# for (key, value) in student_dict.items():
#     print(value)

student_df = pandas.DataFrame(student_dict)
print(student_df)

# Loop through data frame
# for (key, value) in student_df.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row.score)