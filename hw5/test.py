import pandas as pd
import matplotlib.pyplot as plt

# Example Series
data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

# Get the counts of unique values
counts = data.value_counts()

# Plot the bar graph
plt.bar(counts.index, counts.values)

# Add labels and title
plt.xlabel('Items')  # x-axis: unique items (e.g., 'apple', 'banana', etc.)
plt.ylabel('Counts')  # y-axis: frequency of each item
plt.title('Item Frequency')

# Rotate x-axis labels for better readability (if necessary)
plt.xticks(rotation=45)

# Show the plot
plt.show()
