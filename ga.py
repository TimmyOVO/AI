# 求解the_function在[0,15]的最大值

# Generate some individual with random genetic
# Calculate individual's fitness and pick some individual
# Crossover their genetic using specific rule(s)
# Make their child mutation
# Algorithm should be terminates if the population has converged

# def the_function(z):
#     return math.sin(z)
#

# 1 bit for the sign of number ,0 positive 1 negative
# 8 bits for the exponent
# 23 bits for the mantissa

import math
import random


class GA:
    PopulationSize = 1000
    GeneSize = 20

    def __init__(self):
        self.Population = Population(self.PopulationSize, self.GeneSize)
        pass

    def start(self):
        for i in range(0xFFFFFFF):
            self.Population.selection()
            self.Population.crossover()
            self.Population.mutation()
            print('Generation ', i, ' fitness ', self.Population.Individuals[0].fitness(), ' input ', self.Population.Individuals[0].value())
        print(self.Population.Individuals)


class Population:
    Individuals = []
    CrossoverRatio = 0.6
    MutationRatio = 0.2

    def __init__(self, population_size, gene_size):
        self.Individuals = []
        for _ in range(population_size):
            self.Individuals.append(Individual(gene_size))

    def selection(self):
        survived_individuals = []
        for i in self.Individuals:
            v = random.randrange(0, 100)
            if v <= (i.fitness() * 100):
                survived_individuals.append(i)
        survived_individuals.sort(key=lambda z: z.fitness())
        self.Individuals = survived_individuals

    def crossover(self):
        for _ in range(int(len(self.Individuals) * self.CrossoverRatio)):
            p1 = random.choice(self.Individuals)
            p2 = random.choice(self.Individuals)
            self.Individuals.append(p1.crossover(p2))

    def mutation(self):
        for _ in range(int(len(self.Individuals) * self.MutationRatio)):
            target = random.choice(self.Individuals)
            for _ in range(int(len(target.Genes) / 5)):
                target.Genes[random.randrange(0, len(target.Genes))] = random.randrange(0, 2)


class Individual:
    Genes = []

    def __init__(self, gene_size):
        self.Genes = []
        for _ in range(gene_size):
            self.Genes.append(random.randrange(0, 2))

    def crossover(self, p2):
        iin = Individual(len(self.Genes))
        cut_point = random.randrange(0, len(self.Genes))
        iin.Genes[cut_point:] = self.Genes[cut_point:]
        iin.Genes[:cut_point] = p2.Genes[:cut_point]
        return iin

    def value(self):
        temp = [str(iz) for iz in self.Genes]
        v = int('0b' + ''.join(temp), 2)
        return v

    def fitness(self):
        return math.sin(self.value())


GA().start()
