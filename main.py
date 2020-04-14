from tkinter import Tk
from gui import JapEngFrame

if __name__ == '__main__':
    root = Tk()
    root.attributes('-fullscreen', True)
    app  = JapEngFrame(root)
    root.mainloop()
