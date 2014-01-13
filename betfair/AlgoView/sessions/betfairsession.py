import bfpy
from wx.lib.pubsub import Publisher as pub
from abstractsession import AbstractSession
from publisherconstants import *


class BetfairSession(AbstractSession):
    def __init__(self, parent):
        AbstractSession.__init__(self, parent, 'Betfair', 10 * 1000)

        self.parent = parent
        self.bfClient = bfpy.BfClient()

    # Login to session
    def DoLogin(self, username, password):
        try:
            self.bfClient.login(username=username, password=password)
            return True
        except:
            return False

    # Logout of session
    def DoLogout(self):
        try:
            self.bfClient.logout()
            return True
        except:
            return False

    # Get status of session
    def GetSessionStatus(self):
        try:
            bfResp = self.bfClient.keepAlive()
        except:
            pub.sendMessage(self.statusSubject, STATUS_ERROR)
        else:
            if bfResp.header.errorCode == 'OK':
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
        try:
            result = self.bfClient.getAccountFunds(bfpy.ExchangeUK)
            return str(result)
        except:
            return None

    # Get prices and other market data
    def GetMarketData(self, marketId):
        return self.bfClient.getMarketPrices(bfpy.ExchangeUK, marketId=marketId)

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
