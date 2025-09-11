contagem = 0
soma = 0
n = int(input("digite um número:"))
while contagem!=n+1:
    soma += contagem
    contagem+=1
print("a soma dos números de 1 a", n, "é:", soma)
