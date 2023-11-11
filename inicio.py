from colorama import init, Fore, Back, Style
from BaseDePalavras import *
from funcoes import *
import time

init()

print(' =========================== ')
print('|                           |')
print('| Bem-vindo ao Insper Termo |')
print('|                           |')
print(' ==== Design de Software === ')
print('Comandos: desisto')
print(' ')
print(' Regras:')
print(f'  - Você tem {Fore.RED }6{Style.RESET_ALL} tentativas para acertar uma palavra aleatória de 5 letras.')
print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(f'    . {Fore.BLUE }Azul{Style.RESET_ALL}: a letra está na posição correta;')
print(f'    . {Fore.YELLOW }Amarelo{Style.RESET_ALL}: a palavra tem a letra, mas está na posição errada;')
print(f'    . {Fore.BLACK }Cinza{Style.RESET_ALL}: a palavra não tem a letra.')
print('  - Os acentos são ignorados;')
print('  - As palavras podem possuir letras repetidas.')
print(' ')
n_letras = int(input('Com quantas letras quer jogar? '))
print('Sorteando uma palavra...')
time.sleep(2)
print('Já tenho uma palavra! Tente adivinhá-la!')
print('Você tem 6 tentaviva(s)')
print(' ')


palavras = filtra(PALAVRAS,n_letras)
dic = inicializa(palavras)
print(dic) #-----------------------------------------------------------------apenas para teste, apagar dps

palpite = input('Qual seu palpite? ')
tentativas = 1

palavra = ''
palavra_ant = ''
while tentativas < 6:
    idc = 0 
    palavra_ant += palavra + '\n' + '  ---  ' * len(palpite) + '\n'
    palavra = ''
    
    

    if palpite == dic['sorteada']:
        for i in palpite:
            palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '       
            idc += 1
        print('  ---  ' * len(palpite))
        print(palavra)
        print('  ---  ' * len(palpite))
        print(f'*** Parabéns! Você acertou após {tentativas} tentativa(s)!')
        break
    elif palpite == 'desisto':
        desistencia = input('Tem certeza? [S/N] ')
        if desistencia == 'S':
            print('Até a proxima!')
            break
        elif desistencia == 'N':
            print('Boa! Nunca desista!')
            palpite = input('Qual seu palpite? ')

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
    
    if tentativas > 1:
        print(palavra_ant)
    
    print('  ---  ' * len(palpite))
    print(palavra)
    print('  ---  ' * len(palpite))
    print(f'Você tem {6 - tentativas} tentaviva(s)')
    palpite = input('Qual seu palpite? ')
    tentativas += 1
palavra = ''
idc = 0
if palpite == dic['sorteada']:
    for i in palpite:
        palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '       
        idc += 1
    print('  ---  ' * len(palpite))
    print(palavra)
    print('  ---  ' * len(palpite))
    print(f'*** Parabéns! Você acertou após {tentativas} tentativa(s)!')
else:
    for i in indicador:
        if i == 0:
            palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '

        elif i == 1:
            palavra += f' | {Fore.YELLOW }{palpite[idc]}{Style.RESET_ALL} | '

        elif i == 2:
            palavra += f' | {Fore.BLACK }{palpite[idc]}{Style.RESET_ALL} | '
        
        idc += 1

if palpite != dic['sorteada']:          
    if tentativas > 1:
        print(palavra_ant)
    
    print('  ---  ' * len(palpite))
    print(palavra)
    print('  ---  ' * len(palpite))


    print('Você perdeu')
    
