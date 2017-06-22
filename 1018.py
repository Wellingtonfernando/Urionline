num = int(input())

cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0
soma = 0
aux = num
aux = int(aux)

while(soma != num):
    if(aux >= 100):
        cont100 += 1
        soma += 100
        aux = aux - 100
    elif(aux >= 50):
        cont50 += 1
        soma += 50
        aux = aux - 50
    elif(aux >= 20):
        cont20 += 1
        soma += 20
        aux = aux - 20
    elif(aux >= 10):
        cont10 += 1
        soma += 10
        aux = aux - 10
    elif(aux >= 5):
        cont5 += 1
        soma += 5
        aux = aux - 5
    elif(aux >= 2):
        cont2 += 1
        soma += 2
        aux = aux - 2
    elif(aux >= 1):
        cont1 += 1
        soma += 1
        aux = aux - 1
        
print("%d" %num)
print("%d nota(s) de R$ 100,00" %cont100)
print("%d nota(s) de R$ 50.00"  %cont50)
print("%d nota(s) de R$ 20,00"  %cont20)
print("%d nota(s) de R$ 10,00"  %cont10)
print("%d nota(s) de R$ 5,00"   %cont5)
print("%d nota(s) de R$ 2,00"   %cont2)
print("%d nota(s) de R$ 1,00"   %cont1)
