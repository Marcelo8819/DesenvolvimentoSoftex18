print('Identificação')
cont = 0
while cont == 0:
  try:
    print("Digite seu nome: ")
    nome = input()
    print("Digite o ano do seu nascimento, entre 1922 e 2021: ")
    ano_nasc = int(input())
    print(nome)
    print("você tem ", 2022 - ano_nasc, " anos.")
    cont = 1
  except:
    print("informaçoes erradas!")
    cont = 0