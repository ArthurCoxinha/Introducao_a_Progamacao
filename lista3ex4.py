jogadores = 0
somaAltura = 0
jogadores = int(input("número de jogadores "))
for i in range(jogadores):
    altura = float(input("digite a altura dos jogadores: "))
    somaAltura+=altura
print("a altura média dos jogadores é:", somaAltura/jogadores)