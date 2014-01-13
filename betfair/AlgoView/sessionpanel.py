import wx
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *
from sessionloader import SessionLoader
from algomanagementpanel import AlgoManagementPanel


class SessionPanel(wx.Panel):
    def __init__(self, parent):
        super(SessionPanel, self).__init__(parent)

        self.parent = parent
        self.stopTabSwitching = False
        self.currentSession = None

        pub.subscribe(self.OnSessionStatusPublish, SUBJECT_STATUS)

        self.InitUI()
        self.sessionLoader = SessionLoader(self.nbSessionTabs)
        self.LoadSessions()

    def InitUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.nbSessionTabs = wx.Notebook(self, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        sizer.Add(self.nbSessionTabs, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnSessionTabChange)

    def AddSessionTabs(self):
        for i in range(len(self.sessions)):
            self.nbSessionTabs.AddPage(self.sessions[i], self.sessions[i].session.sessionType)

    def LoadSessions(self):
        pub.sendMessage(SUBJECT_STATUSBAR, 'Loading available sessions...')
        self.sessions = self.sessionLoader.loadSessions()
        pub.sendMessage(SUBJECT_STATUSBAR, 'Found ' + str(len(self.sessions)) + ' sessions')
        self.AddSessionTabs()

    def OnSessionStatusPublish(self, status):
        tabName = self.nbSessionTabs.GetCurrentPage().session.sessionType + ' Management'

        if status.data == STATUS_LOGIN or status.data == STATUS_LOGGED_IN:
            self.currentSession = self.nbSessionTabs.GetCurrentPage().session

            if self.stopTabSwitching == False:
                self.parent.InsertPage(1, AlgoManagementPanel(self.parent, self.currentSession), tabName)
                self.parent.SetSelection(1)

            self.stopTabSwitching = True
        elif status.data == STATUS_LOGOUT or status.data == STATUS_LOGGED_OUT:
            if self.stopTabSwitching == True:
                for i in range(self.parent.GetPageCount()):
                    if self.parent.GetPageText(i) == tabName:
                        self.parent.RemovePage(i)
                        break

            self.currentSession = None
            self.stopTabSwitching = False

    def OnSessionTabChange(self, event):
        if self.stopTabSwitching:
            event.Veto()
        else:
            event.Skip()
