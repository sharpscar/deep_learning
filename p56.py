import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from itertools import islice


import pandas as pd
df = pd.read_csv("/home/scar/Downloads/seoul.csv", encoding='cp949')

# print(df.columns)
x = df[df.columns[0]]

x = pd.to_datetime(x)
print(x) # x는 날짜를 뽑아온다.
target = df.columns[-2:]
low = df[target[0]]         # 최저기온을  리스트에 담아서 가져온다.
high = df[target[1]]        # 최고기온을 리스트에 담아서 가져온다.

plt.plot(x, low.values, color="b", label="Low")         #플로트에 X 최저 값 , 파란색으로
plt.plot(x, high.values, color="r", label="High")       #플로트에 x 최고 값  빨간색으로
plt.legend()
plt.show()      #출력한다. 

# for i, row in islice(df.iterrows(),5):
#     # 최고 기온과 최저 기온값이 존재한다면
#     if row[-1] != '' and row[-2] :
#         if 1983
#     print(row[0], row[1], row[2],row[3], row[4])

# 더벤티 / 메가 / 이디야?