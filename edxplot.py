#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn


def read_data(file_name):
    data_file = open(file_name)

    xs = []
    ys = []

    reading = False
    for line in data_file:

        if reading is True:
            if 'Angle' not in line:
                print(line.strip().split(','))
                x, y = line.strip().split(',')[:2]

                xs.append(float(x))
                ys.append(float(y))

        if '[Data]' in line:
            reading = True

    return xs, ys


if __name__ == "__main__":

    import sys

    xs, ys = read_data(sys.argv[1])

    plt.plot(xs, ys)
    plt.xlabel('Ângulo', fontsize=18)
    plt.ylabel('PSD', fontsize=18)
    plt.tick_params(labelsize=16)
    plt.show()
