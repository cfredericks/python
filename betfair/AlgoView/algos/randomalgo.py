from abstractalgo import AbstractAlgorithm


class RandomAlgorithm(AbstractAlgorithm):
    def __init__(self, algoId):
        AbstractAlgorithm.__init__(self, algoId, "Random Algorithm",
            "This algorithm makes random trading decisions for testing sims")

    def Run(self):
            return "Random algorithm"
