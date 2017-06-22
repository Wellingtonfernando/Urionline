nome = str(input())
sal = float(input())
tot_vendas = float(input())
comisao = 0.15

total = (comisao * tot_vendas) + sal

print('TOTAL = R$ %.2f' %total)
