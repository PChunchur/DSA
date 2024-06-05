# to find if a string s is a valid anagram of string t 
# An anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
# eg: s = "anagram", t = "nagaram", return true



# Approach 1: Hash 
# Time Complexity: O(n)
# Cover all edge cases 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                            # if the length of the strings are not equal
            return False                                # then it means that strings are not same, hence false
        
        countS, countT = {} , {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1        # get the count of each character in the string s
            countT[t[i]] = countT.get(t[i],0) + 1
            
            for j in countS:
                if countS[j] != countT.getchar(j,0):
                    return False
                
            return True
        
        
        
        
# Approach 2: Sorting

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    
    
# Approach 3: Counter

import collections

class Solution: 
    def isAnagram(self, s: str, t: str)-> bool:
        return collections.Counter(s) == collections.Counter(t)
    
    
            