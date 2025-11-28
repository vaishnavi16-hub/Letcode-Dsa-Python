
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 









# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         res = ""
#         carry = 0
#         a, b = a[::-1], b[::-1]

#         for i in range(max(len(a), len(b))):
#             digitA = ord(a[i]) - ord("0") if i < len(a) else 0
#             digitB = ord(b[i]) - ord("0") if i < len(b) else 0

#             total = digitA + digitB + carry
#             res = str(total % 2) + res
#             carry = total // 2  # 🔧 fix here: carry should be total // 2

#         if carry:
#             res = "1" + res

#         return res
