# Printing the elements present in the first array but not in the second array
# eg: arr1 = [1, 2, 3, 4, 5], arr2 = [3, 4, 5, 6, 7] -> Output must be [1, 2]
#19 April

def missingElements(a,b,n,m):
    set_b = set(b)
    missing_elements = (element for element in a if element not in set_b)
    return missing_elements

a = {1,2,3,4}
b = {3,4,5,6}
n = len(a)
m = len(b)
print(missingElements(a,b,n,m))