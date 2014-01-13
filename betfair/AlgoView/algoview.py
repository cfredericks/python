import wx
from sessionpanel import SessionPanel
from summarypanel import SummaryPanel
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *

# Event IDs
ID_MENU_QUIT = wx.NewId()


class AlgorithmView(wx.Frame):
    def __init__(self, parent, title):
        super(AlgorithmView, self).__init__(parent, title=title, size=(900, 600))
        self.SetMinSize(wx.Size(600, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        # Menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.Append(ID_MENU_QUIT, 'Quit', '')
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        # Status bar
        self.CreateStatusBar()
        self.GetStatusBar().SetFieldsCount(3)

        self.nbAlgoTabs = wx.Notebook(self, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        # Session tab
        self.pnlSession = SessionPanel(self.nbAlgoTabs)
        self.nbAlgoTabs.AddPage(self.pnlSession, "Session")

        # Summary tab
        self.pnlSummary = SummaryPanel(self.nbAlgoTabs)
        self.nbAlgoTabs.AddPage(self.pnlSummary, "Summary")

        pub.subscribe(self.OnStatusBarPublish, SUBJECT_STATUSBAR)
        pub.subscribe(self.OnSessionStatusPublish, SUBJECT_STATUS)

        # Event handlers
        self.Bind(wx.EVT_MENU, self.OnQuit, id=ID_MENU_QUIT)

    def OnQuit(self, event):
        self.Close()

    def OnStatusBarPublish(self, msg, index=0):
        self.GetStatusBar().PushStatusText(msg.data, index)

    def OnSessionStatusPublish(self, status):
        # No response
        if status.data == STATUS_ERROR:
            self.GetStatusBar().PushStatusText("Network problem", 2)
        # Running sims
        elif status.data == STATUS_SIM:
            self.GetStatusBar().PushStatusText("Running simulations", 2)
        # Just established Betfair login
        elif status.data == STATUS_LOGIN:
            self.GetStatusBar().PushStatusText("Logged in", 2)
        # Still logged in
        elif status.data == STATUS_LOGGED_IN:
            self.GetStatusBar().PushStatusText("Logged in", 2)
        # Just logged off
        elif status.data == STATUS_LOGOUT:
            self.GetStatusBar().PushStatusText("Logged out", 2)
        # Not logged in
        elif status.data == STATUS_LOGGED_OUT:
            self.GetStatusBar().PushStatusText("Logged out", 2)
        else:
            self.GetStatusBar().PushStatusText("Disconnected", 2)

if __name__ == '__main__':
    app = wx.App(redirect=False)
    AlgorithmView(None, title='Algorithm View')
    app.MainLoop()
