import numpy as np
import keras
from keras import layers, optimizers

keras.utils.set_random_seed(2)

inputs = np.array([
    [0,0], [0,1],[1,0],[1,1]
], dtype=np.float32)
outputs = np.array([1,0,0,0], dtype=np.float32)

model = keras.Sequential([
    layers.Dense(units=1, input_shape=(2,), activation="sigmoid"),
    layers.Dense(units=1, activation="sigmoid")
])




model.compile(optimizer="Adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(inputs, outputs, epochs=300)

# result = model.predict(inputs)
# print(result)
# #반올림을 해줘서 실제 부울린 값으로 바꿔줘야 한다.
# #인풋과 아웃풋은 2차원과 1차원의 차이가 있다 그래서 차원을 조정해줘야 한다. reshape(-1)
# print(np.round(result).reshape(-1) == outputs)

'''
시그모이드 함수는 0과 1 사이로 값을 압축하여 다음 뉴런에 전달하고, 
확률처럼 해석 가능하며, 미분 가능하다는 장점 덕분에 초기 신경망 발전에 기여했습니다.
하지만 경사 소실 문제와 0이 아닌 출력 중심 등의 단점 때문에, 
현대 딥러닝에서는 ReLU(Rectified Linear Unit)나 그 변형 함수들(Leaky ReLU, ELU 등)이 훨씬 더 많이 사용됩니다. 
하지만 이진 분류의 최종 출력층에서는 여전히 시그모이드 함수가 유용하게 사용될 수 있습니다.
'''