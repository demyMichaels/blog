import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data for risk and return
risk = np.array([1, 2, 3, 4, 5, 6])
return_ = np.array([1.5, 1.7, 3.0, 2.5, 3.5, 4.0])

# Reshape data for sklearn LinearRegression
risk_reshaped = risk.reshape(-1, 1)

# Create linear regression model and fit to data
model = LinearRegression()
model.fit(risk_reshaped, return_)

# Predict returns using the model
predicted_return = model.predict(risk_reshaped)

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(risk, return_, color='orange')

# Plotting the regression line
plt.plot(risk, predicted_return, color='blue', linestyle='--')

# Adding annotations
plt.text(2, 3.5, 'Positive\nrisk-adjusted\nreturn', fontsize=10, ha='center')
plt.text(4, 2.0, 'Negative\nrisk-adjusted\nreturn', fontsize=10, ha='center')


# Adding labels and title
plt.xlabel('Risk', color='brown')
plt.ylabel('Return', color='brown')
plt.title('The risk and return relationship')

# Adding grid for better visualization
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('risk_return_relationship.png', format='png', dpi=300)

# Show the plot
plt.show()