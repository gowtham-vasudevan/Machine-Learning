import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('Simple LR.csv'):
  x, y = line.split(',')
  X.append(x)
  Y.append(y)
  
X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

denominator = X.dot(X) - X.mean()*X.sum()
a = (X.dot(Y) - Y.mean()*X.sum()) / denominator
b = (X.mean()*X.dot(Y) - Y.mean()*X.dot(X)) / denominator

yhat = a*X + b

plt.scatter(X, Y)
plt.plot(X, yhat, color='red')
plt.show()
