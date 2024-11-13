import pandas as pd
import matplotlib.pyplot as plt




dataset =  'states (1).csv'
data = pd.read_csv(dataset)

data['Uninsured Rate (2010)'] = data['Uninsured Rate (2010)'].str.rstrip('%').astype(float)
data['Uninsured Rate (2015)'] = data['Uninsured Rate (2015)'].str.rstrip('%').astype(float)

data_2010_sorted = data.sort_values('Uninsured Rate (2010)')
data_2015_sorted = data.sort_values('Uninsured Rate (2015)')

plt.figure(figsize=(18,12))

y_min_2010 = 0
y_max_2010 = 20

y_min_2015 = 0
y_max_2015 = 15


plt.subplot(2,1,1)
plt.bar(data_2010_sorted['State'], data_2010_sorted['Uninsured Rate (2010)'], color ='skyblue')
plt.title('Uninsured Rate by State (2010)', fontsize = 20)
plt.xlabel('State', fontsize = 14)
plt.ylabel('Uninsured Rate (%)', fontsize = 14)
plt.ylim(y_min_2010, y_max_2010)
plt.xticks(rotation = 90, fontsize = 8)
plt.yticks(fontsize = 8)

plt.subplot(2, 1, 2)
plt.bar(data_2015_sorted['State'], data_2015_sorted['Uninsured Rate (2015)'], color = 'lightgreen')
plt.title('Uninsured Rate by State (2015)', fontsize = 20)
plt.xlabel('State', fontsize = 14)
plt.ylabel('Uninsured Rate (%)', fontsize = 14)
plt.ylim(y_min_2015, y_max_2015)
plt.xticks(rotation = 90)

plt.tight_layout()
plt.show()