texto = str(input("digite o texto: "))
chave = 3
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convertido = ''
texto1 = texto.upper()
for caractere in texto1:
    if caractere in CARACTERES:
        num = CARACTERES.find(caractere)
        num = num + chave
    if num >= len(CARACTERES):
        num = num - len(CARACTERES)
    elif num < 0:
        num = num + len(CARACTERES)
        convertido = convertido + CARACTERES[num]
    else:
        convertido = convertido + CARACTERES[num]
    
print('texto cripitografado eh' , convertido)
