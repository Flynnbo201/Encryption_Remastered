import wx
from core.accounts import load_accounts, save_accounts, hash_password, load_accounts_local

class MyFrame3(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="ADMIN PANEL", size=(400, 400))
        panel = wx.Panel(self)

        self.accounts = load_accounts()

        self.user_label = wx.StaticText(panel, label="Username:", pos=(10, 10))
        self.user_input = wx.TextCtrl(panel, pos=(100, 10), size=(150, -1))

        self.pass_label = wx.StaticText(panel, label="Password:", pos=(10, 40))
        self.pass_input = wx.TextCtrl(panel, pos=(100, 40), size=(150, -1))

        self.add_button = wx.Button(panel, label="Add Account", pos=(10, 80))
        self.remove_button = wx.Button(panel, label="Remove Account", pos=(150, 80))
        self.status_label = wx.StaticText(panel, label="", pos=(10, 120), size=(360, 25))

        self.add_button.Bind(wx.EVT_BUTTON, self.add_account)
        self.remove_button.Bind(wx.EVT_BUTTON, self.remove_account)

        self.Bind(wx.EVT_CLOSE, self.close_app)

        self.Show()

    def close_app(self, event):
        import time
        from core.ui_manager import appchange
        self.login = appchange.login_change(self)
        print('admin window closed')

        

    def load(self, event, web_or_local):
        from core.accounts import load_accounts, load_accounts_local

        if web_or_local:
            loaded_local = str(load_accounts)
        else:
            loaded_local = str(load_accounts_local())
        print(loaded_local)
        self.loadotp.SetValue(loaded_local)
    
    def add_account(self, event):
        username = self.user_input.GetValue()
        password = self.pass_input.GetValue()
        if username and password:
            if username not in self.accounts:
                self.accounts[username] = hash_password(password)
                save_accounts(self.accounts)
                self.status_label.SetLabel("Account added.")
            else:
                self.status_label.SetLabel("Account already exists.")
        else:
            self.status_label.SetLabel("Please enter username and password.")

    def remove_account(self, event):
        username = self.user_input.GetValue()
        if username:
            if username in self.accounts:
                del self.accounts[username]
                save_accounts(self.accounts)
                self.status_label.SetLabel("Account removed.")
            else:
                self.status_label.SetLabel("Account not found.")
        else:
            self.status_label.SetLabel("Please enter username.")