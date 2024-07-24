import matplotlib.pyplot as plt
import numpy as np

# Data
dates = ["2024-07-03", "2024-07-15", "2024-07-22", "2024-07-23"]
products = ["Acer Nitro 5", "Samsung Galaxy S21", "LG OLED55CXPUA", "Sony Bravia X900H"]

# Number of issues reported for each product on each date
issues = {
    "2024-07-03": [1, 0, 0, 0],
    "2024-07-15": [0, 1, 2, 0],
    "2024-07-22": [0, 0, 1, 0],
    "2024-07-23": [0, 0, 0, 1]
}

# Convert issues to a format suitable for plotting
issue_counts = np.array([issues[date] for date in dates])
n_products = len(products)
bar_width = 0.2
index = np.arange(n_products)

# Plotting
plt.figure(figsize=(14, 8))

for i, date in enumerate(dates):
    plt.bar(index + i * bar_width, issue_counts[i], bar_width, label=date)

# Add titles and labels
plt.title('Number of Issues Reported for Each Product by Date')
plt.xlabel('Product')
plt.ylabel('Number of Issues')
plt.xticks(index + bar_width * (len(dates) / 2 - 0.5), products, rotation=45)
plt.legend(title='Date')
plt.grid(True)

# Save the plot as an image file
plt.savefig('grouped_bar_chart_issues.png', format='png')  # Save the plot

# Show the plot
plt.show()