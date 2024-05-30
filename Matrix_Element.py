import numpy as np
def matrixElement(self,n):
    
    a = [1,1],[1,0]
    b = [1,1],[1,0]
    position = 1
    
    for i in range(n):
        b = np.dot(a,b)
        position =  b[1,0] % 1000000007 
        
    return position  


n = 3
matrixElement(n)