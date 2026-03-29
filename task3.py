import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

# maximum marks
print(f"Maximum marks: {series.max()}")
# minimum marks
print(f"Minimum marks: {series.min()}")
# sum of all marks
print(f"Sum of marks: {series.sum()}")
# mean
print(f"Mean marks: {series.mean()}")

pass_status = series.apply(lambda x: x >= 70)
print("\nPass Status (True = Pass, False = Fail):")
print(pass_status)

# how many students passed
pass_count = pass_status.sum()
print(f"\nNumber of students who passed: {pass_count}")