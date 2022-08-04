"""
Autor: Nicolle Ribeiro e Rebekah Veiga
Trabalho 1 - Problema da Galeria """

from genetic2022g import *

#Função de força bruta realiza métodos diretos de resolver um problema que dependem do poder de computação 
# e tentam todas as possibilidades em vez de técnicas avançadas para melhorar a eficiência. 
def run_bruteforce(fotos_totais, max_tagueadas):
    n_fotos = len(fotos_totais) #Numero total de fotos
    #Individuo inicial (todos zeros)
    individuo = BitArray(n_fotos) 
    #Individuo final (todos uns)
    end = BitArray(n_fotos)
    end.invert()
    #Contador de combinacoes
    combos = 0

    #Verifica todos possiveis individuos
    best = (0,individuo)
    while individuo.uint < end.uint:
        individuo = BitArray(uint = individuo.uint+1, length=n_fotos)
        fit = fitness(individuo , fotos_totais, max_tagueadas)

        if fit > best [0]:
            best = (fit, individuo)
        combos += 1

    print("Nro de combinacoes (Brute Force): "+str(combos))
    return(best)
