import sys

from words import Words
from histograma import Histograma


def main():
    threads = 1
    option = 0
    move = 1
    if len(sys.argv) > 1:
        if "-t" in sys.argv:
            pos = sys.argv.index("-t")
            threads = int(sys.argv[pos + 1])
            move += 2
        if "-h" in sys.argv:
            option += 1
            move += 1
        if option == 0:
            alg = Words(threads)
        else:
            alg = Histograma(threads)
        files = sys.argv[move:]
        for file in files:
            alg.execute(file)

    # 7m 30s  1t
    # 5m 30s  8t


if __name__ == '__main__':
    sys.exit(main())
