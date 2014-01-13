import wx
from algoloader import AlgorithmLoader
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *

# Event IDs
ID_LOAD_ALGOS = wx.NewId()
ID_LOAD_MARKETS = wx.NewId()


class AlgoManagementPanel(wx.Panel):
    def __init__(self, parent, session):
        super(AlgoManagementPanel, self).__init__(parent)

        self.session = session
        self.InitUI()

        # Load available trading algorithms
        self.LoadAlgos()
        self.LoadMarkets()

    def InitUI(self):
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        # Refresh image for adding to refresh buttons
        bitmapRefresh = wx.Bitmap('img/refresh.png')
        image = wx.ImageFromBitmap(bitmapRefresh)
        image = image.Scale(16, 16, wx.IMAGE_QUALITY_HIGH)
        bitmapRefresh = wx.BitmapFromImage(image)

        vbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Available Algorithms')
        st1.SetFont(font)
        hbox1.Add(st1)
        btnRefreshAlgos = wx.BitmapButton(self, ID_LOAD_ALGOS, bitmapRefresh)
        hbox1.Add(btnRefreshAlgos, flag=wx.RIGHT | wx.TOP)
        vbox1.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)

        vbox1.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.lstAlgos = wx.ListBox(self, -1)
        hbox2.Add(self.lstAlgos, proportion=1, flag=wx.EXPAND)
        vbox1.Add(hbox2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox1.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(self, label='Available ' + self.session.sessionType + ' Markets')
        st2.SetFont(font)
        hbox3.Add(st2)
        btnRefreshMarkets = wx.BitmapButton(self, ID_LOAD_MARKETS, bitmapRefresh)
        hbox3.Add(btnRefreshMarkets, flag=wx.RIGHT | wx.TOP)
        vbox1.Add(hbox3, flag=wx.LEFT, border=10)

        vbox1.Add((-1, 10))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.treeMarkets = wx.TreeCtrl(self, 1, wx.DefaultPosition, (-1, -1), wx.TR_HAS_BUTTONS | wx.TR_MULTIPLE)
        hbox4.Add(self.treeMarkets, proportion=1, flag=wx.EXPAND)
        vbox1.Add(hbox4, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        self.SetSizer(vbox1)

        # Event handlers
        self.Bind(wx.EVT_BUTTON, self.OnLoadAlgos, id=ID_LOAD_ALGOS)
        self.Bind(wx.EVT_BUTTON, self.OnLoadMarkets, id=ID_LOAD_MARKETS)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnMarketSelected, self.treeMarkets)

    def OnLoadAlgos(self, event):
        self.LoadAlgos()

    def OnLoadMarkets(self, event):
        self.LoadMarkets()

    def LoadAlgos(self):
        pub.sendMessage(SUBJECT_STATUSBAR, "Loading trading algorithms...")

        self.algos = AlgorithmLoader().loadAlgorithms()

        self.lstAlgos.Clear()
        for algo in self.algos:
            self.lstAlgos.Append(algo.name + " - " + algo.description)

        pub.sendMessage(SUBJECT_STATUSBAR, "Found " + str(len(self.algos)) + " available algorithms")
        return True

    def LoadMarkets(self):
        self.markets = self.session.GetAvailableMarkets()

        if self.markets == None:
            return False

        self.treeMarkets.DeleteAllItems()
        root = self.treeMarkets.AddRoot('Markets')

        # Add all markets to the tree
        items = {}
        for market in self.markets:
            path = ''
            parent = root
            # Iterate over the market path
            for item in market.menuPathParts:
                path = path + item
                if path in items:
                    parent = items[path]
                    continue
                # Add this node if it doesn't exist
                parent = items[path] = self.treeMarkets.AppendItem(parent, item)
            # After all of the parent nodes are present, at the market type
            items[path + market.marketName] = self.treeMarkets.AppendItem(items[path], market.marketName)
            # Attach the market information to the tree object for extraction later
            self.treeMarkets.SetPyData(items[path + market.marketName], market)

        self.treeMarkets.Expand(root)

        pub.sendMessage(SUBJECT_STATUSBAR,
            'Found ' + str(len(self.markets)) + ' available ' + self.session.sessionType + ' markets')

        return True

    def OnMarketSelected(self, event):
        selected = event.GetItem()
        if self.treeMarkets.GetChildrenCount(selected) == 0:
            mId = self.treeMarkets.GetPyData(selected).marketId
            wx.MessageBox(str(self.treeMarkets.GetPyData(selected)), 'AlgoView')
            #print self.bfClient.getMarket(bfpy.ExchangeUK, marketId=mId)
            print self.session.GetMarketData(marketId=mId)
            ##print self.bfClient.getMarketPricesCompressed(bfpy.ExchangeUK, marketId=mId)
            #print self.bfClient.getMUBets(bfpy.ExchangeUK, marketId=mId, betStatus='MU')
            ##print self.bfClient.getMUBetsLite(bfpy.ExchangeUK, marketId=mId, betStatus='MU')
            #print self.bfClient.getMarketProfitAndLoss(bfpy.ExchangeUK, marketId=mId)
            #print self.bfClient.getCompleteMarketPricesCompressed(bfpy.ExchangeUK, marketId=mId)
            #print self.bfClient.getDetailAvailableMarketDepth(bfpy.ExchangeUK, marketId=mId, selectionId=55190)
            ##print self.bfClient.getMarketTradedVolume(bfpy.ExchangeUK, marketId=mId, selectionId=55190)
            #print self.bfClient.getMarketTradedVolumeCompressed(bfpy.ExchangeUK, marketId=mId)
            # TODO(coreyf): Show market information in GUI
        else:
            event.Skip()
