import time

from WordCounter import WordCounter


# Author : Alex Fernández Ocón

class Words(WordCounter):
    def __init__(self, threads):
        super().__init__(threads)

    def mapLine(self):
        # While the queue is not empty process the pack of lines
        while not self.q.empty():
            lines = self.q.get()
            for line in lines:
                for word in line.split():
                    letterCheck = []
                    # We count per word so we increase total here
                    self.total = self.total + 1
                    for letter in word.lower():
                        if letter not in letterCheck and letter.isalpha():
                            letterCheck.append(letter)
                            self.map.append(letter)

            self.q.task_done()

    # To use the algorithm word.execute(path)
    def execute(self, path):
        self.map = []
        self.rate = {}
        self.total = 0
        initial = time.time()
        super().read(path)
        super().createThreads(path)
        final = time.time()
        #print("Map Duration:", final - initial)

        initial = time.time()
        super().shuffle()
        final = time.time()
        #print("Shuffle Duration:", final - initial)

        initial = time.time()
        super().operation(path)
        final = time.time()
        #print("Reduce Duration:", final - initial)
        return self.rate
