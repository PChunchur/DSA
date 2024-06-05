# Given a array of integers and a target og type int, 
# Find the two numbers that add up to the target 
# retun their indices 
# eg arr = [2,7,11,15], target = 9
# output -> [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        in_map = {}
        
        for i,nums in enumerate(nums):
            complement = target - nums      # 7 = 9-2
            if complement in in_map:
                return [in_map[complement], i ]
            
            in_map[nums] = i 
            
        return []
    
# this is a dictionary based approachs
            