from abstractalgo import AbstractAlgorithm


class TestAlgorithm(AbstractAlgorithm):
    def __init__(self, algoId):
        AbstractAlgorithm.__init__(self, algoId, "Test Algorithm",
            "This algorithm is for algorithms in test")

    def Run(self):
            return "Test algorithm"
