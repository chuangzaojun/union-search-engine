import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="Union Search Engine", style=wx.DEFAULT_FRAME_STYLE, size=(800,600))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="Union Search Engine")
        self.title.SetFont(wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.title.SetPosition((20,20))

        self.search_box = wx.TextCtrl(panel, value="", size=(700,40), style=wx.TE_PROCESS_ENTER)
        self.search_box.SetPosition((20,80))
        self.search_box.Bind(wx.EVT_TEXT_ENTER, self.on_search)

        self.search_button = wx.Button(panel, label="Search", size=(100,40))
        self.search_button.SetPosition((730,80))
        self.search_button.Bind(wx.EVT_BUTTON, self.on_search)

        self.result_text = wx.StaticText(panel, label="", size=(780,400), style=wx.ALIGN_LEFT)
        self.result_text.SetPosition((20,130))
        self.result_text.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.result_text.Wrap(760)


    def on_search(self, event):
        query = self.search_box.GetValue()
        if query:
            self.result_text.SetLabel("Searching...")
            # TODO: Implement search engine here
            self.result_text.SetLabel("No results found for \"" + query + "\"")
        else:
            self.result_text.SetLabel("")
