import random

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Rectangle

size = 50


class MapGenerator:
    MapSize = 0
    LineCount = 0

    Barrier = []

    def __init__(self, size, linecount):
        self.MapSize = size
        self.LineCount = linecount

    def get_point(self, x, zx, zc):
        return x * zx + zc

    def generate_map(self):
        for z in range(self.LineCount):
            self.generate_barrier()

    def generate_barrier(self):
        start = random.randrange(0, int(self.MapSize / 2))
        length = random.randrange(0, self.MapSize)
        zx = random.randrange(0, int(self.MapSize / 8))
        zc = random.randrange(0, int(self.MapSize / 2))
        for i in range(length * 5):
            z = start + i / 5
            self.Barrier.append((numpy.floor(z), numpy.floor(self.get_point(z, zx, zc))))
        self.Barrier = list(dict.fromkeys(self.Barrier))


class MapPictureGenerator:
    Map = None

    def __init__(self):
        self.Map = MapGenerator(size, 5)
        self.Map.generate_map()

    def setup(self):
        numpy.array([])
        plt.figure(figsize=(5, 5))
        ax = plt.gca()
        ax.set_xlim([0, size])
        ax.set_ylim([0, size])
        for x in range(size):
            for z in range(size):
                ax.add_patch(Rectangle((x, z), width=1, height=1, edgecolor='gray', facecolor='w'))

        for p in self.Map.Barrier:
            # plt.plot([p[0][0], p[0][1]], [p[1][0], p[1][1]])
            ax.add_patch(Rectangle((numpy.floor(p[0]), numpy.floor(p[1])), width=1, height=1, color='red'))
        plt.show()
        print(self.Map.Barrier)


def function1(x):
    return x + 10 * numpy.sin(5 * x) + 7 * numpy.cos(4 * x)


x = numpy.linspace(0, 15)
y = function1(x)
plt.plot(x, y)
plt.show()
