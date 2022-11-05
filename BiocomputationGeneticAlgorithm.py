# -*- coding: utf-8 -*-
# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import copy
import math
import matplotlib.pyplot as plt
import numpy as np

GenMax = 50
P = 50  # Number of candidates in solution #The total number
global N
N = 20  # Number of Genes
Mutation = 0.5
MUTRATE = 0.1  # adjust to max value 0.1
totalfitness = 0
bestingeneration = [0] * GenMax
number = 10
random.seed(a=None, version=2)
worst_individual = [0]*N #-------------DOUBLE CHECK ERROR


# random.seed(datetime.now())

# setting up
class Individual:  # setup of individual giving gene and fitness
    def __init__(self):
        self.gene = [0] * N  # Amount of genes/ the 1's and zeros INITALISE USING [0]*N
        self.fitness = 0

    def genes(self):
        for i in range(N):
            self.gene[i] = random.uniform(-5.12, 5.12)

            # creates more variance


def minimisationfunction(gene):
    # x = population[i].gene
    beg = 10 * N
    sum = 0
    for i in range(N):
        x = gene
        sum = ((np.power(x[i], 2)) - (10 * (math.cos(2 * math.pi * (x[i]))))) + sum
  
        #fitness = -20*math.exp(-0.2*math.sqrt((1/N)*sum(genet)))-math.exp((1/N)*math.cos(2*math.pi*sum(gene)))
        
    final = sum + beg  # maths is the fitness
   # final = summary
    return final






# def minimisationfunction(gene):
#     # x = population[i].gene
#     # beg = 10 * N
#     # sum = 0
#     # for i in range(N):
#     #     x = gene
#     #     sum = ((np.power(x[i], 2)) - (10 * (math.cos(2 * math.pi * (x[i]))))) + sum
#     # final = sum + beg  # maths is the fitness
   
    # for i in range(0, N):
    #      genet = 0*[N]
    #      genet[i]=pow(gene[i], 2)
    #      fitness = -20*math.exp(-0.2*math.sqrt((1/N)*sum(genet)))-math.exp((1/N)*math.cos(2*math.pi*sum(gene)))
    
#     final = fitness
    
#     return final





    # fitness = 10 * len(gene)
    # for j in range(0, len(gene)):
    #     fitness = fitness + (gene[j] * gene[j] - 10 * math.cos(2 * math.pi * gene[j]))
    # return fitness


# def minimisation(population):
#     x = population[i]
#     beg = 10*N
#     sum = 0
#     for i in range(N-1):
#         sum = x(i)
#
#     result = 5
#     return result

# 10.24 (double whats on the right ) * rand(0,1) - 5.12 #if one person in the population one person has 10 gene, each gene can between those two numbers 5.12 and -5.12

def calculatefitness(gene):
    fitness = 0
    for i in range(0, len(gene)):
        if gene[i]:
            fitness = fitness + gene[i]
    return fitness


def maxFit(offspring):
    fitnesses = []
    for i in range(0, P):
        fitnesses.append(offspring[i].fitness)
    return max(fitnesses)


def printarray(position):
    for i in range(P):  # cycle through everything one by one
        print(f'Number {i}: {position[i].gene} - Fitness: {position[i].fitness},')


# --------------------------- initialising population ------------------------------------#

population = []
offspring = []
mutatedpopulation = []
bestcandidate = Individual()
totalfitness = [0]


def createpopulation(population, totalfitness):
    for i in range(P):
        population.append(Individual())  # Initalise a gene and fitness
        population[i].genes()  # Initalise a gene and fitness and calls the functon

    return population


def tournamentselection(population, totalfitness):
    for i in range(P):
        parent = random.randint(0, P - 1)  # picks a random parent to chose int tournament selection
        off1 = population[parent]
        parent2 = random.randint(0, P - 1)  # picks a random parent to chose int tournament selection
        off2 = population[parent2]
        if off1.fitness < off2.fitness:  # change this for minimisation
            offspring.append(off1)
        else:
            offspring.append(off2)
    return offspring




def crossover(offspring, totalfitness):
    offspring_crossed = []

    for i in range(0, P, 2):
        newind1 = Individual()
        newind2 = Individual()
        # weirdness of having to use .copy for arrays or
        # it is actually a pointer, not a copy
        crosspoint = random.randint(1, N - 1)
        headgene1 = []
        tailgene1 = []
        headgene2 = []
        tailgene2 = []
        for h in range(0, crosspoint):
            headgene1.append(offspring[i].gene[h])
            headgene2.append(offspring[i + 1].gene[h])

        for j in range(crosspoint, N):
            tailgene1.append(offspring[i].gene[j])
            tailgene2.append(offspring[i + 1].gene[j])
        newind1.gene = headgene1 + tailgene2
        newind1.fitness = (headgene1 + tailgene2).count(1)
        newind2.gene = headgene2 + tailgene1
        newind2.fitness = (headgene2 + tailgene1).count(1)
        offspring_crossed.append(newind1)
        offspring_crossed.append(newind2)

    return offspring_crossed

# mean fitness of one population
def mean_fitness(population):
    totalfitness = 0
    for i in range(0, P):
        print(population[i])
        totalfitness += offspring[i].fitness
    return totalfitness


def calcTotal(population):
    total = 0
    for i in range(0, P):
        total = total + population[i].fitness
    return total



def mutation(offspring, totalfitness):
    for i in range(0, P):
        newind = Individual()
        newind.gene = []
        for j in range(0, N):
            gene = offspring[i].gene[j]
            mutationprob = random.randint(0, 100)  # random() part
            # randomfloat = random.uniform(0.0,0.7) #could possibly be adjusted
            alter = random.uniform(0, 0.1)  # mutstep Adjust
            bit = random.randint(0, 1)

            if mutationprob < (100 * MUTRATE):
                if bit == 0:
                    offspring[i].gene[j] = offspring[i].gene[j] + alter

                else:
                    offspring[i].gene[j] = offspring[i].gene[j] - alter
            newind.gene.append(gene)

    return offspring


def bestinpopulation(population):
    best_individual = []
    counter = 0
    best_fitness = 10000  # adjust for max so fitst goes through
    for i in range(1, np.size(population)):
        if population[i].fitness < best_fitness:  # best_fitness value rises occassionally ?
            best_individual = i
            best_fitness = population[i].fitness

    return best_individual, best_fitness,


# --------------------------- MAIN ------------------------------------#


population = createpopulation(population, totalfitness)  # create population

for i in range(P):
    population[i].fitness = minimisationfunction(population[i].gene)  # fitness func for minimisation

best_individual, bestingeneration[0] = bestinpopulation(population)  #

best_individual2 = best_individual

bestperson = population[best_individual]

#plt.plot(bestingeneration, 'o')
#plt.xlabel("Generation")
#plt.ylabel("Fitness")
#plt.show()

generations = 1

while generations < GenMax:
    offspring = []
    offspring = tournamentselection(population, totalfitness)  # select parents
    # totalfitness[0] = 0  # reset total fitness to for counter
    temp = Individual()
    offspring = crossover(offspring, totalfitness)  # recombine pairs of parents
    offspringcopy = copy.deepcopy(offspring)
    mutatedpopulation = mutation(offspringcopy, totalfitness)
    for i in range(P):
        offspringcopy[i].fitness = minimisationfunction(mutatedpopulation[i].gene)  # added a plus
    x = []  # set as breakpoint checking best fitness
    best_individual, bestingeneration[generations] = bestinpopulation(offspringcopy)

    worst_fitness = 0
    for i in range(P):
        if offspringcopy[i].fitness > worst_fitness:
            worst_individual = i
            worst_fitness = offspringcopy[i].fitness

    if bestingeneration[generations - 1] < bestingeneration[generations]:
        bestingeneration[generations] = bestingeneration[generations - 1]
        offspringcopy[worst_individual] = population[best_individual2]

    best_individual2 = best_individual

    population = offspringcopy
    
    generations += 1
print('fitness array total:', generations, bestingeneration)
    # print(fitnesstotalarray)
plt.plot(bestingeneration)  # store value into array when looping then average all the values

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.show()

# to build up next
# Put into loop 10 times avg
# take bestingene each time store it - [] removing the plot
# plot the array it was stored int as sthat shows the average

# possib before plotting it is gen 2 < than previous ,