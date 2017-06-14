import numpy as np 
a1=np.ones((4,4))
a1[2,3]=2
a1[3,1]=6

a2=np.zeros((5,5))
for i in range(0,6):
	for j in range(0,6):
		if i==j:
			a2[i-1,j-1]=i
#print(a1)
#print(a2)

a3=np.zeros((16,1))
a3[0]=a3[1]=1
for i in range(2,16):
	a3[i]=a3[i-1]+a3[i-2]

a4=np.zeros((16,64))
for i in range(0,64):
	for j in range(0,16):
		a4[j,i]=a3[j]

a4_even=[]
for i in range(0,16):
	for j in range(0,64):
		if a4[i,j]/2.0==int(a4[i,j]/2):
			a4_even.append(a4[i,j])
#print(a4_even)

arandom=np.random.uniform(2,16,10)

arandom_int=arandom.astype(int)


#b=arandom_int<10 
b=np.all(((arandom_int%2)==0,arandom_int<10,arandom_int>5),axis=0)
a5=arandom_int[b]
print(arandom_int)
print(a5)
