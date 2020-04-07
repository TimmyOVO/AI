# 求解the_function在[0,15]的最大值

# Generate some individual with random genetic
# Calculate individual's fitness and pick some individual
# Crossover their genetic using specific rule(s)
# Make their child mutation
# Algorithm should be terminates if the population has converged

# def the_function(z):
#     return 3 * numpy.sin(z) * 7 * numpy.cos(z) + 4 * z
#

# 1 bit for the sign of number ,0 positive 1 negative
# 8 bits for the exponent
# 23 bits for the mantissa

import random
import struct
from codecs import decode

import matplotlib.pyplot as plt
import numpy

Round = [0, 2000]

class GA:
    PopulationSize = 10000
    GeneSize = 64

    def __init__(self):
        self.Population = Population(self.PopulationSize, self.GeneSize)
        pass

    def start(self):
        for i in range(Round[1]):
            self.Population.selection()
            self.Population.crossover()
            self.Population.mutation()
            if not (len(self.Population.Individuals) == 0):
                plt.plot([i], [self.Population.Individuals[0].fitness()], marker='o', markersize=3, color="red")
                print('Generation ', i, ' fitness ', self.Population.Individuals[0].fitness(), ' input ',
                      self.Population.Individuals[0].value())


class Population:
    Individuals = []
    CrossoverRatio = 0.7
    MutationRatio = 0.1

    def __init__(self, population_size, gene_size):
        self.Individuals = []
        for _ in range(population_size):
            self.Individuals.append(Individual(gene_size))

    def selection(self):
        survived_individuals = []
        for i in self.Individuals:
            v = random.randrange(0, 100)
            if v <= (i.fitness()):
                survived_individuals.append(i)
        survived_individuals.sort(key=lambda z: z.fitness(), reverse=True)
        if len(survived_individuals) >= 500:
            survived_individuals = survived_individuals[:500]
        self.Individuals = survived_individuals

    def crossover(self):
        for _ in range(int(len(self.Individuals) * self.CrossoverRatio)):
            p1 = random.choice(self.Individuals)
            p2 = random.choice(self.Individuals)
            self.Individuals.append(p1.crossover(p2))

    def mutation(self):
        for _ in range(int(len(self.Individuals) * self.MutationRatio)):
            target = random.choice(self.Individuals)
            for _ in range(int(len(target.Genes) / 10)):
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
        v = bin_to_float(''.join(temp))
        return v

    def fitness(self):
        v = self.value()
        if v < Round[0] or v > Round[1]:
            return -100
        return 3 * numpy.sin(v) * 7 * numpy.cos(v) + 4 * v


def bin_to_float(b):
    bf = int_to_bytes(int(b, 2), 8)
    return struct.unpack('>d', bf)[0]


def int_to_bytes(n, length):
    return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]


def float_to_bin(value):
    [d] = struct.unpack(">Q", struct.pack(">d", value))
    return '{:064b}'.format(d)


GA().start()

x = numpy.linspace(Round[0], Round[1])
y = 3 * numpy.sin(x) * 7 * numpy.cos(x) + 4 * x
plt.plot(x, y)
plt.title('f(x) = 3sin(x) * 7cos(x) + 4x')
plt.show()
