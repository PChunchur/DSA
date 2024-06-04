# Here Given two strings s1,s2, check if s2 is a rotated version of s1.
# Example: For s1 = "programming" and s2 = "ingprogram", the output should be True.
# Example: For s1 = "programming" and s2 = "ingpro", the output should be False.
# Roatation is unidirectional 

class Solution:
    def isRotation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s3 = s1+s1
        
        return goal in s3