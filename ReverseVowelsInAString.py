# Reversing a string, where the vowels positions are reversed but the consonants stay the same 


# *LOGIC*
# We are going to use a two pointer approach 
# We will have a left pointer and a right pointer, and we will keep moving them towards each other
# We will swap the vowels at the left and right pointers, and then move the pointers towards each other
# We will keep doing this until the left pointer is less than the right pointer

class Solution:
    def ReverseVowels(self, s: str) -> str:
        i = 0 
        j = len(s) - 1
        s = list(s)     #String is immutable,
                        #convert to list which is mutable (Mutable means values can be)
        vowels = set('aieouAEIOU')
        
        while i < j :
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]  # Here we swap the vowels 
                i += 1
                j -= 1
            
            elif s[i] not in vowels:
                i += 1
                
            elif s[j] not in vowels:
                j -= 1
                
        return ''.join(s)   # Convert the list back to a string and return it
    
n = input("Enter the string: ")
print(Solution().ReverseVowels(n))