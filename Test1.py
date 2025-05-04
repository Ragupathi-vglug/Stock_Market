import pandas as pd
import matplotlib.pyplot as plt

# Load and clean dataset
df = pd.read_csv("data.csv")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
price_columns = ['Close/Last', 'Open', 'High', 'Low']
for col in price_columns:
    df[col] = df[col].replace({'\$': ''}, regex=True).astype(float)

# Ensure sorting by date
df.sort_values(by=['Company', 'Date'], inplace=True)

# Get latest closing price per company
latest_prices = df.groupby('Company').last()['Close/Last']

# Bar chart of latest closing prices
plt.figure(figsize=(10, 6))
bars = plt.bar(latest_prices.index, latest_prices.values, color='mediumseagreen')
plt.title("Latest Closing Price by Company")
plt.xlabel("Company")
plt.ylabel("Closing Price ($)")
plt.grid(axis='y')

# Add value labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Average trading volume per company
avg_volume = df.groupby('Company')['Volume'].mean()

# Bar chart of average trading volumes
plt.figure(figsize=(10, 6))
bars = plt.bar(avg_volume.index, avg_volume.values, color='cornflowerblue')
plt.title("Average Trading Volume by Company")
plt.xlabel("Company")
plt.ylabel("Average Volume")
plt.grid(axis='y')

# Add value labels on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1000000, f"{yval:.0f}", ha='center', va='bottom')

plt.tight_layout()
plt.show(block=True)

