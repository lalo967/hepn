import numpy as np

a = [1,2,3]
c = [4,5,6]
e= np.append(a,c)
b = np.array(e).reshape((1,6))
np.savetxt('a.txt',b,fmt='%d')
