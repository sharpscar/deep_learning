
import keras
from keras import layers

model = keras.Sequential([
    layers.Dense(16, input_shape=(16,16), activation = "sigmoid"),
    layers.Dense(128,activation = "sigmoid"),
    layers.Dense(512,activation = "sigmoid"),
    layers.Dense(10, activation = "softmax"),

])

model.summary()

'''
즉, 이 모델은 16개의 시퀀스를 처리하며, 각각의 시퀀스에 대해 벡터 연산을 수행하는 구조입니다.

이 모델은 시퀀스 데이터 (ex. 문장, 시계열 등)를 입력으로 받아 다층 퍼셉트론(DNN) 형태로 처리하는 구조입니다.

출력이 10개 클래스이므로, 아마 분류 모델일 가능성이 높습니다 (예: 숫자 인식, 감정 분류 등).

각 Dense 층은 시퀀스의 각 타임스텝에 독립적으로 적용됩니다.
'''