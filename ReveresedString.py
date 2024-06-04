# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. 
# Do not include any extra spaces.


# APPROACH 1 

class Solution:
    def reversedWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
    
    
    
    
    
# APPROACH 2
class Sol1:
    def reversedWords(self, s: str) -> str:
        x = s.split()
        return " ".join(x[::-1])
    
    
# Approach 3

class Sol2: 
    def reversedWords(self, s: str) -> str:
        result = ""
        i = 0
        n = len(s)
        
        while i<n:
            while i < n and s[i] == " ":
                if i>=n:
                    break
                j = i+1 
                
            while j<n and s[j] != " ":
                j += 1
                
            sub = s[i:j]
            
            if len(result) != 0:
                result = sub + " " + result
                
            else: 
                result = sub
                i = j + 1
                
        return result 
    