"""
Autor: Nicolle Ribeiro e Rebekah Veiga
Trabalho 1 - Problema da Galeria 
"""

from random import randint , random , getrandbits
from operator import add
from functools import reduce
from bitstring import BitArray

#Cria um membro da populacao, a partir de um array de bits aleatorios
def individual(length , rand=True):
    if rand:
        return BitArray(uint=getrandbits(length) ,length=length)
    else:
        return BitArray(length)

#Cria a população com o tamanho total definido (100 individuos)
def population(count, length):
    return [ individual(length) for x in range(count) ]


#A função fitness vai resultar na soma dos likes contidos nas fotos onde o numero máximo de pessoas tagueadas
#não for ultrapassado (15 pessoas).
#Se exceder o numero máximo de tags ele vai retornar zero e esse valor não vai ser contabilizado no fitness
def fitness(individual , fotos_totais , max_tagueadas):
    #Valores iniciais
    tag = 0
    likes = 0

    #Para cada bit
    for i,x in enumerate(individual):
        #Fotos postadas
        if x :
            tag += fotos_totais[i][0]
            likes += fotos_totais[i][1]

            #Se exceder o numero de tag maximo
            if tag > max_tagueadas:
                return 0
    return likes

#contabilizar o número de pessoas marcadas em todas as fotos, onde retorna a soma de tags em todas as fotos
def tag(individual , fotos_totais):
    tag =0
    for i,x in enumerate(individual):
        if x:
            tag+=fotos_totais[i][0]
    return tag

#Calcula a media de fitness da população
def media_fitness(pop, fotos_totais, max_tagueadas):
    summed = reduce(add, (fitness(x, fotos_totais, max_tagueadas) for x in pop))
    sum_peso = 10*reduce(add, (tag(x,fotos_totais) for x in pop))
    len_ = len(pop)*1.0
    return (summed/len_, sum_peso/len_)

#Calcula o melhor de fitness da população
def best_fitness(pop, fotos_totais, max_tagueadas):
    graded = [(x, fitness(x, fotos_totais, max_tagueadas), x) for x in pop]
    best = max(graded, key=lambda graded:graded[1])
    return (best[1], 10*tag(best[0], fotos_totais))

#Função de evolução que vai receber como parametros o tamanho da população, 
#o numero de fotos totais, o numero maximo de pessoas, o numero de individuos
#que vao ser passados por elitismo,
#Taxa de porcentagem da qnt de individuos que serão pais e a taxa de mutação da pop.
def evolve(pop, fotos_totais, max_tagueadas, elite=5, r_parents=0.4, mutate=0.01):
    #Tabula cada individuo e o seu fitness
    graded = [(fitness(x, fotos_totais, max_tagueadas), x) for x in pop]

    #Ordena pelo fitness
    graded = sorted(graded, key=lambda graded: graded[0], reverse=True)

    #Pais, quantidade de individuos pais
    parents_length = int(len(graded)*r_parents)

    #Elitismo, ele pega os 5 individuos com melhores fitness e passa direto para a proxima geração
    if elite:
        parents = [x[1] for x in graded][0:elite]
    else:
        parents = []

#Para geração dos próximos filhos
#Utiliza o método da roleta - onde indivíduos da geração são escolhidos para fazer parte da próxima geração, 
#através de um sorteio de roleta. Neste método, cada indivíduo da população é representado na roleta proporcionalmente 
#ao seu índice de aptidão (Fitness). Para os individuos com alta aptidão é dada uma porção maior da roleta, enquanto
#aos de aptidão mais baixa é dada uma porção menor da roleta. Então a roleta é girada de acordo com o tamanho da população
#e os individuos sorteados pela roleta são os que participarão da próxima geração
        
    #Roleta
    sum_fit = reduce(add, (x[0] for x in graded))
    while len(parents) < parents_length:
        pick = random ()
        acum_fit = 0
        for i, (fit, individual) in enumerate(graded):
            acum_fit += fit/sum_fit #Distribuicao acumulativa normalizada
            
            if acum_fit > pick:
                parents.append(individual)
                break

    parents_length = len(parents)
    #descobre quantos filhos terao que ser gerados alem da elite e aleatorios
    desired_length = len(pop) - parents_length
    children = []
    #comeca a gerar filhos que faltam
    while len(children) < desired_length:
        #escolhe pai e mae no conjunto de pais
        male = randint(0, parents_length -1)
        female = randint(0, parents_length -1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = randint(2,len(male))
            #gera filho metade de cada
            child = male[:half] + female[half:]
            #adiciona novo filho a lista de filhos
            children.append(child)

    #Adiciona lista de filhos na nova populacao
    parents.extend(children)
    # mutate some individuals
    for i, individual in enumerate(parents):
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual.invert(pos_to_mutate)
    return parents




   
