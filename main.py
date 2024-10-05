import jieba

import wx

from core import Engine
from shell import Shell
from gui import MyFrame

if __name__ == "__main__":

    engine = Engine()
    shell = Shell(engine)
    shell.run()

    # app = wx.App()
    # frame = MyFrame(None, -1)
    # frame.Show(True)
    # app.MainLoop()