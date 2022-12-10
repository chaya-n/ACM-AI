import numpy as np
import random
a=np.random.randint(26,size=(3, 3))
for i in range(3):
    for j in range(3):
        print(a[i,j], end ="\t")
    print()