'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.'''

'''Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        merged = []

        while i<len(word1) and j<len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        merged.extend(word1[i:])

        merged.extend(word2[j:])

        return ''.join(merged)

            
# extend method in python is used to add elements of a list to another list.
            
        