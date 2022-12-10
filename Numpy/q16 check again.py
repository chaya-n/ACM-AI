import numpy as np
import random
# given_val=random.random()
# a=np.random.random((3,3))
given_val=int(input("Enter :"))
a=np.array([[1,2,3],[4,5,6],[11,12,13]])
closest=None
mini=0
for i in range(3):
    for j in range(3):
        diff=a[i,j]-given_val
        if(diff<=mini):
            closest=a[i,j]
print(closest)