import os
import inspect
from algos.abstractalgo import AbstractAlgorithm


class AlgorithmLoader:
    def __init__(self):
        pass

    def findAlgorithms(self):
        # Check for algos
        res = {}

        files = []
        for f in os.listdir("algos"):
            if not os.path.isdir(f) and f[-3:] == '.py':
                files.append(f[:-3])

        for f in files:
            impt = __import__("algos." + f, fromlist=["*"])
            for t in dir(impt):
                if t[:2] != '__':
                    # NOTE: This is a security risk and should be fixed
                    cls = eval("impt." + t)
                    mro = inspect.getmro(cls)
                    if AbstractAlgorithm in mro and mro.index(AbstractAlgorithm) > 0:
                        res[cls] = impt

        return res

    def loadAlgorithms(self):
        algoTypes = self.findAlgorithms()

        algos = []
        for algo in algoTypes:
            algos.append(algo())
            #print "Found algo:", algos[-1].name, "::", algos[-1].description

        return algos
