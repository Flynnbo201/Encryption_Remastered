import wx
from app.ui_login import MyFrame

if __name__ == "__main__":
    try:
        app = wx.App(False)
        frame = MyFrame()
        app.MainLoop()
    except Exception as e:
        import traceback
        print("An error occurred:")
        traceback.print_exc()
        input("Press Enter to exit...")
