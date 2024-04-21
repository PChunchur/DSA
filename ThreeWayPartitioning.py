#The essence of the problem is to partition the array into three parts: less than a, in  between a and b, and greater than b.
# We use two pointers l and r, where l points to the first element and r points to the last element. 
# We iterate through the array and swap the elements with the l-th element if the element is less than a, and with the r-th element if the element is greater than b.
# We stop when the l-th element is greater than the r-th element.
#April 21

def swap(array,i,j):
    temp = array[l]
    array[l] = array[r]
    array[r] = temp

def threeWayPartition(self,array,a,b):
    l = 0
    r = len(array) -1
    i =0
    
    while i<= r:
        if array[i] < a:
            swap(array,l,r)
            l += 1
            i += 1
        elif array[i] > b:
            swap(array,i,r)
            r -= 1
            
        else:
            i+=1