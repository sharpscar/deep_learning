import matplotlib.pyplot as plt

import random
result = []
import pandas as pd

df = pd.read_csv("/home/scar/Downloads/seoul.csv", encoding='cp949')

x = df[df.columns[0]]  #날짜

target = df.columns[-2:]

low = df[target[0]]
high = df[target[1]]

df['날짜'] = pd.to_datetime(df['날짜'])
aug_rows = df[df.iloc[:,0].dt.month==8]
jan_rows = df[df.iloc[:,0].dt.month==1]




years = aug_rows['날짜'].dt.year
years_clean = years.dropna().values
print(years_clean)
plt.boxplot(years_clean)
# plt.boxplot(jan_rows)
plt.show()


#
# plt.boxplot(target)
# plt.show()

# for i in range(13) :
#     result.append(random.randint(1,1000))
#
# print(sorted(result))
#
# plt.boxplot(result)
# plt.show()