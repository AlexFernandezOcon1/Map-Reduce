import os
import logging
import threading
import queue


class WordCounter:
    def __init__(self, threads):

        self.nThreads = threads
        self.rate = {}
        self.total = 0
        self.q = queue.Queue()
        self.map = []

    def createThreads(self, path):
        thread = list()
        for i in range(self.nThreads):
            # makes the thread work on map
            t = threading.Thread(target=self.mapLine, daemon=True)
            thread.append(t)
            t.start()
        self.q.join()

    def read(self, path):
        logging.info("Reading file %s", path)
        with open(path, "r", encoding='utf8') as f:
            count = 1
            work = []
            for line in f:
                count = count + +1
                # group lines in packs of 100 to reduce the amount of access to the queue
                if count % 100 == 0:
                    self.q.put(work)
                    work = []
                work.append(line)
            if len(work) > 0:
                self.q.put(work)

    def shuffle(self):
        for value in self.map:
            if value in self.rate:
                self.rate[value] += 1
            else:
                self.rate[value] = 1

    def check_file(self, path):
        if os.path.exists(path):
            logging.warning("Removing last file")
            os.remove(path)

    def operation(self, path):
        resultPath = path[:-4] + "_result.txt"
        self.check_file(resultPath)
        f = open(resultPath, "w", encoding="utf8")
        f.write(resultPath + "\n")
        logging.info("Executing operation")
        self.rate = {key: (value / self.total * 100) for (key, value) in self.rate.items()}
        [f.write(key + " : " + "{:.2f}".format(value) + "% \n") for key, value in self.rate.items()]
        f.close()
