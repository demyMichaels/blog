import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
categories = [
    'Price', 'Relationship management', 'Account executives', 'Corporate dealers',
    'Ease of use', 'Security', 'Accuracy', 'Speed', 'Market commentary', 'Confirmation', 'Tracking'
]

before_values = [1, 2, 4, 4, 3, 2, 3, 2, 1, 2, 1]
after_values = [4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4]

# Create a DataFrame
data = pd.DataFrame({
    'Category': categories,
    'Before': before_values,
    'After': after_values
})

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(data['Category'], data['Before'], label="EFS and Other Traditional Competitors’ “Before” Strategy", linestyle='--', marker='o', color='gray')
ax.plot(data['Category'], data['After'], label="EFS’s “After” Strategy", linestyle='-', marker='o', color='limegreen')

# Adding titles and labels
ax.set_title('EFS: Before and After', fontsize=16)
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# Rotate category labels for better readability
plt.xticks(rotation=45)

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6)

# Adding legend
ax.legend()

# Save the plot as an image file
plt.savefig('blue_ocean_strategy.png')

# Show the plot (optional, will work if running in a suitable environment)
plt.show()

# Display the adjusted data
print(data)
