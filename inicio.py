from colorama import init, Fore, Back, Style
init()

def filtra(palavras,n):
    filtro = []
    for palavra in palavras:
        if len(palavra) == n:
            if palavra.lower() not in filtro:
                filtro.append(palavra.lower())
    return filtro

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
palpite = [input('Qual seu palpite?')]

print(filtra(palpite,n_letras))