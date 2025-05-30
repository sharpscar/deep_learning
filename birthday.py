import matplotlib.pyplot as plt
from scipy.ndimage import label
import pandas as pd

df = pd.read_csv("/home/scar/Downloads/seoul.csv", encoding='cp949')

print(df.columns)
df["날짜"] = pd.to_datetime(df["날짜"])

df = df[("1998-06-01" <= df["날짜"]) & (df["날짜"] <= "1998-06-30")]

date = df[df.columns[0]]
high = df[df.columns[-1]]
low = df[df.columns[-2]]
dot_df = df["1998-06-14" == df["날짜"]]
dot_date = dot_df[dot_df.columns[0]]
dot_high = dot_df[dot_df.columns[-1]]
dot_low = dot_df[dot_df.columns[-2]]

# print(date)
# print(high)
# print(low)

plt.title("My Birthday Temperature")

plt.scatter(dot_date, dot_high, color="r")
plt.scatter(dot_date, dot_low, color="b")
plt.plot(date, high, color="r", label="High")
plt.plot(date, low, color="b", label="Low")
plt.xticks(rotation=-20)
plt.legend()
plt.show()