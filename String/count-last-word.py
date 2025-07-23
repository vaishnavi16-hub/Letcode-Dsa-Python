

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

#  Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.



# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i, length = len(s) - 1, 0

#         # Skip trailing spaces
#         while i >= 0 and s[i] == " ":
#             i -= 1
        
#         # Count the length of the last word
#         while i >= 0 and s[i] != " ":
#             length += 1
#             i -= 1

#         return length
