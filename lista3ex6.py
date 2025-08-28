maiorMedia=0
menorMedia=9999
qtdeAprov=0
qtdeRep=0
for i in range(10):
    n1 = float(input("nota 1 bimestre: "))
    n2 = float(input("nota 2 bimestre: "))
    n3 = float(input("nota 3 bimestre: "))
    media = (n1+n2+n3) / 3
    if media>maiorMedia:
        maiorMedia=media
    if media<menorMedia:
        menorMedia=media
    if media>=6:
        qtdeAprov+=1
    else:
        qtdeRep+=1
print("A maior média é ", maiorMedia)
print("A menor média é ", menorMedia)
print("A quantidade de alunos aprovados é ", qtdeAprov)
print("A quantidade de alunos reprovados é ", qtdeRep)