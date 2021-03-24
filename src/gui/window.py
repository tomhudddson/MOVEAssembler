import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self, title, w, h):
        self.window = None
        self.mainframe = None
        self.srcFile = ""
        self.outputEditor = None

        self._setupWindow(title, w, h)
        self._setupOutputEditor()
        self._setupSourceFileChooser()
        self._setupSettingsWindow()

    def run(self):
        self.window.mainloop()

    def _setupWindow(self, title, w, h):
        self.window = tk.Tk()
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()

        self.window.title(title)
        self.window.geometry(
            "{width}x{height}+{xoffset}+{yoffset}".format(
                width = w, height = h,
                xoffset = int( (screenWidth / 2) - (w / 2) ),
                yoffset = int( (screenHeight / 2) - (h / 2) )            
        ))

        self.mainframe = tk.Frame(self.window)
        self.mainframe.pack(fill = tk.BOTH, expand = tk.TRUE)

    def _setupSettingsWindow(self):
        pass

    def _setupSourceFileChooser(self):
        self.sourceFileChooserFrame = tk.Frame(self.mainframe)
        self.sourceFileChooserFrame.pack(
            side = tk.TOP,
            fill = tk.X,
            anchor = tk.N,
            expand = tk.TRUE
        )
        self.chooserButton = ttk.Button(self.sourceFileChooserFrame, 
            text = "Choose Source File"
        )
        self.chooserButton.grid(column = 0, row = 0)

        self.chooserEntry = ttk.Entry(self.sourceFileChooserFrame, width = 100)
        self.chooserEntry.grid(column = 1, row = 0)

    def _setupOutputEditor(self):
        self.outputEditorFrame = tk.Frame(self.mainframe)
        self.outputEditorFrame.pack(
            side = tk.BOTTOM,
            fill = tk.X,
            anchor = tk.S,
            expand = tk.TRUE
        )
        self.outputEditor = tk.Text(self.outputEditorFrame)
        self.outputEditor.pack(fill = tk.BOTH)
        