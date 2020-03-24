import matplotlib.pyplot as plt


class DataBuilder:

    def read_files(self):
        pass

    def read(self):
        pass

def deltaN(N: int):
    N0 = 100
    alpha = 0.05
    deltaT = 1
    if N > N0:
        N = N0
    return alpha * (N0 - N) * deltaT

if __name__ == '__main__':
    db = DataBuilder()

    n = 0
    N = []
    for i in range(100):
        N.append(n)
        n += deltaN(n)

    plt.plot(N)
    plt.show()
