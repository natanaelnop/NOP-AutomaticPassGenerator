import random
import string
caracteres_especiais = "!@#$%^&*()-_=+[]{};:,.<>?/|"

print("NOP - Gerador de Senha Automatica")
print("Voce pode escolher o tamanho da senha que deseja gerar, \nse ela contera numeros, letras e caracteres especiais.")
print("******************************************************\n")
tam = input("Quantos caracteres deseja que sua senha tenha?")
num = input('Deseja ter numeros em sua senha? (Digite s para sim ou n para não)')
let = input('Deseja ter letras em sua senha? (Digite s para sim ou n para não)')
esp = input('Deseja ter caracteres especiais em sua senha? (Digite s para sim ou n para não)')

senha = []
tipos_escolhidos = []

if num == 's':
    tipos_escolhidos.append('num')
if let == 's':
    tipos_escolhidos.append('let')
if esp == 's':
    tipos_escolhidos.append('esp')

while len(senha) < int(tam):
    tipo = random.choice(tipos_escolhidos)
    if tipo == 'num':
        senha.append(str(random.randint(0, 9)))
    elif tipo == 'let':
        senha.append(random.choice(string.ascii_lowercase))
    elif tipo == 'esp':
        senha.append(random.choice(caracteres_especiais))

print(''.join(senha))
