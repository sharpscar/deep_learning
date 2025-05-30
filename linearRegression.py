import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#모든 컴퓨터에서 결과가 같게 나오도록 하기위해서 seed를 고정
np.random.seed(0)

#0~1사이를 10등분하여 만든 배열을 생성
x = np.linspace(0,2,10)
y = np.linspace(0,2,10)
print("xy 0~1사이를 10등분하여 만든 배열을 생성")
print(x,y)
#x에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성
x = x +np.random.normal(0., 0.01, 10)
#y에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성
y = y + np.random.normal(0., 0.01, 10)
print("#x에 오차를 주기 위해서 정규분포를 이용하여 10 길이만큼 생성")
print(x,y)

