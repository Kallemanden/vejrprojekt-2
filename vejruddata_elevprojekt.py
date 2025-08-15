import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('vejruddata.csv')

print("Første par rækker ser sådan her ud:")
print(data.head())

data['Dato'] = pd.to_datetime(data['Dato'])
data = data.set_index('Dato')
data['Maaned'] = data.index.month

print("\nLidt generel statistik:")
print(data.describe())

temp_pr_maaned = data.groupby('Maaned')['Temp'].mean()
print("\nGennemsnitstemperatur pr måned:")
print(temp_pr_maaned)

sns.set(style="whitegrid")

plt.figure(figsize=(12,6))
plt.plot(data.index, data['Temp'], label='Temp i °C')
plt.title("Temperatur over tid")
plt.xlabel("Dato")
plt.ylabel("Temperatur")
plt.legend()
plt.show()


plt.figure(figsize=(10,5))
sns.histplot(data['Temp'], bins=20, kde=True, color='red')
plt.title("Fordeling af temperatur")
plt.xlabel("Temp")
plt.ylabel("Antal dage")
plt.show()


plt.figure(figsize=(10,6))
sns.scatterplot(x='Temp', y='Nedbor', data=data, hue='Maaned', palette='tab10')
plt.title("Temperatur vs Nedbør")
plt.xlabel("Temp")
plt.ylabel("Nedbør")
plt.show()


print("\nKorrelation mellem Temp og Nedbør:")
print(data[['Temp','Nedbor']].corr())
