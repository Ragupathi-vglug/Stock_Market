import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['Close/Last']=df['Close/Last'].replace({'\$': ''}, regex=True).astype(float)
price_change=df.groupby("Company").agg(
    Start_Price=("Close/Last","first"),
    End_Price=("Close/Last","last"),
    Avg_Volume=("Volume","mean"))

price_change["Price_Growth (%)"]=((price_change["End_Price"] - price_change["Start_Price"]) / price_change["Start_Price"]) * 100
top_price_growth=price_change.sort_values(by="Price_Growth (%)", ascending=False)
top_trading_volume = price_change.sort_values(by="Avg_Volume", ascending=False)
# Display top 5 companies in each category
print("Top 5 Companies by Stock Price Growth:")
print(top_price_growth.head())
print("\nTop 5 Companies by Trading Volume:")
print(top_trading_volume.head())
# Plot top 5 price growth companies
plt.figure(figsize=(10, 5))
plt.bar(top_price_growth.index[:5], top_price_growth["Price_Growth (%)"][:5], color='green')
plt.title("Top 5 Companies by Stock Price Growth")
plt.ylabel("Growth (%)")
plt.xlabel("Company")
plt.xticks(rotation=45)
plt.show()
# Plot top 5 trading volume companies
plt.figure(figsize=(10,5))
plt.bar(top_trading_volume.index[:5], top_trading_volume["Avg_Volume"][:5], color='blue')
plt.title("Top 5 Companies by Trading Volume")
plt.ylabel("Average Volume")
plt.xlabel("Company")
plt.xticks(rotation=45)
plt.show()
