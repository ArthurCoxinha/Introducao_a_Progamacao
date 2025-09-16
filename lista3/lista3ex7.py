thanos = 1.50
aranha = 1.10
anos = 0
for i in range(100):
    thanos=thanos+0.02
    aranha=aranha+0.03
    anos=anos+1
    if aranha>thanos:
        break
print(anos)
        