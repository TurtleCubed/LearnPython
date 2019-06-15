
import wx


class ShinySorter(wx.Frame):
    def __init__(self, parent, title):
        super(ShinySorter, self).__init__(parent, title=title, size=(500, 600))

        self.pnl = wx.Panel(self)
        self.image_size = 200
        self.image_number = 1
        self.num_nah = 0
        self.num_green = 0
        self.normal = None
        self.shiny = None
        self.nah_text = None
        self.green_text = None

        self.create_window()

    def create_window(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        header = wx.StaticText(self.pnl, label="Is the Shiny Green or Nah?", style=wx.ALIGN_CENTER)
        font = header.GetFont()
        font.PointSize += 10
        font = font.Bold()
        header.SetFont(font)
        header.SetForegroundColour((50, 225, 50))
        vbox.Add(header, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        normal_image = wx.Image("Sprites\\BW\\1.png", wx.BITMAP_TYPE_ANY)
        normal_image.Rescale(self.image_size, self.image_size)
        shiny_image = wx.Image("Sprites\\ShinyBW\\1s.png", wx.BITMAP_TYPE_ANY)
        shiny_image.Rescale(self.image_size, self.image_size)
        self.normal = wx.StaticBitmap(self.pnl, wx.ID_ANY, wx.Bitmap(normal_image))
        self.shiny = wx.StaticBitmap(self.pnl, wx.ID_ANY, wx.Bitmap(shiny_image))
        image_row = wx.BoxSizer(wx.HORIZONTAL)
        image_row.Add(self.normal, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        image_row.Add(self.shiny, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        vbox.Add(image_row, 2, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.nah_text = wx.StaticText(self.pnl, label=str(self.num_nah), style=wx.ALIGN_CENTER)
        self.nah_text.SetFont(font)
        self.green_text = wx.StaticText(self.pnl, label=str(self.num_green), style=wx.ALIGN_CENTER)
        self.green_text.SetFont(font)
        self.green_text.SetForegroundColour((50, 225, 50))
        number_row = wx.BoxSizer(wx.HORIZONTAL)
        number_row.Add(self.nah_text, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        number_row.Add(self.green_text, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(number_row, 3, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

        nah_button = wx.Button(self.pnl, size=wx.DefaultSize, id=0, label="Nah")
        green_button = wx.Button(self.pnl, size=wx.DefaultSize, id=1, label="Green")
        green_button.SetForegroundColour((50, 225, 50))
        button_row = wx.BoxSizer(wx.HORIZONTAL)
        button_row.Add(nah_button, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        button_row.Add(green_button, wx.ID_ANY, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 0)
        vbox.Add(button_row, 4, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 20)

        nah_button.Bind(wx.EVT_BUTTON, self.update_frame)
        green_button.Bind(wx.EVT_BUTTON, self.update_frame)

        self.pnl.SetSizer(vbox)
        self.Center()
        self.Show()

    def update_frame(self, event):
        btn = event.GetEventObject().GetLabel()
        if btn == "Nah":
            self.num_nah += 1
        else:
            self.num_green += 1
        self.image_number += 1
        normal_image = wx.Image("Sprites\\BW\\" + str(self.image_number) + ".png", wx.BITMAP_TYPE_ANY)
        normal_image.Rescale(self.image_size, self.image_size)
        shiny_image = wx.Image("Sprites\\ShinyBW\\" + str(self.image_number) + "s.png", wx.BITMAP_TYPE_ANY)
        shiny_image.Rescale(self.image_size, self.image_size)
        self.normal.SetBitmap(wx.Bitmap(normal_image))
        self.shiny.SetBitmap(wx.Bitmap(shiny_image))
        self.nah_text.SetLabel(str(self.num_nah))
        self.green_text.SetLabel(str(self.num_green))

        self.pnl.Refresh()


app = wx.App()
frm = ShinySorter(None, title="ShinySorter")
frm.Show()
app.MainLoop()
