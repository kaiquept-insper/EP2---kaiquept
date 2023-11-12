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
print(f'  - Você tem {Fore.RED }6{Style.RESET_ALL} tentativas para acertar uma palavra aleatória com um numero de letras de sua escolha.')
print('  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:')
print(f'    . {Fore.BLUE }Azul{Style.RESET_ALL}: a letra está na posição correta;')
print(f'    . {Fore.YELLOW }Amarelo{Style.RESET_ALL}: a palavra tem a letra, mas está na posição errada;')
print(f'    . {Fore.BLACK }Cinza{Style.RESET_ALL}: a palavra não tem a letra.')
print('  - Os acentos são ignorados;')
print('  - As palavras podem possuir letras repetidas.')
print(' ')
jog_nov = 'S'
while jog_nov == 'S':
    n_letras = int(input('Com quantas letras quer jogar? '))
    while 1 > n_letras or 23 < n_letras:
        print('Não há palavras com esse numero de letras no sistema...')
        n_letras = int(input('Digite um numero entre 1 e 23: '))
    print('Sorteando uma palavra...')
    time.sleep(2)
    print('Já tenho uma palavra! Tente adivinhá-la!')
    print('Você tem 6 tentaviva(s)')
    print(' ')


    palavras = filtra(PALAVRAS,n_letras)
    dic = inicializa(palavras)
    #print(dic)

    palpite = input('Qual seu palpite? ')
    tentativas = 1

    palavra = ''
    palavra_ant = ''
    while tentativas < 6:
        idc = 0 
        palavra_ant += palavra + '\n' + '  ---  ' * len(palpite) + '\n'
        palavra = ''
    
        while palpite not in PALAVRAS:
            print('Palavra desconhecida')
            palpite = input('Qual seu palpite? ')

        if palpite == dic['sorteada']:
            for i in palpite:
                palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '       
                idc += 1
            print('  ---  ' * len(palpite))
            print(palavra)
            print('  ---  ' * len(palpite))
            print('  ---------------------------------------------  ')
            print(f' | {Fore.YELLOW }Parabéns! Você acertou após {tentativas} tentativa(s)!{Style.RESET_ALL} | ')
            print('  ---------------------------------------------  ')
            break
        elif palpite == 'desisto':
            desistencia = input('Tem certeza? [S/N] ')
            if desistencia == 'S':
                print('  ----------------  ')
                print(f' | {Fore.RED }Até a proxima!{Style.RESET_ALL} | ')
                print('  ----------------  ')
                break

            elif desistencia == 'N':
                print('  ---------------------  ')
                print(f' | {Fore.GREEN }Boa! Nunca desista!{Style.RESET_ALL} | ')
                print('  ---------------------  ')
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
    if tentativas == 6:
        if palpite == dic['sorteada']:
            for i in palpite:
                palavra += f' | {Fore.BLUE }{palpite[idc]}{Style.RESET_ALL} | '       
                idc += 1
            print('  ---  ' * len(palpite))
            print(palavra)
            print('  ---  ' * len(palpite))
            print('  ---------------------------------------------  ')
            print(f' | {Fore.YELLOW }Parabéns! Você acertou após {tentativas} tentativa(s)!{Style.RESET_ALL} | ')
            print('  ---------------------------------------------  ')
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

        sorteada = dic['sorteada']
        print(f'A palavra era {Fore.YELLOW }{sorteada}{Style.RESET_ALL}')
        print('  -------------  ')
        print(f' | {Fore.RED }Você perdeu{Style.RESET_ALL} | ')
        print('  -------------  ')
    
    jog_nov = input('Deseja jogar novamente?[S/N] ')
    if jog_nov == 'N':
        print('Até a proxima!')
        break