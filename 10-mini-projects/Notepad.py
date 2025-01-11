import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class SimpleNotePad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Bob\'s Notepad')

        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

    def run(self) -> None:
        self.root.mainloop()

def main():
    root: Tk = tk.Tk()
    app: SimpleNotePad = SimpleNotePad(root=root)
    app.run()

if __name__ == '__main__':
    main()