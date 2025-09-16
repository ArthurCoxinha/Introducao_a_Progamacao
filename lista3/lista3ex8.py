numero = int(input("digite o número para fatorar: "))
fat = 1
for i in range(1, numero+1):
    fat *= i
print("o resultado do número fatorado é: ", fat)