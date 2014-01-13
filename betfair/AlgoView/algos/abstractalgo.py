import abc
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *


class AbstractAlgorithm(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, algoId, name="Undefined", description=""):
        self.name = name
        self.description = description

        # should be unique
        self.id = id

        # Listeners
        pub.subscribe(self.OnNewMarketData, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnAck, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnMatched, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnReject, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnPartial, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnComplete, SUBJECT_STATUSBAR)

        # Unique marketActionId
        self.marketActionId = 0

        # MarketAction cache

    @abc.abstractmethod
    def Start(self):
        raise Exception("Start not implemented!")

    @abc.abstractmethod
    def Stop(self):
        raise Exception("Stop not implemented!")

    # @param args Array of MarketDatum's with the same timestamp
    # return Array of MarketAction's that will be used to call Session callbacks
    @abc.abstractmethod
    def OnNewMarketData(self, args):
        self.marketActionId = self.marketActionId + 1
        raise Exception("OnNewMarketData not implemented!")

    @abc.abstractmethod
    def OnAck(self, actionId):
        raise Exception("OnAck not implemented!")

    @abc.abstractmethod
    def OnMatched(self, actionId):
        raise Exception("OnMatched not implemented!")

    @abc.abstractmethod
    def OnReject(self, actionId, errorText):
        raise Exception("OnReject not implemented!")

    @abc.abstractmethod
    def OnPartial(self, actionId, amount):
        raise Exception("OnPartial not implemented!")

    @abc.abstractmethod
    def OnComplete(self, actionId):
        raise Exception("OnComplete not implemented!")
