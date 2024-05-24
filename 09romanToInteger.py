class Solution:
    def romanToInt(self, s: str) -> int:
       valueSymbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
       } 
       result = 0
       for index in range (len(s)): 
            if index < len(s) - 1 and valueSymbols[s[index]] < valueSymbols[s[index+1]]:
                #Idéia: toda vez que o valor atual for menor que o proximo valor, só tirar o valor atual da contagem
                result -= valueSymbols[s[index]]
            else:
                result += valueSymbols[s[index]]

       return result
       
        