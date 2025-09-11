contagem = 0
somaAltura = 0
jogadores = int(input("número de jogadores "))
while contagem!=jogadores: 
    altura = float(input("digite a altura dos jogadores: "))
    somaAltura+=altura
    contagem+=1
print("a altura média dos jogadores é:", somaAltura/jogadores)