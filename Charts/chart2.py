import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Data
risk = [5.0, 10.0, 15.0, 15.0, 20.0, 25.0] 
return_values = [6.5, 7.0, 11.0, 13.0, 15.0, 19.0]
labels = ["Smoothed average", "Adjusted growth", "Large-cap L-T growth", "Large-cap L-T consumer", "Sector concentration", "Small cap"]

# Create the plot
plt.figure(figsize=(10, 6))

# Set the background gradient
cmap = plt.get_cmap('RdYlGn')
norm = plt.Normalize(vmin=min(return_values), vmax=max(return_values))
plt.imshow([[0, 1], [1, 0]], cmap=cmap, extent=(min(risk), max(risk), min(return_values), max(return_values)), aspect='auto', alpha=0.3)

# Add a subtle texture to the background
texture = plt.Rectangle((min(risk), min(return_values)), max(risk) - min(risk), max(return_values) - min(return_values), 
                        facecolor='none', edgecolor='#CCCCCC', hatch='////', linewidth=0.5)
plt.gca().add_patch(texture)

# Plot the scatter points
plt.scatter(risk, return_values, c=return_values, cmap=cmap, norm=norm)

# Add labels and annotations
for i, label in enumerate(labels):
    plt.annotate(label, (risk[i], return_values[i]), xytext=(5, 5), textcoords="offset points", 
                 bbox=dict(boxstyle="round", fc="w", ec="k", lw=1), 
                 arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.2", color="k"))

plt.xlabel("Risk, standard deviation (%)", fontsize=12, color='#333333')
plt.ylabel("Return (%)", fontsize=12, color='#333333')
plt.title("Risk-return profile", fontsize=14, color='#333333')
plt.grid(True, color='#CCCCCC')

# Save the plot as an image file
plt.savefig("risk_return_profile2.png", dpi=300)
plt.show()