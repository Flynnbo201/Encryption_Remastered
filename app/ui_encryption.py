import wx
from core.crypto import generate_key, encrypt_data, decrypt_data


class EncryptionApp(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="ENCRYPTION WINDOW", size=(500, 400))
        
        notebook = wx.Notebook(self)
        
        # --- Encryption Tab ---

        encryption_panel = wx.Panel(notebook)

        self.text_input = wx.TextCtrl(encryption_panel, pos=(10, 10), size=(470, 50), style=wx.TE_MULTILINE)
        self.encrypt_button = wx.Button(encryption_panel, label="Encrypt", pos=(10, 70))
        self.result_output = wx.TextCtrl(encryption_panel, value="", pos=(10, 110), size=(470, 240), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.encrypt_button.Bind(wx.EVT_BUTTON, self.encrypt_text)

        # --- Decryption Tab
        panel_decrypt = wx.Panel(notebook)
        vbox_dec = wx.BoxSizer(wx.VERTICAL)

        vbox_dec.Add(wx.StaticText(panel_decrypt, label="Enter encryption key:"), flag=wx.LEFT|wx.TOP, border=5)
        self.decrypt_key_input = wx.TextCtrl(panel_decrypt)
        vbox_dec.Add(self.decrypt_key_input, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        vbox_dec.Add(wx.StaticText(panel_decrypt, label="Enter data to decrypt (token):"), flag=wx.LEFT|wx.TOP, border=5)
        self.decrypt_data_input = wx.TextCtrl(panel_decrypt, style=wx.TE_MULTILINE, size=(-1, 80))
        vbox_dec.Add(self.decrypt_data_input, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        self.btn_decrypt = wx.Button(panel_decrypt, label="Decrypt Data")
        self.btn_decrypt.Bind(wx.EVT_BUTTON, self.decrypt_text)
        vbox_dec.Add(self.btn_decrypt, flag=wx.ALIGN_CENTER|wx.ALL, border=10)

        vbox_dec.Add(wx.StaticText(panel_decrypt, label="Decryption Output:"), flag=wx.LEFT, border=5)
        self.decrypt_output = wx.TextCtrl(panel_decrypt, style=wx.TE_MULTILINE|wx.TE_READONLY, size=(-1, 150))
        vbox_dec.Add(self.decrypt_output, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)

        panel_decrypt.SetSizer(vbox_dec)
        notebook.AddPage(encryption_panel, 'Encrypt data')
        notebook.AddPage(panel_decrypt, 'Decrypt data')

        self.Bind(wx.EVT_CLOSE, self.close_app)
        
        self.Show()

    def close_app(self, event):
        from core.ui_manager import appchange
        self.login = appchange.login_change(self)
        print('encryption window closed')


    def encrypt_text(self, event):
        try:
            data = self.text_input.GetValue()
            self.key = generate_key()
            encrypted = encrypt_data(data, self.key)
            self.result_output.SetValue(f"Encrypted:\n{encrypted.decode()}\n\nKey:\n{self.key.decode()}")
        except Exception as e:
            self.result_output.SetValue(f"Error: {str(e)}")

    def decrypt_text(self, event):
        try:
            key = self.decrypt_key_input.GetValue()
            token = self.decrypt_data_input.GetValue()
            decrypted = decrypt_data(token, key)
            self.decrypt_output.SetValue(f"Decrypted:\n{decrypted.decode()}")
        except Exception as e:
            self.decrypt_output.SetValue(f"Error: {str(e)}")
