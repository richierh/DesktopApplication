import wx

class Interface(wx.Frame):
    def __init__(self, *args,**kwds):
        super(Interface, self).__init__(*args,**kwds)
        self.SetTitle("Main Layout PMC Software")
        self.SetSize((500,300))
        self.Center()

        self.Sizer=wx.BoxSizer(wx.VERTICAL)

        self.Panel1 = wx.Panel(self,size=(300,300))
        self.Panel1.SetBackgroundColour("BLUE")



        self.Sizer2 = wx.FlexGridSizer(2,0,0,0)
        self.TextCtrl1 = wx.StaticText(self.Panel1,label="Okay")
        self.Font= wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False ) 	
        self.TextCtrl1.SetFont(self.Font)
        self.TextCtrl2 = wx.StaticText(self.Panel1,label="Terima")

        self.Sizer2.Add(self.TextCtrl1,wx.EXPAND)
        self.Sizer2.Add(self.TextCtrl2,wx.EXPAND)
        self.Panel1.SetSizer(self.Sizer2)

        self.SetSizer(self.Sizer)
        self.Sizer.Add(self.Panel1,wx.EXPAND)

        # Show the window on screen
        #self.Show()

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    frame = Interface(None)
    frame.Show(True)
    app.MainLoop()