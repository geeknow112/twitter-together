import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)

f = open('./tweets/baby-step.tweet', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

