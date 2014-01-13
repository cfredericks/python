import wx
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *
from betfairsession import BetfairSession
from abstractsessionpanel import AbstractSessionPanel

# Event IDs
ID_LOGIN = wx.NewId()
ID_LOGOUT = wx.NewId()
ID_ACCOUNT_INFO = wx.NewId()


class BetfairSessionPanel(AbstractSessionPanel):
    def __init__(self, parent):
        super(BetfairSessionPanel, self).__init__(parent, BetfairSession(parent))
        self.InitUI()

    def InitUI(self):
        vbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Username:', size=wx.Size(60, 20))
        hbox1.Add(st1)
        self.txtUser = wx.TextCtrl(self, value="USER", size=wx.Size(200, 20))
        hbox1.Add(self.txtUser)
        vbox1.Add(hbox1, border=10)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(self, label='Password:', size=wx.Size(60, 20))
        hbox2.Add(st2)
        self.txtPass = wx.TextCtrl(self, value="PASSWORD", size=wx.Size(200, 20), style=wx.TE_PASSWORD)
        hbox2.Add(self.txtPass)
        vbox1.Add(hbox2, border=10)

        vbox1.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.btnLogout = wx.Button(self, ID_LOGOUT, "Logout")
        self.btnLogout.Enabled = False
        hbox3.Add(self.btnLogout)
        self.btnLogin = wx.Button(self, ID_LOGIN, "Login")
        hbox3.Add(self.btnLogin)
        vbox1.Add(hbox3)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.btnAccountInfo = wx.Button(self, ID_ACCOUNT_INFO, "Get Account Info")
        self.btnAccountInfo.Enabled = False
        hbox4.Add(self.btnAccountInfo)
        vbox1.Add(hbox4)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.txtAccountInfo = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE)
        hbox5.Add(self.txtAccountInfo, proportion=1, flag=wx.EXPAND)
        vbox1.Add(hbox5, proportion=1, flag=wx.EXPAND)

        self.SetSizer(vbox1)

        pub.subscribe(self.OnSessionStatusPublish, SUBJECT_STATUS)

        # Event handlers
        self.Bind(wx.EVT_BUTTON, self.OnLoginBetfair, id=ID_LOGIN)
        self.Bind(wx.EVT_BUTTON, self.OnLogoutBetfair, id=ID_LOGOUT)
        self.Bind(wx.EVT_BUTTON, self.OnAccountInfo, id=ID_ACCOUNT_INFO)

    def OnLoginBetfair(self, event):
        self.session.Login(username=self.txtUser.GetValue(), password=self.txtPass.GetValue())

    def OnLogoutBetfair(self, event):
        self.session.Logout()

    def OnSessionStatusPublish(self, status):
        if status.data != STATUS_LOGGED_IN and status.data != STATUS_LOGIN and \
           status.data != STATUS_LOGGED_OUT and status.data != STATUS_LOGOUT:
            return

        self.txtUser.Enabled = False
        self.txtPass.Enabled = False
        self.btnLogin.Enabled = False
        self.btnLogout.Enabled = False
        self.btnAccountInfo.Enabled = False

        if status.data == STATUS_LOGGED_IN or status.data == STATUS_LOGIN:
            self.btnLogout.Enabled = True
            self.btnAccountInfo.Enabled = True
        else:
            self.txtUser.Enabled = True
            self.txtPass.Enabled = True
            self.btnLogin.Enabled = True

    def OnAccountInfo(self, event):
        bfResp = self.session.GetAccountInfo()
        if bfResp != None:
            self.txtAccountInfo.SetValue(str(bfResp))
        else:
            self.txtAccountInfo.SetValue('')
