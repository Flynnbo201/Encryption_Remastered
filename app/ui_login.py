import wx
import time
from threading import Thread
from core.accounts import load_accounts, verify_password



class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='LOG IN WINDOW')
        panel = wx.Panel(self)

        self.accounts = load_accounts()

        self.text1 = wx.StaticText(panel, label='username:', size=(55, 20), style=1)
        self.input1 = wx.TextCtrl(panel, size=(150, 20), style=1)

        self.text2 = wx.StaticText(panel, label='password:', size=(55, 20), style=1)
        self.input2 = wx.TextCtrl(panel, size=(150, 20), style=wx.TE_PASSWORD)

        self.enter = wx.Button(parent=panel, label='ENTER', pos=(0, 50), size=(215, 20))
        self.enter.Bind(wx.EVT_BUTTON, self.on_button)

        self.status = wx.StaticText(panel, label='', pos=(0, 125), size=(215, 20), style=1)

        self.success = False

        sizer = wx.FlexGridSizer(3, 2, 5, 10)
        sizer.Add(self.text1)
        sizer.Add(self.input1)
        sizer.Add(self.text2)
        sizer.Add(self.input2)
        panel.SetSizer(sizer)

        self.Show()

        Thread(target=self.background_checker, daemon=True).start()
        self.Bind(wx.EVT_CLOSE, self.close_app)

        self.admin_account = {'admin': 'admin123'}

    def background_checker(self):
        while True:
            time.sleep(1)
            if self.success:
                wx.CallAfter(self.Close)
                break

    def close_app(self, event):
        from core.ui_manager import appchange
        username = self.input1.GetValue()
        password = self.input2.GetValue()
        if self.success and username in self.admin_account and self.admin_account[username] == password:
            self.admin = appchange.admin_change(self)
        elif self.success:
            self.user = appchange.encryption_change(self)
        else:
            wx.GetApp().ExitMainLoop()
        event.Skip()

    def on_button(self, event):
        username = self.input1.GetLineText(0)
        password = self.input2.GetLineText(0)
        if username in self.accounts:
            yes = verify_password(self.accounts[username], password)
        else:
            yes = False

        if yes:
            self.status.SetLabel('success')
            self.success = True
        elif username in self.admin_account and self.admin_account[username] == password:
            self.status.SetLabel('success')
            self.success = True
        else:
            self.status.SetLabel('invalid username or password')
            self.success = False