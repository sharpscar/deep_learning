import matplotlib.pyplot as plt


import pandas as pd
df = pd.read_csv("/home/scar/Downloads/seoul.csv", encoding='cp949')

date_column = df.columns[0]
print(f"날짜 컬럼명: {date_column}")

df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

monthly_data = [df[df.iloc[:,0].dt.month==i].iloc[:,-1].dropna().values for i in range(1,13)]

# plt.boxplot(monthly_data)
# plt.xlabel('월')
# plt.ylabel('값')
# plt.show()

print(monthly_data)