from abstractalgo import AbstractAlgorithm


class SingleMarketAlgorithm(AbstractAlgorithm):
    def __init__(self, algoId):
        AbstractAlgorithm.__init__(self, algoId, "Single Market Algorithm",
            "This is a simple algorithm that buys low and sells high")

    def Run(self):
            return "Single-market algorithm"
