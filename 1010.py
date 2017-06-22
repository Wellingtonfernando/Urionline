peca1, Npeca, vr_peca = input().split()
peca2, Npeca2, vr_peca2 = input().split()

Npeca = int(Npeca)
Npeca2 = int(Npeca2)
vr_peca = float(vr_peca)
vr_peca2 = float(vr_peca2)

vr_total = (Npeca * vr_peca) + (Npeca2 * vr_peca2)

print('VALOR A PAGAR: R$ %.2f' %vr_total)
