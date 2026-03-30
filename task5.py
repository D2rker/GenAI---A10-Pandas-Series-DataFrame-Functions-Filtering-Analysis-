import pandas as pd

students_data = {
    'Name' : ['amit', 'neha', 'rahul', 'sneha', 'pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['math', 'math', 'science', 'science', 'math']
}

students = pd.DataFrame(students_data)

# print information
print("info")
students.info()

print("\n describe")
print(students.describe())

print("\n head")
print(students.head())

print("\n tail")
print(students.tail())


# sort students by marks in decending order
students_sorted = students.sort_values(by='Marks', ascending=False).reset_index(drop=True)

print("\n--- Sorted and Reset Index ---")
print(students_sorted)
