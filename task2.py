import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

# adding 5 grace marks
grace_marks = series + 5
print(f"After adding 5 grace marks: {grace_marks}")

# subtract 2 marks
subtract = grace_marks - 5
print(f"after subtracting 2 marks: {subtract}")

# multiply by 1.05
multiplying = grace_marks * 1.02
print(f"after multiplying 1.02 marks: {multiplying}")

# Divide by 2
Divide = grace_marks / 2
print(f"after Divide by 2: {Divide}")