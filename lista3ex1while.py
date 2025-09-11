somaValor=0 
contNegativo=0
contagem=1
while contagem<=20:
    contagem+=1
    valor=int(input("digite um número: "))
    if valor>0:
        somaValor+=valor
    else:
        contNegativo+=1
print("A soma dos valores positivos é:", somaValor)
print("A quantidade de valores negativos é:", contNegativo)