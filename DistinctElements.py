# Printing Distinct Elements of a union of two arrays 
# eg: arr1 = [1, 2, 3, 4, 5], arr2 = [3, 4, 5, 6, 7] -> Output must be [1, 2, 3, 4, 5, 6, 7]

def distinctElements(arr1, arr2):
    arr3 = arr1 + arr2
    arr3.sort()
    set_3 = set(arr3)
    return sorted(set_3)



arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(distinctElements(arr1, arr2))