import numpy as np

a = [1,2,3]    
b = np.array(a).reshape((1,3))    
np.savetxt('a.txt',b,fmt='%d')
