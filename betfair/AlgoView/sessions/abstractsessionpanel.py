import wx
from wx.lib.pubsub import Publisher as pub
from publisherconstants import *


class AbstractSessionPanel(wx.Panel):
    def __init__(self, parent, session):
        super(AbstractSessionPanel, self).__init__(parent)
        self.session = session
        pub.subscribe(self.OnSessionStatusPublish, SUBJECT_STATUS)

    def OnSessionStatusPublish(self, status):
        pass
