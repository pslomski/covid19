import matplotlib.pyplot as plt


class DataFile:

    def __init__(self, file_name: str):
        self._file_name = file_name
        self._country = ''

    def read(self, country: str):
        self._country = country
        data_map = dict()
        f = open(self._file_name)
        try:
            f.readline() # read header
            for line in f:
                line = line.strip()
                if len(line) > 0:
                    self._parse_line(line, data_map)
            self._write_data(data_map)
        finally:
            f.close()

    def _parse_line(self, line: str, data_map: dict):
        tokens = line.split(';')
        if len(tokens) > 5:
            if tokens[1] == self._country:
                data_map[tokens[0]] = (tokens[2])

    def _write_data(self, data_map: dict):
        f = open(self._country + '.data', 'w')
        try:
            for x in sorted(data_map.keys()):
                f.write('{0};{1}\n'.format(x, data_map[x]))
        finally:
            f.close()


def deltaN(n: int):
    n0 = 100
    alpha = 0.05
    delta_t = 1
    return alpha * (n0 - n) * delta_t


def plot():
    n = 1
    data = []
    for i in range(100):
        data.append(n)
        n += deltaN(n)
    plt.plot(data)
    plt.show()


def plot_file(file_name: str):
    f = open(file_name + '.data')
    lines = f.readlines()
    f.close()
    n = 1
    data = []
    for line in lines:
        tokens = line.split(';')
        data.append(float(tokens[1]))
    plt.plot(data)
    plt.show()


def get(country: str):
    db = DataFile('covid19.data')
    db.read(country)
    plot_file(country)


if __name__ == '__main__':
    get('Poland')
    get('Italy')
    get('The United Kingdom')
    get('China')