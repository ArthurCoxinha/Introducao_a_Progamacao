numero = int(input("digite o numero para ver se é primo ou não: "))
contagem = 0
if numero<2:
    print("o numero não é primo: ")
    
for i in range(1, numero + 1):
        
    if numero %i == 0:
        contagem += 1
            
if contagem ==2:
    print("é numero primo")
else:
    print("o numero não é primo")