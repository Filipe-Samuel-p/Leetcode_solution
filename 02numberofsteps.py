""" Dado um número inteiro num, retorne o número de etapas para reduzi-lo a zero .

Em uma etapa, se o número atual for par, você deverá dividi-lo por 2, caso contrário, deverá subtraí 1-lo.

 

Exemplo 1:

Entrada: num = 14
 Saída: 6
 Explicação:  
Etapa 1) 14 é par; divida por 2 e obtenha 7.  
Passo 2) 7 é ímpar; subtraia 1 e obtenha 6. 
Etapa 3) 6 é par; divida por 2 e obtenha 3.  
Etapa 4) 3 é ímpar; subtraia 1 e obtenha 2.  
Etapa 5) 2 é par; divida por 2 e obtenha 1.  
Passo 6) 1 é ímpar; subtraia 1 e obtenha 0."""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        contador = 0
        while num != 0:
            num = num/2 if num % 2 == 0 else num - 1
            contador += 1
        return contador