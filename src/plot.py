import matplotlib.pyplot as plt
import numpy as np

# Data
products = ["Acer Nitro 5", "Samsung Galaxy S21", "LG OLED55CXPUA", "Sony Bravia X900H"]
dates = ["2024-07-03", "2024-07-15", "2024-07-22", "2024-07-23"]

# Number of issues for each product on each date
data = {
    "Acer Nitro 5": [1, 0, 0, 0],
    "Samsung Galaxy S21": [0, 1, 0, 0],
    "LG OLED55CXPUA": [0, 1, 1, 0],
    "Sony Bravia X900H": [0, 0, 0, 1]
}

# Plotting
x = np.arange(len(dates))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
bars = []
for i, product in enumerate(products):
    bars.append(ax.bar(x + i * width, data[product], width, label=product))

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Date')
ax.set_ylabel('Number of Issues')
ax.set_title('Number of Issues Reported for Each Product Over Time')
ax.set_xticks(x + width * (len(products) / 2 - 0.5))
ax.set_xticklabels(dates)
ax.legend()

plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.tight_layout()

plt.savefig('issues_by_product.png', format='png')
plt.show()