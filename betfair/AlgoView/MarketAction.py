class MarketActionState:
    REQUEST = 1
    ACK = 2
    REJECT = 3
    PARTIAL = 4
    COMPLETE = 5


class MarketActionType:
    NEW = 1
    CANCEL = 2
    MODIFY = 3


class MarketActionSide:
    BACK = 1
    LAY = 2


class MarketAction:
    # long id
    # long ticks
    # MarketActionState state
    # MarketActionType type
    # double price
    # double size
    # MarketActionSide side

    def __init__(self, size, price, side, type, state, ticks, id):
        self.size = size
        self.price = price
        self.side = side
        self.state = state
        self.type = type
        self.ticks = ticks
        self.id = id


class MarketDatum:
    # long id
    # long ticks
    # long runnerId
    # double[] pricesToBack
    # double[] valuesToBack
    # double[] pricesToLay
    # double[] valuesToLay

    def __init__(self, runnerId, runnerName, pricesToBack, valuesToBack, pricesToLay, valuesToLay, ticks, id):
        self.runnerId = runnerId
        self.runnerName = runnerName
        self.pricesToBack = pricesToBack
        self.valuesToBack = valuesToBack
        self.pricesToLay = pricesToLay
        self.valuesToLay = valuesToLay
        self.ticks = ticks
        self.id = id

    def __str__(self):
        return ('MarketDatum{' +
            'ID:' + str(self.id) +
            ', Ticks:' + str(self.ticks) +
            ', Runner:' + self.runnerName + ' (' + str(self.runnerId) + ')' +
            ', BackPrices:' + str(self.pricesToBack) +
            ', BackValues:' + str(self.valuesToBack) +
            ', LayPrices:' + str(self.pricesToLay) +
            ', LayValues:' + str(self.valuesToLay) +
            '}')
