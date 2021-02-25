# coding=UTF-8
import tkinter as tk
import configparser as cfg
from tkinter import filedialog as fd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class TabVertical(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self['padx'] = 10
        self['pady'] = 10
        self.init_ui()

    def init_ui(self):
        self.frame_settings = tk.LabelFrame(self, text='Настройки', height=250, width=250)
        self.frame_settings.grid(row=0, column=0)
        tk.Label(self.frame_settings, text="Точка X0").grid(row=0,column=0)
        tk.Label(self.frame_settings, text="Начальная скорость V0").grid(row=1, column=0)
        tk.Label(self.frame_settings, text="Ускорение g").grid(row=2, column=0)
        tk.Label(self.frame_settings, text="Желтая точка на графике - x0").grid(row=3, column=0, columnspan=2)
        self.ent_x0 = tk.Entry(self.frame_settings)
        self.ent_v0 = tk.Entry(self.frame_settings)
        self.ent_g = tk.Entry(self.frame_settings)
        self.ent_x0.grid(row = 0, column = 1)
        self.ent_v0.grid(row=1, column=1)
        self.ent_g.grid(row=2, column=1)
        tk.Button(self.frame_settings, text="Считать из файла", command=self.read_file).grid(row=5, column=0, columnspan=2)
        tk.Button(self.frame_settings, text="Расчитать!", command=self.calc).grid(row=6, column=0)
        tk.Button(self.frame_settings, text="Очистить поля", command=self.clear_entry).grid(row=6, column=1)

        self.frame_result = tk.LabelFrame(self, text='Расчет', height=250, width=250)
        self.frame_result.grid(row=1, column=0)
        tk.Label(self.frame_result, text="Точка X0").grid(row=0, column=0)
        tk.Label(self.frame_result, text="Начальная скорость V0").grid(row=1, column=0)
        tk.Label(self.frame_result, text="Ускорение g").grid(row=2, column=0)
        tk.Label(self.frame_result, text="Время подъема").grid(row=3, column=0)
        tk.Label(self.frame_result, text="Время полета").grid(row=4, column=0)
        tk.Label(self.frame_result, text="Максимальная высота").grid(row=5, column=0)
        self.lbl_x0 = tk.Label(self.frame_result, text="-")
        self.lbl_v0 = tk.Label(self.frame_result, text="-")
        self.lbl_g = tk.Label(self.frame_result, text="-")
        self.lbl_tpod = tk.Label(self.frame_result, text="-")
        self.lbl_tpol = tk.Label(self.frame_result, text="-")
        self.lbl_hmax = tk.Label(self.frame_result, text="-")
        self.lbl_x0.grid(row=0, column=1)
        self.lbl_v0.grid(row=1, column=1)
        self.lbl_g.grid(row=2, column=1)
        self.lbl_tpod.grid(row=3, column=1)
        self.lbl_tpol.grid(row=4, column=1)
        self.lbl_hmax.grid(row=5, column=1)
        tk.Button(self.frame_result, text="Сохранить результаты", command=self.save_file).grid(row=6, column=0, columnspan=2)

        self.frame_canvas = tk.LabelFrame(self, text='График')
        self.frame_canvas.grid(row=0, column=1, rowspan=2)
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.plot = self.figure.add_subplot(111)
        #self.plot.plot([0,2,3,4], [0, 'b', 7, 8])
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame_canvas)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)



        self.pack()

    def clear_entry(self):
        self.ent_v0.delete(0, tk.END)
        self.ent_x0.delete(0, tk.END)
        self.ent_g.delete(0, tk.END)

    def save_file(self):
        file_name = fd.asksaveasfilename(filetypes=[("Ini files", "*.ini")])
        config = cfg.ConfigParser()
        print(file_name)
        config['VERTICAL.RESULT'] = {
            'x0': self.lbl_x0['text'],
            'speed': self.lbl_v0['text'],
            'g': self.lbl_g['text'],
            'tpod': self.lbl_tpod['text'],
            'hmax': self.lbl_hmax['text'],
            'tpol': self.lbl_tpol['text'],
        }
        with open(file_name + ".ini", 'w') as configfile:
            config.write(configfile)

    def read_file(self):
        file_name = fd.askopenfilename(filetypes=[("Ini files", ".ini")])
        config = cfg.ConfigParser()
        config.read(file_name)
        if 'VERTICAL' not in config:
            messagebox.showerror("ОШИБКА ВВОДА", "Блок VERTICAL отсутствует в файле")
            return
        self.clear_entry()
        df = config['VERTICAL']
        if 'speed' in df:
            print(df['speed'])
            self.ent_v0.insert(0, df['speed'])
        if 'x0' in df:
            self.ent_x0.insert(0, df['x0'])
        if 'g' in df:
            self.ent_g.insert(0, df['g'])
        print(file_name)


    def calc(self):
        str_x0 = str(self.ent_x0.get())
        try:
            x0 = float(str_x0)
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле x0")
            return
        str_v0 = str(self.ent_v0.get())
        try:
            v0 = float(str_v0)
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
            return
        str_g = str(self.ent_g.get())
        try:
            g = float(str_g)
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле g")
            return
        if v0 <= 0:
            hmax = x0
            self.lbl_tpod['text'] = str(0)
        else:
            hmax = x0 + (v0 ** 2) / (2 * g)
            self.lbl_tpod['text'] = str(v0 / g)
        self.lbl_x0['text'] = str(x0)
        self.lbl_v0['text'] = str(v0)
        self.lbl_g['text'] = str(g)
        self.lbl_tpol['text'] = str((v0 + (v0 ** 2 + 2 * x0 * g)**0.5) / g)
        self.lbl_hmax['text'] = str(hmax)
        self.plot.clear()
        self.plot.plot([0, 0], [0, hmax])
        self.plot.scatter(0, x0, color='orange', s=40, marker='o')
        self.canvas.draw()