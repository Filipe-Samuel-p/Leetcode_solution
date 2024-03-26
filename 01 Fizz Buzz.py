""" Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lista = list(range(1,n+1))
        for i in lista:
            if i % 3 == 0 and i % 5 == 0:
                lista[-1 + i] = "FizzBuzz"
            elif i % 3 == 0:
               lista[-1 + i] = "Fizz"
            elif i % 5 == 0:
                lista[-1 + i] = "Buzz"
            else:
               lista[-1 + i] = str(i)
            
        return lista
