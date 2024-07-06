import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
categories = [
    'Stocks', 'Real Estate', 'ETFs', 'Bonds',
    'Cash', 'Futures', 'Cryptos', 'CFDs', 'Art', 'Precious Metals', 'Commodities'
]

demy = [1, 2, 4, 4, 3, 2, 3, 2, 3, 4, 1]
favour = [4, 3, 4, 3, 4, 5, 3, 2, 3, 5, 4]

# Create a DataFrame
data = pd.DataFrame({
    'Category': categories,
    'Demy': demy,
    'Favour': favour
})

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(data['Category'], data['Demy'], label=" “Demy” Strategy", linestyle='--', marker='o', color='gray')
ax.plot(data['Category'], data['Favour'], label=" “Favour” Strategy", linestyle='-', marker='o', color='limegreen')

# Adding titles and labels
ax.set_title('EFS: Comparison of Demy and Favour Asset Allocation', fontsize=16)
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# Rotate category labels for better readability
plt.xticks(rotation=45, ha='right')

# Adding grid
ax.grid(True, linestyle='--', alpha=0.6)

# Adding legend
ax.legend()

# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()

# Save the plot as an image file
plt.savefig('Demy vs Favour Assets.png')

# Show the plot (optional, will work if running in a suitable environment)
plt.show()

# Display the adjusted data
print(data)
