# coding=UTF-8
from tkinter import Tk, ttk
import tkinter as tk

from AngleThrow import TabAngle
from VerticalThrow import TabVertical
from HorizontalThrow import TabHorizontal


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('ThrowCalc')

        self.init_ui()

    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1000, height=700)

        tab_angle = TabAngle(self.notebook)
        tab_vertical = TabVertical(self.notebook)
        tab_horizontal = TabHorizontal(self.notebook)

        self.notebook.add(tab_angle, text="Под углом к горизонту")
        self.notebook.add(tab_vertical, text="Вертикально вверх")
        self.notebook.add(tab_horizontal, text="Горизонтально")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('version')
    ex = MainWindow(root)
    root.geometry("830x600")
    root.resizable(width=False, height=False)
    root.mainloop()
