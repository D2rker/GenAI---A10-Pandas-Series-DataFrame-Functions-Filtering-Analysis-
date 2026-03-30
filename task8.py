import pandas as pd

students = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Math'],
    'Marks': [85, 65, 92, 78, 68]
}
data = pd.DataFrame(students)

# Bar graph of student names vs marks
data.plot(kind='bar', x='Student', y='Marks')

# Line graph of marks
data['Marks'].plot(kind='line')

# Histogram of marks
data['Marks'].plot(kind='hist')
