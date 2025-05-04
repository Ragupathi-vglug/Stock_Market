import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data - Replace this with your actual stock closing price data
# Example format: df = pd.read_csv("your_data.csv", index_col="Date", parse_dates=True)
# Each column should be a company's closing price
data = {
    'Apple': [150, 152, 154, 155, 153],
    'Google': [2800, 2825, 2810, 2830, 2840],
    'Amazon': [3400, 3420, 3415, 3430, 3440],
    'Tesla': [700, 710, 705, 720, 725]
}
df = pd.DataFrame(data)

# 1. Calculate the correlation matrix
correlation_matrix = df.corr()

# 2. Print the correlation matrix
print("Correlation Matrix:\n", correlation_matrix)

# 3. Visualize the correlation matrix using matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(correlation_matrix, cmap='coolwarm')

# Add color bar
plt.colorbar(cax)

# Set axis ticks and labels
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha="left")
ax.set_yticklabels(correlation_matrix.columns)

# Annotate each cell with the correlation coefficient
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        value = correlation_matrix.iloc[i, j]
        ax.text(j, i, f"{value:.2f}", va='center', ha='center', color='black')

plt.title("Correlation Matrix of Closing Prices", pad=20)
plt.tight_layout()
plt.show()
