import pandas as pd

sales_data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}
sales = pd.DataFrame(sales_data)

# Total revenue
total_revenue = sales['Revenue'].sum()
print(f"Total Revenue: {total_revenue}")

# Average daily revenue
average_revenue = sales['Revenue'].mean()
print(f"Average Daily Revenue: {average_revenue}")

# Day with highest revenue
highest_revenue_row = sales.loc[sales['Revenue'].idxmax()]
print(f"Day with highest revenue: {highest_revenue_row['Day']} ({highest_revenue_row['Revenue']})")

# Days where revenue > average
above_average_days = sales[sales['Revenue'] > average_revenue]
print("\nDays with above-average revenue:")
print(above_average_days)

# Plot revenue vs day
sales.plot(kind='line', x='Day', y='Revenue', marker='o')
