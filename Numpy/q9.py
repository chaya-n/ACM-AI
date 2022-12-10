import numpy as np
import random
a=np.random.randint(26,size=(3, 3))
b=np.random.randint(26,size=(3,3))
output=[]
for i in range(3):
    for j in range(3):
        if(a[i,j] in b):
            output.append(a[i,j])
print(a)
print(b)
print("This is the Output : ",output)