""" Dado um array nums. Definimos uma soma acumulada de um array como  runningSum[i] = sum(nums[0]…nums[i]).

Retorne a soma acumulada de nums.

 

Exemplo 1:

Entrada: nums = [1,2,3,4]
 Saída: [1,3,6,10]
 Explicação: A soma acumulada é obtida da seguinte forma: [1, 1+2, 1+2+3, 1+2+ 3+4]."""



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        lista = []
        for i in nums:
            x += i
            lista.append(x)
        return lista