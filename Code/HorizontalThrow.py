# coding=UTF-8
import tkinter as tk
import configparser as cfg
from math import atan
from tkinter import filedialog as fd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class TabHorizontal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self['padx'] = 10
        self['pady'] = 10
        self.init_ui()

    def init_ui(self):
        self.frame_settings = tk.LabelFrame(self, text='Настройки', height=250, width=250)
        self.frame_settings.grid(row=0, column=0)
        tk.Label(self.frame_settings, text="Точка Y0").grid(row=0,column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Начальная скорость V0").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Время полета").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Точка падения X").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Ускорение g").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Желтая точка на графике - Y0").grid(row=5, column=0, columnspan=2)
        self.ent_y0 = tk.Entry(self.frame_settings)
        self.ent_v0 = tk.Entry(self.frame_settings)
        self.ent_tpol = tk.Entry(self.frame_settings)
        self.ent_x = tk.Entry(self.frame_settings)
        self.ent_g = tk.Entry(self.frame_settings)
        self.ent_y0.grid(row = 0, column = 1)
        self.ent_v0.grid(row=1, column=1)
        self.ent_tpol.grid(row=2, column=1)
        self.ent_x.grid(row=3, column=1)
        self.ent_g.grid(row=4, column=1)
        tk.Button(self.frame_settings, text="Считать из файла", command=self.read_file).grid(row=6, column=0, columnspan=2)
        tk.Button(self.frame_settings, text="Расчитать!", command=self.calc).grid(row=7, column=0)
        tk.Button(self.frame_settings, text="Очистить поля", command=self.clear_entry).grid(row=7, column=1)

        self.frame_result = tk.LabelFrame(self, text='Расчет', height=250, width=250)
        self.frame_result.grid(row=1, column=0)
        tk.Label(self.frame_result, text="Точка Y0").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Начальная скорость V0").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Ускорение g").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Время полета").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Координата падения X").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Конечная скорость по X").grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Конечная скорость по Y").grid(row=6, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Конечная скорость").grid(row=7, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Угол beta").grid(row=8, column=0, sticky=tk.W)
        self.lbl_y0 = tk.Label(self.frame_result, text="-")
        self.lbl_v0 = tk.Label(self.frame_result, text="-")
        self.lbl_g = tk.Label(self.frame_result, text="-")
        self.lbl_tpol = tk.Label(self.frame_result, text="-")
        self.lbl_x = tk.Label(self.frame_result, text="-")
        self.lbl_vx = tk.Label(self.frame_result, text="-")
        self.lbl_vy = tk.Label(self.frame_result, text="-")
        self.lbl_vKon = tk.Label(self.frame_result, text="-")
        self.lbl_beta = tk.Label(self.frame_result, text="-")
        self.lbl_y0.grid(row=0, column=1)
        self.lbl_v0.grid(row=1, column=1)
        self.lbl_g.grid(row=2, column=1)
        self.lbl_tpol.grid(row=3, column=1)
        self.lbl_x.grid(row=4, column=1)
        self.lbl_vx.grid(row=5, column=1)
        self.lbl_vy.grid(row=6, column=1)
        self.lbl_vKon.grid(row=7, column=1)
        self.lbl_beta.grid(row=8, column=1)
        tk.Button(self.frame_result, text="Сохранить результаты", command=self.save_file).grid(row=9, column=0, columnspan=2)

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
        self.ent_y0.delete(0, tk.END)
        self.ent_g.delete(0, tk.END)

    def read_file(self):
        file_name = fd.askopenfilename(filetypes=[("Txt files", ".txt")])
        config = cfg.ConfigParser()
        config.read(file_name)
        if 'HORIZONTAL' not in config:
            messagebox.showerror("ОШИБКА ВВОДА", "Блок HORIZONTAL отсутствует в файле")
            return
        self.clear_entry()
        df = config['HORIZONTAL']
        if 'v0' in df:
            self.ent_v0.insert(0, df['v0'])
        if 'y0' in df:
            self.ent_y0.insert(0, df['y0'])
        if 'tpol' in df:
            self.ent_tpol.insert(0, df['tpol'])
        if 'x' in df:
            self.ent_x.insert(0, df['x'])
        if 'g' in df:
            self.ent_g.insert(0, df['g'])
        print(file_name)

    def save_file(self):
        file_name = fd.asksaveasfilename(filetypes=[("Txt files", "*.txt")])
        config = cfg.ConfigParser()
        print(file_name)
        config['HORIZONTAL.RESULT'] = {
            'y0': self.lbl_y0['text'],
            'v0': self.lbl_v0['text'],
            'g': self.lbl_g['text'],
            'L': self.lbl_x['text'],
            'tpol': self.lbl_tpol['text'],
            'vx': self.lbl_vx ['text'],
            'vy': self.lbl_vy['text'],
            'vkon': self.lbl_vKon['text'],
            'beta': self.lbl_beta['text'],
        }
        with open(file_name + ".txt", 'w') as configfile:
            config.write(configfile)

    def calc(self):
        defined = set()

        str_y0 = str(self.ent_y0.get())
        if str_y0 != "":
            try:
                y0 = float(str_y0)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле y0")
                return
            if y0 <= 0:
                messagebox.showerror("ОШИБКА ВВОДА", "x0 должно быть больше 0")
                return
            defined.add('y0')

        str_v0 = str(self.ent_v0.get())
        if str_v0 != "":
            try:
                v0 = abs(float(str_v0))
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
                return
            defined.add('v0')

        str_tpol = str(self.ent_tpol.get())
        if str_tpol != "":
            try:
                tpol = abs(float(str_tpol))
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
                return
            defined.add('tpol')

        str_x = str(self.ent_x.get())
        if str_x != "":
            try:
                x = float(str_x)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
                return
            defined.add('x')

        str_g = str(self.ent_g.get())
        try:
            g = abs(float(str_g))
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле g")
            return

        if len(defined) < 2:
            messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для вычислений")
            return

        if 'y0' in defined and 'v0' in defined:
            tpol = ((2 * y0) / g)**0.5
            x = tpol * v0
        elif 'y0' in defined and 'x' in defined:
            tpol = ((2 * y0) / g)**0.5
            v0 = x / tpol
        elif 'v0' in defined and 'tpol' in defined:
            x = v0 * tpol
            y0 = (g * (tpol**2)) / 2
        elif 'v0' in defined and 'x' in defined:
            tpol = x / v0
            y0 = (g * (tpol**2)) / 2
        elif 'tpol' in defined and 'x' in defined:
            v0 = x / tpol
            y0 = (g * (tpol**2)) / 2
        elif 'y0' in defined and 'tpol' in defined:
            messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для вычислений")
            return


        vKon_x = v0
        vKon_y = tpol * g
        vKon = ((vKon_x**2) + (vKon_y**2))**0.5
        beta = atan(vKon_y / vKon_x)
        self.lbl_y0['text'] = str(y0)
        self.lbl_v0['text'] = str(v0)
        self.lbl_g['text'] = str(g)
        self.lbl_tpol['text'] = str(tpol)
        self.lbl_x['text'] = str(x)
        self.lbl_vx['text'] = str(vKon_x)
        self.lbl_vy['text'] = str(vKon_y)
        self.lbl_vKon['text'] = str(vKon)
        self.lbl_beta['text'] = str(beta)
        delta_x = x / 100
        ls_x = []
        for i in range(0, 99):
            ls_x.append(i * delta_x)
        ls_x.append(x)
        ls_y = []
        for i in range(0, 99):
            ls_y.append(y0 - (g * (ls_x[i]**2)) / (2 * (v0**2)))
        ls_y.append(0)
        self.plot.clear()
        self.plot.plot(ls_x, ls_y)
        self.plot.scatter(0, y0, color='orange', s=40, marker='o')
        self.canvas.draw()
