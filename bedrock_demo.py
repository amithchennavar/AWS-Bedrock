import re
import matplotlib.pyplot as plt

data = [
    'Based on the search results, the minimum time taken for each type of order is:',
    '',
    'Snack order: 17 minutes (source 1)',
    'Buffet order: 25 minutes (source 2)',
    'Drinks order: 41 minutes (source 2)',
    'Meal order: 21 minutes (source 2)'
]

# Extract order types and their corresponding minimum time taken
order_types = []
time_taken = []

for line in data[2:]:
    match = re.search(r'(\w+)\sorder:\s+(\d+)\s+minutes', line)
    if match:
        order_type = match.group(1)
        time = int(match.group(2))
        order_types.append(order_type)
        time_taken.append(time)

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(order_types, time_taken, color='lightgreen')
plt.xlabel('Order Type')
plt.ylabel('Minimum Time Taken (minutes)')
plt.title('Minimum Time Taken for Each Type of Order')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
