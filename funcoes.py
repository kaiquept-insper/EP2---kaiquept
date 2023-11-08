import pygame
import random

def filtra(palavras,n):
    filtro = []
    for palavra in palavras:
        if len(palavra) == n:
            if palavra.lower() not in filtro:
                filtro.append(palavra.lower())
    return filtro

def inicializa(palavras):
    dic = {'n','sorteada','especuladas','tentativas'}
    dic['n'] = len(palavras[0])
    dic['tentativas'] = len(palavras[0])+1
    dic['especuladas'] = []
    dic['sorteada'] = random.choice(palavras)
    return dic

def indica_posicao(sorteada, especulada):
    retorno = []
    i=0
    if len(sorteada) != len(especulada):
        return retorno
    else:
        while i < len(sorteada):
            if sorteada[i] == especulada[i]:
                retorno.append(0)
            elif especulada[i] in sorteada:
                retorno.append(1)
            else:
                retorno.append(2)
            i += 1
    return retorno

