import wx


class SummaryPanel(wx.Panel):
    def __init__(self, parent):
        super(SummaryPanel, self).__init__(parent)

        self.InitUI()

    def InitUI(self):
        vbox1 = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(vbox1)
