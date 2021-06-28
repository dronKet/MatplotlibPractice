import matplotlib.pyplot as plt
import numpy as np


def iterate_numpy(population):
    neighbours = sum([np.roll(np.roll(population, -1, 1), 1, 0),
                      np.roll(np.roll(population, 1, 1), -1, 0),
                      np.roll(np.roll(population, 1, 1), 1, 0),
                      np.roll(np.roll(population, -1, 1), -1, 0),
                      np.roll(population, 1, 1),
                      np.roll(population, -1, 1),
                      np.roll(population, 1, 0),
                      np.roll(population, -1, 0)])
    return (neighbours == 3) | (population & (neighbours == 2))


population = np.random.randint(2, size=(int(input()), int(input())), dtype=np.uint8)

for i in range(10):
    plt.matshow(population)
    plt.show()
    #print(population,sep="\n")
    population = iterate_numpy(population)

