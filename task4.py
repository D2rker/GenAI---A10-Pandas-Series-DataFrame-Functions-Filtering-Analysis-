import pandas as pd

data = {
    'Name' : ['amit', 'neha', 'rahul', 'sneha', 'pooja'],
    'Marks' : [78, 85, 90, 66, 72],
    'Subject' : ['math', 'math', 'science', 'science', 'math']
}

collection = pd.DataFrame(data)

# print first 3 rows
print("first 3 rows")
print(collection.head(3))

# print last 2 rows
print("last 2 rows")
print(collection.tail(2))

# shape
print(f"Dataframe shape: {collection.shape}")

# column name
print(f"Column name : {list(collection.columns)}")
