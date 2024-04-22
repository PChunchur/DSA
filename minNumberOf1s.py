#Min number of 1's in a row
#April 22
#The essence of this problem is to find the row with the minimum number of 1's in a matrix.
#We take two approaches 
# 1 - create an empty list and append the number of 1's in each row. Return the minimum number of 1's in the list.
# 2 - We initialize two variables min_count and min_index to infinity and -1 respectively. 
# 2 We iterate through the matrix and sum the number of 1's in each row.

class Solution:
    def minRow(self,n,m,a):
        num = []
        
        for i in range(n):
            count = 0
            
            for j in range(m):
                if a[i][j] != 0:
                    count+= 1
            if count>0:
                num.append(count)
            
            
        return min(num) if num else 1
    
    
    
class Solution2:
    def minRow(self,n,m,a):
        min_count = float('inf')
        min_index = -1
        
        for i in range(n):
            count = sum(a[i])
            
            if count < min_count:
                min_count = count
                min_index = i
                
        return min_index+1 if min_index != -1 else 1