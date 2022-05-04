import os
import logging
import threading
import queue
import concurrent.futures
import time

from WordCounter import WordCounter


class Histograma(WordCounter):
    def __init__(self, threads):
        super().__init__(threads)

    def mapLine(self):
        while not self.q.empty():
            lines = self.q.get()
            for line in lines:
                for word in line.split():
                    letterCheck = []
                    for letter in word.lower():
                        self.total = self.total + 1
                        if letter not in letterCheck and letter.isalpha():
                            letterCheck.append(letter)
                            self.map.append(letter)

            self.q.task_done()

    def execute(self, path):
        self.map = []
        self.rate = {}
        self.total = 0
        initial = time.time()
        super().read(path)
        super().createThreads(path)
        final = time.time()
        print("Map Duration:", final - initial)

        initial = time.time()
        super().shuffle()
        final = time.time()
        print("Shuffle Duration:", final - initial)

        initial = time.time()
        super().operation(path)
        final = time.time()
        print("Reduce Duration:", final - initial)
        print(path)
        print(self.rate)
        return self.rate

