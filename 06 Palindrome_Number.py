""" Given an integer x, return true if x is a 
palindrome,and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        lista = [x for x in string]
        lista2 = []
        for i in range(len(lista) - 1, -1, -1):
            lista2.append(lista[i])
        palindrome = "".join(lista2)
        valor = True if palindrome == string else False
        
        return valor