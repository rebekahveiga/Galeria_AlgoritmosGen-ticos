# Neste novo contexto, imagine que um determinado aplicativo tem um conjunto de fotos de um usuário. 
# Cada foto tem um número de likes, bem como um número de pessoas que foram "tagueadas" na foto, além do próprio usuário. 
# A idéia é ter um serviço GALERIA, o qual identifica no conjunto total de fotos onde o usuário é tagueado, 
# aquelas mais curtidas. 
# Deve-se evitar fotos não tão pessoais, como aquelas onde o usuário é "mais um". 
# Uma boa forma de evitar isso é limitar  o número total de taguados a um valor máximo (MAX_TAG) 
# no total de fotos selecionadas para a GALERIA.

from matplotlib import pyplot as plt
from genetic2022g import *
from bruteforceg import *
import time

#Definindo fotos_totais possiveis (pessoas tagueadas, número de likes)
fotos_totais =  [(6 ,230) ,(5 ,425) ,(1 ,210) ,(1 ,557) ,(3 ,840) ,(8 ,380) ,(2 ,565) ,(3 ,127) ,(7 ,495) ,
(17,428) ,(8,339) ,(2,486) ,(14,618)] #,(5,484) ,(4,292) ,(3,373) ,(11,210) ,(3,214), (3 ,220) ,(5 ,418) ,(2 ,313) ,(8 ,235), (3,200),
#(5,360), (2, 244), (5,499)]

#Numero de fotos
n_fotos = len(fotos_totais)
print("Nro de fotos: "+str(n_fotos)) # Numero total de fotos
max_tagueadas = 15 #limitar a 30 pessoas tagueadas no total das fotos, com isso se evita fotos com muitas pessoas

#Calcula valor de validação com o metodo da força bruta 
t0 = time.time()
best = run_bruteforce(fotos_totais, max_tagueadas)
t1 = time.time()
print("Tempo Brute force: "+str(t1-t0))
t0 = time.time()
print('t0 =' +str(t0))

#Tamanho da população, 100 individuos
p_count = 100

#Criando a população
p = population(p_count , n_fotos)

#Numero de gerações que serão testadas, 1500 gerações
epochs = 150

#Salva fitness para referencia
media = media_fitness(p, fotos_totais, max_tagueadas) #fitness medio 
best_f = best_fitness(p, fotos_totais, max_tagueadas) #melhor fitness 
#aqui ele guarda o historico dos fitness
fitness_history = [[media[0]],[media[1]],[best_f[0]],[best_f[1]]] 

"""
Ele ira evoluir por 1500 gerações, criando assim 1500 gerações de 100 individios e irá guardar a média dos fitness 
e também o melhor fitness daquela geração.

"""
for i in range(epochs):
    p = evolve(p, fotos_totais , max_tagueadas) #evolui
    media = media_fitness(p, fotos_totais, max_tagueadas) #guarda o valor médio de fitness daquela geração
    best_f = best_fitness(p, fotos_totais, max_tagueadas) #guarda o melhor fitness daquela geração
    fitness_history[0].append(media[0])
    fitness_history[1].append(media[1])
    fitness_history[2].append(best_f[0])
    fitness_history[3].append(best_f[1])

t1 = time.time()

#aqui é printado o melhor fitness da soma de tags e da soma de likes
print("Individuo Brute Force: "+str(best[1])+", Likes na foto: "+str(best[0]))

#tempo de processamento do algoritmo genético
print("Tempo AG: "+str(t1-t0))

#printado melhor fitness pelo algoritmo genético
print("Individuo AG: "+str(sorted(p, key=lambda p:p[0])[-1])+", Likes na foto: " +str(fitness_history[2][-1]))

#plotagem do gráfico
fig = plt.figure()
ax = plt.axes()
ax.plot(fitness_history[0])
ax.plot(fitness_history[2])
ax.plot([best[0] for i in fitness_history[0]])
ax.plot(fitness_history[1])
ax.plot(fitness_history[3])

ax.legend(["Fitness Media", "Melhor Fitness", "Fitness Brute Force", " Likes (x10)", "Likes (x10)"])

ax.grid(True)
plt.show()
