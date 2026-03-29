import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

# series values
print(f"series values {series.values}")

# index
print(f"Index {series.index}")

# Data type
print(f"Data type {series.dtype}")

# Access element
print(f"Access first element {series[0]}")

# last 2nd element
print(f"last 2nd element {series[-2:]}")

