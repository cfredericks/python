import os
import inspect
from sessions.abstractsessionpanel import AbstractSessionPanel


class SessionLoader:
    def __init__(self, parent):
        self.parent = parent

    def findSessions(self):
        # Check for sessions
        res = {}

        files = []
        for f in os.listdir("sessions"):
            if not os.path.isdir(f) and f[-3:] == '.py':
                files.append(f[:-3])

        for f in files:
            impt = __import__("sessions." + f, fromlist=["*"])
            for t in dir(impt):
                if t[:2] != '__' and inspect.isclass(eval("impt." + t)):
                    # NOTE: This is a security risk and should be fixed
                    cls = eval("impt." + t)
                    mro = inspect.getmro(cls)
                    if AbstractSessionPanel in mro and mro.index(AbstractSessionPanel) > 0:
                        res[cls] = impt

        return res

    def loadSessions(self):
        sessionTypes = self.findSessions()

        sessions = []
        for session in sessionTypes:
            sessions.append(session(self.parent))
            #print "Found session:", sessions[-1].name, "::", sessions[-1].description

        return sessions
