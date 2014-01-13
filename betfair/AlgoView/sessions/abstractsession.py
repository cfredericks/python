import abc
import wx
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *
from sessionstatusthread import SessionStatusThread


class AbstractSession(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, parent, sessionType, statusPeriodMs=10 * 1000, tickPeriodMs=1 * 1000):
        self.parent = parent
        self.sessionType = sessionType
        self.statusPeriodMs = statusPeriodMs
        self.tickPeriodMs = tickPeriodMs

        self.statusSubject = SUBJECT_STATUS + '.' + self.sessionType.lower()
        pub.subscribe(self.OnSessionStatusPublish, self.statusSubject)

        # Session status publishing timer
        self.tmrSessionStatus = wx.Timer(None)
        self.tmrSessionStatus.Bind(wx.EVT_TIMER, self.OnStatusTimerTimeout, self.tmrSessionStatus)

        # Tick driver
        self.tmrTickDriver = wx.Timer(None)
        self.tmrTickDriver.Bind(wx.EVT_TIMER, self.OnTick, self.tmrTickDriver)

    ######################
    # Abstract methods to override #
    ######################

    # Login to session
    @abc.abstractmethod
    def DoLogin(self, username, password):
        raise Exception("DoLogin not implemented!")

    # Logout of session
    @abc.abstractmethod
    def DoLogout(self):
        raise Exception("DoLogout not implemented!")

    # Get status of session
    @abc.abstractmethod
    def GetSessionStatus(self):
        raise Exception("GetSessionStatus not implemented!")

    # Get prices and other market data
    @abc.abstractmethod
    def GetMarketData(self, marketId):
        raise Exception("GetMarketData not implemented!")

    # Get available markets to trade on
    @abc.abstractmethod
    def DoGetAvailableMarkets(self):
        raise Exception("GetAvailableMarkets not implemented!")

    # Send an order to the session
    @abc.abstractmethod
    def SendTrade(self, data):
        raise Exception("SendTrade not implemented!")

    # Cancel an outstanding order
    @abc.abstractmethod
    def CancelTrade(self, data):
        raise Exception("CancelTrade not implemented!")

    # Modify an outstanding order
    @abc.abstractmethod
    def ModifyTrade(self, data):
        raise Exception("ModifyTrade not implemented!")

    # Get account information for this session
    @abc.abstractmethod
    def GetAccountInfo(self):
        raise Exception("GetAccountInfo not implemented!")

    # Get all outstanding orders
    @abc.abstractmethod
    def GetOutstadingTrades(self):
        raise Exception("GetOutstadingTrades not implemented!")

    # Get information for a specific order
    @abc.abstractmethod
    def GetTradeInfo(self, data):
        raise Exception("GetTradeInfo not implemented!")

    #############
    # Generic actions #
    #############

    def Login(self, username, password):
        if self.DoLogin(username, password):
            pub.sendMessage(self.statusSubject, STATUS_LOGIN)
            self.StartStatusTimer()
            return True
        else:
            msg = 'Unable to login to ' + self.sessionType + ' session'
            wx.MessageBox(msg, 'AlgoView - ' + self.sessionType)
            pub.sendMessage(SUBJECT_STATUSBAR, msg)
            return False

    def Logout(self):
        if self.DoLogout():
            pub.sendMessage(self.statusSubject, STATUS_LOGOUT)
            self.StopStatusTimer()
            return True
        else:
            wx.MessageBox(self.sessionType + ' session logout error', 'AlgoView - ' + self.sessionType)
            return False

    def GetAvailableMarkets(self):
        pub.sendMessage(SUBJECT_STATUSBAR, 'Loading ' + self.sessionType + ' markets...')

        marketsResponse = self.DoGetAvailableMarkets()
        if marketsResponse != None:
            pub.sendMessage(SUBJECT_STATUSBAR, "Found " + str(len(marketsResponse)) + " available markets")
            return marketsResponse
        else:
            wx.MessageBox('Problem retrieving ' + self.sessionType + ' markets', 'AlgoView - ' + self.sessionType)
            pub.sendMessage(SUBJECT_STATUSBAR, 'Problem retrieving ' + self.sessionType + ' markets')
            return None

    def OnSessionStatusPublish(self, status):
        if status.data != STATUS_LOGOUT:
            self.StartStatusTimer()

    #######
    # Timers #
    #######

    def OnStatusTimerTimeout(self, event):
        self.StopStatusTimer()
        SessionStatusThread(self, self)

    def StartStatusTimer(self):
        wx.CallAfter(self.tmrSessionStatus.Start, self.statusPeriodMs)

    def StopStatusTimer(self):
        self.tmrSessionStatus.Stop()

    def StartTickDriver(self):
        wx.CallAfter(self.tmrTickDriver.Start, self.tickPeriodMs)

    def StopTickDriver(self):
        self.tmrTickDriver.Stop()

    def OnTick(self, event):
        pass
