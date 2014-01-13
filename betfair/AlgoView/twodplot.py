import wx
import sys

years = ('2003', '2004', '2005')


class TwoDPlot(wx.Panel):
    def __init__(self, parent, chartTitle, data):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('WHITE')

        self.title = chartTitle
        self.SetData(data)

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def SetData(self, data):
        xmin = sys.maxint
        xmax = -sys.maxint - 1
        ymin = sys.maxint
        ymax = -sys.maxint - 1
        for d in data:
            if d[0] < xmin:
                xmin = d[0]
            if d[0] > xmax:
                xmax = d[0]
            if d[1] < ymin:
                ymin = d[1]
            if d[1] > ymax:
                ymax = d[1]

        self.data = data
        self.xlimits = (xmin, xmax)
        self.ylimits = (ymin, ymax)

        #self.Repaint()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetDeviceOrigin(40, 240)
        dc.SetAxisOrientation(True, True)
        dc.SetPen(wx.Pen('WHITE'))
        dc.DrawRectangle(1, 1, 300, 200)
        self.DrawAxis(dc)
        self.DrawGrid(dc)
        self.DrawTitle(dc)
        self.DrawData(dc)

    def DrawAxis(self, dc):
        dc.SetPen(wx.Pen('#0AB1FF'))
        font = dc.GetFont()
        font.SetPointSize(8)
        dc.SetFont(font)
        dc.DrawLine(1, 1, 300, 1)
        dc.DrawLine(1, 1, 1, 201)

        for i in range(20, 220, 20):
            dc.DrawText(str(i), -30, i + 5)
            dc.DrawLine(2, i, -5, i)

        for i in range(100, 300, 100):
            dc.DrawLine(i, 2, i, -5)

        for i in range(3):
            dc.DrawText(years[i], i * 100 - 13, -10)

    def DrawGrid(self, dc):
        dc.SetPen(wx.Pen('#d5d5d5'))

        for i in range(20, 220, 20):
            dc.DrawLine(2, i, 300, i)

        for i in range(100, 300, 100):
            dc.DrawLine(i, 2, i, 200)

    def DrawTitle(self, dc):
        font = dc.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)
        dc.DrawText(self.title, 90, 235)

    def DrawData(self, dc):
        dc.SetPen(wx.Pen('#0ab1ff'))
        for i in range(10, 310, 10):
            dc.DrawSpline(self.data)


class TwoDChartExample(wx.Frame):
    def __init__(self, parent, id, winTitle, chartTitle):
        wx.Frame.__init__(self, parent, id, winTitle, size=(390, 300))

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('WHITE')

        data = ((10, 9), (20, 22), (30, 21), (40, 30), (50, 41),
                (60, 53), (70, 45), (80, 20), (90, 19), (100, 22),
                (110, 42), (120, 62), (130, 43), (140, 71), (150, 89),
                (160, 65), (170, 126), (180, 187), (190, 128), (200, 125),
                (210, 150), (220, 129), (230, 133), (240, 134), (250, 165),
                (260, 132), (270, 130), (280, 159), (290, 163), (300, 94))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        linechart = TwoDPlot(panel, chartTitle, data)
        hbox.Add(linechart, 1, wx.EXPAND | wx.ALL, 15)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App(redirect=False)
    TwoDChartExample(None, -1, 'A line chart', 'Historical Prices')
    app.MainLoop()
