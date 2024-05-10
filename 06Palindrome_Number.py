""" Given an integer x, return true if x is a 
palindrome,and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        value = True if string == string[::-1] else False
        
        return value