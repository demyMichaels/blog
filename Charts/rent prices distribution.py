import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Generating random data to simulate rent prices
np.random.seed(42)
data = np.random.normal(loc=1500, scale=30, size=1000)

# Plotting the histogram
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=False, stat="density", color='gray')

# Adding statistical annotations
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=False)[0]
std_dev = np.std(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Fill between the histograms
plt.fill_betweenx([0, 0.014], mean - std_dev, mean + std_dev, alpha=0.2, color='brown', label='Std Dev')
plt.axvline(mean, color='red', linestyle='--', linewidth=1, label='Mean')
plt.axvline(median, color='blue', linestyle='--', linewidth=1, label='Median')

# Plot lines for 5% and 95% percentiles
percentile_5 = np.percentile(data, 5)
percentile_95 = np.percentile(data, 95)
plt.axvline(percentile_5, color='purple', linestyle='--', linewidth=1, label='5%')
plt.axvline(percentile_95, color='purple', linestyle='--', linewidth=1, label='95%')

# Adding text box with statistics
textstr = '\n'.join((
    f'Minimum: ${np.min(data):.2f}',
    f'Maximum: ${np.max(data):.2f}',
    f'Mean: ${mean:.2f}',
    f'Median: ${median:.2f}',
    f'Mode: ${mode:.2f}',
    f'Stddev: ${std_dev:.2f}',
    f'Skewness: {skewness:.2f}',
    f'Kurtosis: {kurtosis:.2f}',
    f'10%: ${np.percentile(data, 10):.2f}',
    f'25%: ${np.percentile(data, 25):.2f}',
    f'70%: ${np.percentile(data, 70):.2f}',
    f'90%: ${np.percentile(data, 90):.2f}',
    f'Values: {len(data)}'
))

# These are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Place a text box in upper right in axes coords
plt.text(0.95, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

# Adding labels and legend
plt.xlabel('Rent Prices ($)')
plt.ylabel('Density')
plt.legend(loc='upper right')
plt.title('Rent Prices Distribution')

# Save the plot as a PNG file
plt.savefig('rent_prices_distribution.png', format='png', dpi=300)

# Show the plot
plt.show()