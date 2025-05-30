import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#모든 컴퓨터에서 결과가 같게 나오도록 하기위해서 seed를 고정
np.random.seed(0)

#0~1사이를 10등분하여 만든 배열을 생성
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
# print("xy 0~1사이를 10등분하여 만든 배열을 생성")
# print(x,y)
#x에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성
x = x +np.random.normal(0., 0.1, 100)
#y에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성
y = y + np.random.normal(0., 0.1, 100)
# print("#x에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성")
# print(x,y)

#x의 차원을 추가하여 x와 y가 1:1로 매칭되도록 만든다
x = np.expand_dims(x, axis=1)

#선형 회귀 모델을 생성한다.
model = linear_model.LinearRegression()
#선형회귀 모델에 데이터와 정답을 주어 이에 맞게 모델을 맞춘다 (fit)
model.fit(x,y)

#선형회귀 중 1차 함수에 해당하기 때문에 1차함수의 기울기를 구할수 있다.
#이 수치는 나중에 시각화에 사용될 것이다.
# print(model.coef_)

# 맞춰진 모델을 이용하여 3을 예측하도록 한다.
# print(model.predict([[3]]))

# 실제 데이터들을 점분포도로 그림
plt.scatter(x,y)
plt.show()

#데이터들로 학습하여 만들어진 model로 그릴수 있는 1차함수
x_ = np.linspace(-2,2,100)
plt.plot(x_, model.coef_ * x_, color = "r")
plt.show()

#점 분포도와 1차 함수를 동시에 출력
plt.scatter(x,y)
plt.plot(x_, model.coef_ * x_, color="r")
plt.show()