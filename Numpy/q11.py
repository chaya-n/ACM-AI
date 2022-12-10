import numpy as np
import random
cartesian= np.random.random((10,2))
polar=np.zeros((10,2))
for i in range(10):
    x,y=cartesian[i,0] ,cartesian[i,1]
    polar[i,0]=np.sqrt(x**2+y**2)
    polar[i,1]=np.arctan2(y,x)
print(polar)
