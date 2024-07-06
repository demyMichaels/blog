import matplotlib.pyplot as plt
import numpy as np

# Data
risk = [5.0, 10.0, 15.0, 15.0, 20.0, 25.0] 
return_values = [6.5, 7.0, 11.0, 13.0, 15.0, 19.0]
labels = ["Smoothed average", "Adjusted growth", "Large-cap L-T growth", "Large-cap L-T consumer", "Sector concentration", "Small cap"]

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(risk, return_values)

for i, label in enumerate(labels):
    plt.annotate(label, (risk[i], return_values[i]))

plt.xlabel("Risk, standard deviation (%)")
plt.ylabel("Return (%)")
plt.title("Risk-return profile")
plt.grid(True)

# Save the plot as an image file
plt.savefig("risk_return_profile.png", dpi=300)
plt.show()