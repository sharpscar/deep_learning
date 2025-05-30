import pandas as pd
import matplotlib.pyplot as plt

# 모든 행을 출력하도록 설정
pd.set_option('display.max_rows', None)

# 모든 컬럼을 출력하도록 설정
pd.set_option('display.max_columns', None)
result = []

name = input("찾고싶은 지역의 이름을 알려주세요 : " )
df = pd.read_csv("/home/scar/Downloads/gender.csv", encoding='cp949')

for index ,row in df.iterrows():
    if  name in row[0]:
        for i in range(3,104):
            result.append(int(row[i])-int(row[i+103]))

print(len(result))


plt.bar(range(100), result[:100])
plt.show()