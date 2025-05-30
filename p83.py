import matplotlib.pyplot as plt


import pandas as pd
df = pd.read_csv("/home/scar/Downloads/seoul.csv", encoding='cp949')
target = df.columns[-2:]

# x = df[df.columns[0]]
# x =  pd.to_datetime(x)
# high = df[target[1]]

#

df['날짜'] = pd.to_datetime(df['날짜'])
aug_rows = df[df.iloc[:,0].dt.month==8]
jan_rows = df[df.iloc[:,0].dt.month==11]

plt.hist(aug_rows[df.columns[-1]], bins=100, color='r', label='Aug')
plt.hist(jan_rows[df.columns[-1]], bins=100, color='b', label='Jan')
plt.legend()
plt.show()


