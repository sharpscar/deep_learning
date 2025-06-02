import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np
import keras
from keras import layers, optimizers

keras.utils.set_random_seed(0)

load_data = load_diabetes()
x= load_data.data
y = load_data.target  #당뇨병 진행 정도
size = x.shape


model = keras.Sequential([
    layers.Dense(units=1, input_shape=(size[1],), activation="relu"),
    layers.Dense(units=256, activation="relu"),
    layers.Dense(units=1),
])


model.compile(optimizer="Adam", loss="mse")
history = model.fit(x,y,epochs=100)

history_ = history.history

plt.plot(history_['loss'])
plt.show()

print(load_data.DESCR)