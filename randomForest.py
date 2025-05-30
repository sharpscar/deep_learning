import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import accuracy_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)  # 모든 열 출력


# 모든 컴터에서 결과가 같게 나오도록 하기 위해서 ㅁSeed를 고정한다.
np.random.seed(0)

# 데ㅐ이터 불러오기
df = pd.read_csv("/home/scar/Downloads/titanic.csv", encoding="cp949")
# print(df)

#데이터 전처리
#데이터 필터리링 (필요한 속성만 분리함)
features = ["Pclass", "Sex", "Age", "Fare", "Embarked"]
train  =df[features + ["Survived"]]

#결측치에 해당하는 Row 제거 - 컬럼이 비어있는 놈은 제거해라!
train = train.dropna(axis=0)

train["Sex"] = df["Sex"].map({"male": 0 , "female":1})
train["Embarked"] = df["Embarked"].map({"Q":0, "S": 1, "C":2})

#데이터 전처리 완료된 데이터를 데이터와 목표로 분리
x = train[features]
y= train["Survived"]

#학습에 사용할 train-test 데이터셋으로 나눔
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, shuffle=True)

#Random Forest 객체 생성
model = RandomForestClassifier(n_estimators=5)
model.fit(x_train, y_train)


# 학습된 모델로 Test 데이터 예측
pred = model.predict(x_test)
#  실제 데이터와 예측 데이터를 비교하여 모델의 성능을 측정
acc = accuracy_score(y_test, pred)
print(acc)
