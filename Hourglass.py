#Maximum sum of an hourglass 
#April 25

def max_sum(self,n,m,mat):
    current_sum = -1
    
    if n<2 and m<2:
        return -1
    
    else:
        for i in range(n-2):
            for j in range(m-2):
                
                hourglass_sum = ((mat[i][j] + mat[i][j+1] + mat[i][j+2]) + mat[i+1][j+1] (mat[i+2][j] + mat[i+2][j+1] + mat[i+1][j+2]))
                
                current_sum = max(hourglass_sum, current_sum)
                
        return current_sum
                
                
    