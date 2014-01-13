import bfpy
from wx.lib.pubsub import Publisher as pub
from abstractsession import AbstractSession
from publisherconstants import *


class SimSession(AbstractSession):
    def __init__(self, parent):
        AbstractSession.__init__(self, parent, 'Simulator', 1 * 1000)

        self.parent = parent
        self.loggedIn = False

    # Login to session
    def DoLogin(self, username, password):
        self.loggedIn = True
        return True

    # Logout of session
    def DoLogout(self):
        self.loggedIn = False
        return True

    # Get status of session
    def GetSessionStatus(self):
        if self.loggedIn:
            pub.sendMessage(self.statusSubject, STATUS_LOGGED_IN)
        else:
            pub.sendMessage(self.statusSubject, STATUS_LOGGED_OUT)

    # Get available markets to trade on
    def DoGetAvailableMarkets(self):
        try:
            marketsResponse = self.bfClient.getAllMarkets(bfpy.ExchangeUK)
            if (marketsResponse.errorCode != "OK"):
                return None
            return marketsResponse.marketData
        except:
            return None

    # Get account information for this session
    def GetAccountInfo(self):
        if self.loggedIn:
            return 'Logged in to sim session'
        else:
            return 'Logged out of sim session'

    # Send an order to the session
    def SendTrade(self, data):
        pass

    # Cancel an outstanding order
    def CancelTrade(self, data):
        pass

    # Modify an outstanding order
    def ModifyTrade(self, data):
        pass

    # Get all outstanding orders
    def GetOutstadingTrades(self):
        pass

    # Get information for a specific order
    def GetTradeInfo(self, data):
        pass

    # Get prices and other market data
    def GetMarketData(self, data):
        pass
