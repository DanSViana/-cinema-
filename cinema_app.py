# importação de biblioteca
import os 
from datetime import date

# entrada de dados
nome = input('Informe seu nome:')
idade = int(input('Informe sua idade:'))
data = f'({date.today().day}/{date.today().month}/{date.today().year})'

# limpa console
os.system('cls')

# início
while True:
    print(f'{'-'*30} CINE PYTHON {'-'*30}\n')
    print(f'{data}\n')
    print('Sala 1 - A volta dos Que Não Foram - 12 anos.')
    print('Sala 2 - A Roda Quadrada - Livre.')
    print('Sala 3 - Poeira em Alto Mar - 14 anos.')
    print('Sala 4 - As Tranças do Rei Careca - 16 anos.')
    print('Sala 5 - A vingança do Peixe Frito - 18 anos.')

    # escolha do usuário 
    sala = input('\nSala desejada: ')

    # verifica a sala escolhida
    match sala:
        case '1':
            idade_minima = 12
            filme = 'A volta dos Que Não Foram'
        case '2':
            idade_minima = 0
            filme = 'A Roda Quadrada'
        case '3':
            idade_minima = 14
            filme = 'Poeira em Alto Mar'
        case '4':
            idade_minima = 16
            filme = 'As Tranças do Rei Careca'
        case '5':
            idade_minima = 18
            filme = 'A vingança do Peixe Frito'
        case _:
            print('Sala inexistente. Favor escolher outra sala')
            continue

            
    # verificação de idade
    if idade >= idade_minima:
        print(f'Pagante: {nome}.')
        print(f'Filme: {filme}.')
        print(f'Sala: {sala}.')
        print('\nTenha um ótimo filme!')
        break
    else:
        print(f'{nome} não possui a idade minimo para ver {filme}.')
        print('Favor escolhe outro filme!')
        continue