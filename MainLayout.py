import wx

class Interface(wx.Frame):
    def __init__(self, *args,**kwds):
        super(Interface, self).__init__(*args,**kwds)
        self.SetTitle("Main Layout PMC Software")
        self.SetSize((500,300))
        self.Center()
        # Show the window on screen
        #self.Show()

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    frame = Interface(None)
    frame.Show(True)
    app.MainLoop()