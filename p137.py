import pandas as pd
import matplotlib.pyplot as plt

# 모든 행을 출력하도록 설정
pd.set_option('display.max_rows', None)

# 모든 컬럼을 출력하도록 설정
pd.set_option('display.max_columns', None)


name = input("찾고싶은 지역의 이름을 알려주세요 : " )
size = []
m = []
f = []

df = pd.read_csv("/home/scar/Downloads/gender.csv", encoding='cp949')

for index ,row in df.iterrows():

    if  name in row[0]:
        # print(row.values)
        # for num in row.values:


        for i in range(3,104):
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break




plt.rc('font', family='Malgun Gothic')
plt.plot(m, label='Male')
plt.plot(f, label='Female')
plt.legend()
plt.show()