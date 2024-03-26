""" Você recebe uma m x ngrade inteira accountsonde accounts[i][j]está a quantidade de """ """ dinheiro que o cliente tem no banco. Devolva a riqueza que o cliente mais rico possui."""

""" A riqueza de um cliente é a quantidade de dinheiro que ele possui em todas as suas contas bancárias. O cliente mais rico é aquele que possui a riqueza máxima ."""

""" Exemplo 2:

Entrada: contas = [[1,5],[7,3],[3,5]]
 Saída: 10
 Explicação :
1º cliente tem riqueza = 6
2º cliente tem riqueza = 10
3º cliente tem riqueza = 8
O segundo cliente é o mais rico com uma riqueza de 10. """

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maior = 0
        for i in accounts: 
            x = 0
            for j in i:
             x += j
            maior = max(maior, x)                
        return maior