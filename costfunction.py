import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("advertising.csv")

x = np.array(df["TV"])
y = np.array(df["Sales"])
bestw=0
best_cost=float("inf")
best_w = 0
best_b = 0
best_cost = float("inf")

for w in np.arange(0, 0.2, 0.001):
    for b in np.arange(0, 10, 0.1):
        y_pred = w*x + b
        cost = (1/(2*len(x))) * np.sum((y_pred - y)**2)
        if cost < best_cost:
            best_cost = cost
            best_w = w
            best_b = b
print(best_w)
print(best_b)
print(best_cost)
plt.scatter(x, y)
plt.xlabel("TV")
plt.ylabel("Sales")
y_pred = (best_w * x)+ best_b
plt.plot(x,y_pred)
plt.show()
