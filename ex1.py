n1 = int(input("primeiro número: "))
n2 = int(input("segundo número: "))
n3 = int(input("terceiro número: "))

if n1 > n2 > n3:
    print(n1, n2, n3)
if n1 > n3 > n2:    
    print(n1, n3, n2)
if n2 > n1 > n3:
    print(n2, n1, n3)
if n2 > n3 > n1:
    print(n2, n3, n1)
if n3 > n1 > n2:
    print(n3, n1, n2)
if n3 > n2 > n1:
    print(n3, n2, n1 )    
