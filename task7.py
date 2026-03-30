import pandas as pd

students = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Subject': ['Math', 'Science', 'Math', 'History', 'Math'],
    'Marks': [85, 65, 92, 78, 68]
}
data = pd.DataFrame(students)

# Find average marks per subject
avg_marks = data.groupby('Subject')['Marks'].mean()
print(avg_marks)

# Count number of students per subject
student_count = data.groupby('Subject')['Student'].count()
print(student_count)

# Find maximum marks per subject
max_marks = data.groupby('Subject')['Marks'].max()
print(max_marks)
