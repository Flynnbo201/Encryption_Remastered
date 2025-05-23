import wx
from app.ui_admin import MyFrame3
from app.ui_encryption import EncryptionApp
from app.ui_login import MyFrame
class appchange():
    def __init__(self):
        print('init')
    def startup(self):
        try:
            self.app = wx.App(False)
            self.frame = MyFrame()
            self.app.MainLoop()
        except Exception as e:
            import traceback
            print("An error occurred:")
            traceback.print_exc()
            input("Press Enter to exit...")
    def admin_change(self):
        self.app_adm = MyFrame3()
    def login_change(self):
        self.app_log = MyFrame()
    def encryption_change(self):
        self.app_enc = EncryptionApp()


        
