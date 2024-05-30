#Remove duplicates in a sorted array 
# leetcode 26 

# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#IN PLACE MEANS YOU CAN'T USE ANOTHER ARRAY TO STORE THE VALUES

#First initialise two pointers L and R at index 1
#comapre right pointer value to previous value, if same then move right pointer ahead
#If different then move left pointer ahead and copy the value of right pointer to left pointer
#Return index of Left Pointer

def removeDuplicates(self, nums: List[int]) -> int:
    l = 1
    for r in range(1, len(nums)):  # r is the right pointer, range between 1 to last element
        if nums[r] != nums[r-1]:  # Check if right pointer is not equal to left pointer
            nums[l] = nums[r]     #Assing value of right pointer to left pointer
            l += 1  #move the left pointer ahead
    return l 