#!/usr/bin/env python
###############################################################################################
#
# @file      StrFunc.py
# @author    Tristan Yoo (tristan.yoo@gmail.com)
# @date      June 10, 2019
# @brief     A GUI that converts an entered string to one of four options
#
# @copyright Copyright (c) 2019 Tristan Yoo
#
###############################################################################################

import wx
import StrFunc


class StringButtons(wx.Frame):
    def __init__(self, parent, title):
        super(StringButtons, self).__init__(parent, title=title, size=(500, 300))

        # make the panel on which buttons and boxes will be placed on
        pnl = wx.Panel(self)
        # use a BoxSizer to make the layout nice
        vertbox = wx.BoxSizer(wx.VERTICAL)
        # ask for user input
        prompt = wx.StaticText(pnl, label="Enter a sentence", style=wx.ALIGN_CENTER)
        vertbox.Add(prompt, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        # text box
        self.enter_text1 = wx.TextCtrl(pnl, pos=(10, 10), name="GetTextFromUserPromptStr", value="default value")
        vertbox.Add(self.enter_text1, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        # buttons
        cap_button = wx.Button(pnl, id=0, label="CAPITALIZE EACH LETTER")
        rev_button = wx.Button(pnl, id=1, label="words the Reverse")
        ver_button = wx.Button(pnl, id=2, label="gnirts eht esreveR")
        red_button = wx.Button(pnl, id=3, label="Make it red")
        red_button.SetLabelMarkup("Make it <span foreground='red'>red</span>")
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(cap_button, -1, wx.ALL, 5)
        hbox1.Add(rev_button, -1, wx.ALL, 5)
        hbox2.Add(ver_button, -1, wx.ALL, 5)
        hbox2.Add(red_button, -1, wx.ALL, 5)
        vertbox.Add(hbox1, 2, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        vertbox.Add(hbox2, 2, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

        cap_button.Bind(wx.EVT_BUTTON, self.OnClicked)
        rev_button.Bind(wx.EVT_BUTTON, self.OnClicked)
        ver_button.Bind(wx.EVT_BUTTON, self.OnClicked)
        red_button.Bind(wx.EVT_BUTTON, self.OnClicked)

        pnl.SetSizer(vertbox)

        self.Center()
        self.Show()

    # event handler
    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel()
        display_frame = wx.Frame(self, title=btn, size=wx.Size(400, 200))
        display_panel = wx.Panel(display_frame)
        text = self.enter_text1.GetLineText(0)
        if btn == "CAPITALIZE EACH LETTER":
            text = StrFunc.caps(text)
        elif btn == "words the Reverse":
            text = StrFunc.revWords(text)
        elif btn == "gnirts eht esreveR":
            text = StrFunc.reverse(text)
        static_text = wx.StaticText(display_panel, -1, text)
        if btn == "Make it red":
            static_text.SetForegroundColour((255, 0, 0))

        display_frame.Center()
        display_frame.Show()


app = wx.App()
StringButtons(None, title="StringButtons")
app.MainLoop()

