#robô agrícola
bateria=int(input("Nível de bateria: "))
temperatura=int(input("Temperatura do ambiente: "))
umidade=int(input("Umidade do solo: "))
modo=input("Modo de operação: ")
#bateria
if bateria<20:
    print("Bateria muito baixa! Retorne imediatamente para a base")
else:
    if bateria<50:
        print("Atenção: bateria em nível moderado")
    else:
        print("Bateria suficiente para operação")
#temperatura
if temperatura>40:
    print("Temperatura crítica! Operação suspensa")
if temperatura<5:
    print("Frio extremo! Modo de economia ativado")
#umidade
if umidade<30:
    print("Solo muito seco. Recomendado iniciar irrigação")
if umidade>80:
    print("Solo encharcado! Suspenda irrigação imediatamente")
#modo de operação
if modo=="plantio":
    print("Iniciando modo PLANTIO...")
if modo=="colheita":
    print("Iniciando modo COLHEITA...")
if modo=="irrigação":
    print("Iniciando modo IRRIGAÇÃO...")
#ininciando robô
if bateria>=50:
    if temperatura<40:
        if temperatura>5:
            if umidade>30:
                if umidade<80:
                    print("Robô autorizado a iniciar a operação!")
                print("Operação negada! Verifique as condições do ambiente")
            print("Operação negada! Verifique as condições do ambiente")
        print("Operação negada! Verifique as condições do ambiente")
    print("Operação negada! Verifique as condições do ambiente")
print("Operação negada! Verifique as condições do ambiente")