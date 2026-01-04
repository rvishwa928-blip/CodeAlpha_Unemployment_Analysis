# ==========================================
# Unemployment Analysis with Python
# (Auto CSV Creation)
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------------------
# 0. Auto-create CSV if not exists
# ------------------------------------------
csv_file = "unemployment.csv"

if not os.path.exists(csv_file):
    print("CSV file not found. Creating unemployment.csv automatically...")

    data = {
        "Date": pd.date_range(start="2019-01-01", periods=36, freq="M"),
        "Region": ["India"] * 36,
        "Unemployment_Rate": [
            6.1, 6.0, 6.2, 6.3, 6.5, 6.7,
            7.0, 7.2, 7.5, 7.8, 8.0, 8.2,
            9.5, 10.2, 11.0, 12.5, 13.8, 14.0,
            12.0, 11.5, 10.8, 9.9, 9.0, 8.5,
            7.8, 7.5, 7.2, 7.0, 6.8, 6.6,
            6.4, 6.3, 6.2, 6.1, 6.0, 5.9
        ]
    }

    df_auto = pd.DataFrame(data)
    df_auto.to_csv(csv_file, index=False)

    print("unemployment.csv created successfully!\n")

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------
df = pd.read_csv(csv_file)

# ------------------------------------------
# 2. Data Cleaning
# ------------------------------------------
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)

print("Dataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# ------------------------------------------
# 3. Exploratory Data Analysis (EDA)
# ------------------------------------------
print("\nStatistical Summary:")
print(df['Unemployment_Rate'].describe())

# Overall unemployment trend
plt.figure()
sns.lineplot(x='Date', y='Unemployment_Rate', data=df)
plt.title("Overall Unemployment Rate Trend")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ------------------------------------------
# 4. Covid-19 Impact Analysis
# ------------------------------------------
covid_start = "2020-03-01"

pre_covid = df[df['Date'] < covid_start]
post_covid = df[df['Date'] >= covid_start]

print("\nAverage Unemployment Rate (Pre-Covid):",
      pre_covid['Unemployment_Rate'].mean())

print("Average Unemployment Rate (Post-Covid):",
      post_covid['Unemployment_Rate'].mean())

# Comparison Plot
plt.figure()
sns.lineplot(x='Date', y='Unemployment_Rate', data=pre_covid, label="Pre-Covid")
sns.lineplot(x='Date', y='Unemployment_Rate', data=post_covid, label="Post-Covid")
plt.title("Impact of Covid-19 on Unemployment")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.legend()
plt.show()

# ------------------------------------------
# 5. Seasonal Trend Analysis
# ------------------------------------------
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_avg = df.groupby('Month')['Unemployment_Rate'].mean()

plt.figure()
monthly_avg.plot(kind='bar')
plt.title("Average Monthly Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ------------------------------------------
# 6. Region-wise Analysis
# ------------------------------------------
plt.figure(figsize=(10,5))
sns.boxplot(x='Region', y='Unemployment_Rate', data=df)
plt.title("Region-wise Unemployment Distribution")
plt.xticks(rotation=45)
plt.show()

# ------------------------------------------
# 7. Key Insights Extraction
# ------------------------------------------
highest_month = monthly_avg.idxmax()
lowest_month = monthly_avg.idxmin()

print("\nHighest unemployment observed in month:", highest_month)
print("Lowest unemployment observed in month:", lowest_month)
