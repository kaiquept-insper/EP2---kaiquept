from colorama import init, Fore, Back, Style
from BaseDePalavras import *
from funcoes import *
init()

print(' =========================== ')
print('|                           |')
print('| Bem-vindo ao Insper Termo |')
print('|                           |')
print(' ==== Design de Software === ')
print('Comandos: desisto')
print(' Regras:')
print(f'  - Você tem {Fore.RED }6{Style.RESET_ALL} tentativas para acertar uma palavra aleatória de 5 letras.')
print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(f'    . {Fore.BLUE }Azul{Style.RESET_ALL}: a letra está na posição correta;')
print(f'    . {Fore.YELLOW }Amarelo{Style.RESET_ALL}: a palavra tem a letra, mas está na posição errada;')
print(f'    . {Fore.BLACK }Cinza{Style.RESET_ALL}: a palavra não tem a letra.')
print('  - Os acentos são ignorados;')
print('  - As palavras podem possuir letras repetidas.')
print('Sorteando uma palavra...')
print('Já tenho uma palavra! Tente adivinhá-la!')
print('Você tem 6 tentaviva(s)')

n_letras = int(input('Com quantas letras quer jogar?'))
palavras = filtra(PALAVRAS,n_letras)
dic = inicializa(palavras)
print(dic) #-----------------------------------------------------------------apenas para teste, apagar dps

palpite = input('Qual seu palpite?')
tentativas = 1

while tentativas < 6:
    idc = 0 
    palavra = ''
    if palpite == dic['sorteada']:
        for i in palpite:
            palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '       
            idc += 1
        print(palavra)
        print(f'*** Parabéns! Você acertou após {tentativas} tentativa(s)!')
        break

    print(palavra)
    indicador = indica_posicao(dic['sorteada'], palpite)
    
    
    for i in indicador:
        if i == 0:
            palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '

        elif i == 1:
            palavra += f' | {Fore.YELLOW }{palpite[idc]}{Style.RESET_ALL} | '

        elif i == 2:
            palavra += f' | {Fore.BLACK }{palpite[idc]}{Style.RESET_ALL} | '
        
        idc += 1

    print(palavra)
    print(f'Você tem {6 - tentativas} tentaviva(s)')
    palpite = input('Qual seu palpite?')
    tentativas += 1

