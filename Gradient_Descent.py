import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("advertising.csv")
x_train=df["Radio"].values
y_train=df["Sales"].values
def gradient_descent(x, y, w, b, alpha, iterations):
    m = len(x)
    for _ in range(iterations):
        dj_dw = 0
        dj_db = 0
        for i in range(m):
            prediction = w*x[i] + b
            error = prediction - y[i]
            dj_dw += error * x[i]
            dj_db += error
        dj_dw = dj_dw / m
        dj_db = dj_db / m
        w = w - alpha*dj_dw
        b = b - alpha*dj_db
    return w, b
w,b=gradient_descent(x_train,y_train,0,0,0.0001,10000)
pred=w*x_train+b
plt.scatter(x_train, y_train, s=10, c="red")
plt.plot(x_train, pred, c="blue")
plt.show()
print(w)
print(b)
