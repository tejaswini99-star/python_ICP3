import numpy as np
Z = np.random.random_integers(1, 20, 15)
print(Z)
x = Z.reshape((3,5))
print(x)
y = np.where(x == np.amax(x, axis=1, keepdims=True), 0, x)
print("After replacing  the max in each row by 0")
print(y)