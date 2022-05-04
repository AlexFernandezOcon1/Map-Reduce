import sys

from words import Words
from histograma import Histogram


# Author : Alex Fernández Ocón

def main():
    threads = 2
    option = 0
    move = 1
    if len(sys.argv) > 1:
        # -t indicates the amount of threads used
        if "-t" in sys.argv:
            pos = sys.argv.index("-t")
            threads = int(sys.argv[pos + 1])
            move += 2
        # -h indicates that you want to use Histograma
        if "-h" in sys.argv:
            option += 1
            move += 1
        if option == 0:
            alg = Words(threads)
        else:
            alg = Histogram(threads)
        files = sys.argv[move:]
        for file in files:
            alg.execute(file)

    # 7m 30s  1t
    # 5m 30s  8t


if __name__ == '__main__':
    sys.exit(main())
