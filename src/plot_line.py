import matplotlib.pyplot as plt

# Data
dates = ["2024-07-03", "2024-07-15", "2024-07-22", "2024-07-23"]
num_issues = [1, 3, 2, 1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dates, num_issues, marker='o', linestyle='-', color='b', label='Number of Issues')

# Add titles and labels
plt.title('Number of Issues Reported Datewise')
plt.xlabel('Date')
plt.ylabel('Number of Issues')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.grid(True)
plt.legend()

# Save the plot as an image file
plt.savefig('issues_datewise.png', format='png')  # Save the plot

# Show the plot
plt.show()
