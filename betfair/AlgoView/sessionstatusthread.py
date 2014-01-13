from threading import *
from publisherconstants import *


class SessionStatusThread(Thread):
    def __init__(self, notifyWindow, session):
        Thread.__init__(self)
        self.session = session
        self.start()

    def run(self):
        self.session.GetSessionStatus()

    def abort(self):
        pass
