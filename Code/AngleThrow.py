# coding=UTF-8
import tkinter as tk
import configparser as cfg
from tkinter import filedialog as fd
from math import sin, cos, tan, radians
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class TabAngle(tk.Frame):
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
        tk.Label(self.frame_settings, text="Угол alpha").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Ускорение g").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Желтая точка на графике - Y0").grid(row=4, column=0, columnspan=2)
        self.ent_y0 = tk.Entry(self.frame_settings)
        self.ent_v0 = tk.Entry(self.frame_settings)
        self.ent_alpha = tk.Entry(self.frame_settings)
        self.ent_g = tk.Entry(self.frame_settings)
        self.ent_y0.grid(row = 0, column = 1)
        self.ent_v0.grid(row=1, column=1)
        self.ent_alpha.grid(row=2, column=1)
        self.ent_g.grid(row=3, column=1)
        tk.Button(self.frame_settings, text="Считать из файла", command=self.read_file).grid(row=5, column=0, columnspan=2)
        tk.Button(self.frame_settings, text="Расчитать!", command=self.calc).grid(row=6, column=0)
        tk.Button(self.frame_settings, text="Очистить поля", command=self.clear_entry).grid(row=6, column=1)

        self.frame_result = tk.LabelFrame(self, text='Расчет', height=250, width=250)
        self.frame_result.grid(row=1, column=0)
        tk.Label(self.frame_result, text="Точка Y0").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Начальная скорость V0").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Угол alpha").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Ускорение g").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Время подъема").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Максимальная высота подъема").grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Время полета").grid(row=6, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Координата падения X").grid(row=7, column=0, sticky=tk.W)
        self.lbl_y0 = tk.Label(self.frame_result, text="   -   ")
        self.lbl_v0 = tk.Label(self.frame_result, text="   -   ")
        self.lbl_alpha = tk.Label(self.frame_result, text="   -   ")
        self.lbl_g = tk.Label(self.frame_result, text="   -   ")
        self.lbl_tpod = tk.Label(self.frame_result, text="   -   ")
        self.lbl_hmax = tk.Label(self.frame_result, text="   -   ")
        self.lbl_tpol = tk.Label(self.frame_result, text="   -   ")
        self.lbl_x = tk.Label(self.frame_result, text="   -   ")
        self.lbl_y0.grid(row=0, column=1)
        self.lbl_v0.grid(row=1, column=1)
        self.lbl_alpha.grid(row=2, column=1)
        self.lbl_g.grid(row=3, column=1)
        self.lbl_tpod.grid(row=4, column=1)
        self.lbl_hmax.grid(row=5, column=1)
        self.lbl_tpol.grid(row=6, column=1)
        self.lbl_x.grid(row=7, column=1)
        tk.Button(self.frame_result, text="Сохранить результаты", command=self.save_file).grid(row=8, column=0, columnspan=2)

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
        self.ent_alpha.delete(0, tk.END)
        self.ent_g.delete(0, tk.END)

    def read_file(self):
        file_name = fd.askopenfilename(filetypes=[("Txt files", ".txt")])
        config = cfg.ConfigParser()
        config.read(file_name)
        if 'ANGLE' not in config:
            messagebox.showerror("ОШИБКА ВВОДА", "Блок ANGLE отсутствует в файле")
            return
        self.clear_entry()
        df = config['ANGLE']
        if 'v0' in df:
            self.ent_v0.insert(0, df['v0'])
        if 'y0' in df:
            self.ent_y0.insert(0, df['y0'])
        if 'alpha' in df:
            self.ent_alpha.insert(0, df['alpha'])
        if 'g' in df:
            self.ent_g.insert(0, df['g'])
        print(file_name)

    def save_file(self):
        file_name = fd.asksaveasfilename(filetypes=[("Txt files", "*.txt")])
        config = cfg.ConfigParser()
        print(file_name)
        config['ANGLE.RESULT'] = {
            'y0': self.lbl_y0['text'],
            'v0': self.lbl_v0['text'],
            'alpha': self.lbl_alpha['text'],
            'g': self.lbl_g['text'],
            'tpod': self.lbl_tpod['text'],
            'hmax': self.lbl_hmax['text'],
            'tpol': self.lbl_tpol['text'],
            'L': self.lbl_x['text']
        }
        with open(file_name + ".txt", 'w') as configfile:
            config.write(configfile)

    def calc(self):
        str_y0 = str(self.ent_y0.get())
        try:
            y0 = float(str_y0)
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле y0")
            return
        if y0 < 0:
            messagebox.showerror("ОШИБКА ВВОДА", "x0 должно быть больше 0")
            return
        str_v0 = str(self.ent_v0.get())
        try:
            v0 = abs(float(str_v0))
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
            return
        if v0 == 0:
            messagebox.showerror("ОШИБКА ВВОДА", "v0 не может быть равен нулю")
            return
        str_alpha = str(self.ent_alpha.get())
        try:
            alpha = radians(abs(float(str_alpha)))
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле alpha")
            return
        if alpha < 0:
            messagebox.showerror("ОШИБКА ВВОДА", "alpha не может быть меньше нуля")
            return
        str_g = str(self.ent_g.get())
        try:
            g = float(str_g)
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле g")
            return
        tpod = (v0 * sin(alpha)) / g
        hmax = y0 + ((v0 ** 2) * (sin(alpha)**2)) / (2 * g)
        tpol = (v0 * sin(alpha) + (((v0 * sin(alpha))**2) + 2 * y0 * g)**0.5) / g
        x = v0 * cos(alpha) * tpol
        self.lbl_y0['text'] = str(y0)
        self.lbl_v0['text'] = str(v0)
        self.lbl_alpha['text'] = str(alpha)
        self.lbl_g['text'] = str(g)
        self.lbl_tpod['text'] = str(tpod)
        self.lbl_hmax['text'] = str(hmax)
        self.lbl_tpol['text'] = str(tpol)
        self.lbl_x['text'] = str(x)
        delta_x = x / 100
        print(delta_x * 100)
        ls_x = []
        for i in range(0, 99):
            ls_x.append(i * delta_x)
        ls_x.append(x)
        ls_y = []
        for i in range(0, 99):
            ls_y.append(y0 + ls_x[i] * tan(alpha) - (g * (ls_x[i] ** 2)) / (2 * v0 * v0 * (cos(alpha) ** 2)))
        ls_y.append(0)
        self.plot.clear()
        self.plot.plot(ls_x, ls_y)
        self.plot.scatter(0, y0, color='orange', s=40, marker='o')
        self.canvas.draw()