import numpy as np 
a1=np.ones((4,4))
a1[2,3]=2
a1[3,1]=6

a2=np.zeros((5,5))
for i in range(0,6):
	for j in range(0,6):
		if i==j:
			a2[i-1,j-1]=i
print(a1)
print(a2)