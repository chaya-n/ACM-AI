import numpy as np
import random
a=np.random.randint(11,size=(3,2))
b=np.random.randint(11,size=(2,3))
print(a)
print('-----')
print(b)
print('-----')
print(a+b.T)