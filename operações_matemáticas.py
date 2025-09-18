import os
print("OPERAÇÕES MATEMÁTICAS \n     ---MENU---")
print("1 - Soma \n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão\n"
      "5 - Par ou ímpar\n"
      "6 - Primo\n"
      "7 - Fatorial")
opcao=input("Digite a opção desejada ou <SAIR> para encerrar:")
opcaoMaius=opcao.upper()
while opcaoMaius!="SAIR":
    if opcao=="1":
          numero1=int(input("Digite o primeiro valor: "))
          numero2=int(input("Digite o segundo valor: "))
          print("O resultado da soma entre",numero1, "e",numero2,"é",numero1+numero2,)
    if opcao=="2":
          numero1=int(input("Digite o primeiro valor: "))
          numero2=int(input("Digite o segundo valor: "))
          print("O resultado da subtração entre",numero1, "e",numero2,"é",numero1-numero2,)
    if opcao=="3":
          numero1=int(input("Digite o primeiro valor: "))
          numero2=int(input("Digite o segundo valor: "))
          print("O resultado da multiplicação entre",numero1, "e",numero2,"é",numero1*numero2,)
    if opcao=="4":
          numero1=int(input("Digite o primeiro valor: "))
          numero2=int(input("Digite o segundo valor: "))
          print("O resultado da divisão entre",numero1, "e",numero2,"é",numero1/numero2,)
    if opcao=="5":
        numero=int(input("Digite o número para saber se e par ou ímpar: "))
        if numero%2==0:
            print("O número",numero,"é par")
        else:
            print("O número",numero,"é ímpar")
    if opcao=="6":
         primo=int(input("Digite o número para descobrir se é primo:"))
         if primo%2!=0:
               print("o numero é primo")
         else:
               print("o numero não é primo")
    input("Pressione ENTER para voltar ao MENU!")
    os.system("cls")
    print("OPERAÇÕES MATEMÁTICAS \n     ---MENU---")
    print("1 - Soma \n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão\n"
      "5 - Par ou ímpar\n"
      "6 - Primo\n"
      "7 - Fatorial")
    opcao=input("Digite a opção desejada ou <SAIR> para encerrar:")
    opcaoMaius=opcao.upper()