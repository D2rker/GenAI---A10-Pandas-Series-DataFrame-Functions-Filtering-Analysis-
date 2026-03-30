import pandas as pd

students = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Math'],
    'Marks': [85, 65, 92, 78, 68]
}
data = pd.DataFrame(students)

# Students who scored more than 75 marks
filter_1 = data[data['Marks'] > 75]

# Students belonging to subject Math
filter_2 = data[data['Subject'] == 'Math']

# Students who scored more than average marks
filter_3 = data[data['Marks'] > data['Marks'].mean()]

# Students who failed (marks < 70)
filter_4 = data[data['Marks'] < 70]
