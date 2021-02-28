# coding=UTF-8
import tkinter as tk
import webbrowser
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
        tk.Label(self.frame_settings, text="Точка X0").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Начальная скорость V0").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Время подъема").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Время полета").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Максимальная высота подъема").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Ускорение g").grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.frame_settings, text="Желтая точка на графике - x0").grid(row=6, column=0, columnspan=2)
        self.ent_x0 = tk.Entry(self.frame_settings)
        self.ent_v0 = tk.Entry(self.frame_settings)
        self.ent_tpod = tk.Entry(self.frame_settings)
        self.ent_tpol = tk.Entry(self.frame_settings)
        self.ent_hmax = tk.Entry(self.frame_settings)
        self.ent_g = tk.Entry(self.frame_settings)
        self.ent_x0.grid(row=0, column=1)
        self.ent_v0.grid(row=1, column=1)
        self.ent_tpod.grid(row=2, column=1)
        self.ent_tpol.grid(row=3, column=1)
        self.ent_hmax.grid(row=4, column=1)
        self.ent_g.grid(row=5, column=1)
        tk.Button(self.frame_settings, text="Считать из файла", command=self.read_file).grid(row=7, column=0,
                                                                                             columnspan=2)
        tk.Button(self.frame_settings, text="Расчитать!", command=self.calc).grid(row=8, column=0)
        tk.Button(self.frame_settings, text="Очистить поля", command=self.clear_entry).grid(row=8, column=1)

        self.frame_result = tk.LabelFrame(self, text='Расчет', height=250, width=250)
        self.frame_result.grid(row=1, column=0)
        tk.Label(self.frame_result, text="Точка X0").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Начальная скорость V0").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Ускорение g").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Время подъема").grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Время полета").grid(row=4, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Максимальная высота подъема").grid(row=5, column=0, sticky=tk.W)
        tk.Label(self.frame_result, text="Конечная скорость").grid(row=6, column=0, sticky=tk.W)
        self.lbl_x0 = tk.Label(self.frame_result, text="-")
        self.lbl_v0 = tk.Label(self.frame_result, text="-")
        self.lbl_g = tk.Label(self.frame_result, text="-")
        self.lbl_tpod = tk.Label(self.frame_result, text="-")
        self.lbl_tpol = tk.Label(self.frame_result, text="-")
        self.lbl_hmax = tk.Label(self.frame_result, text="-")
        self.lbl_vk = tk.Label(self.frame_result, text="-")
        self.lbl_x0.grid(row=0, column=1)
        self.lbl_v0.grid(row=1, column=1)
        self.lbl_g.grid(row=2, column=1)
        self.lbl_tpod.grid(row=3, column=1)
        self.lbl_tpol.grid(row=4, column=1)
        self.lbl_hmax.grid(row=5, column=1)
        self.lbl_vk.grid(row=6, column=1)
        tk.Button(self.frame_result, text="Сохранить результаты", command=self.save_file).grid(row=7, column=0,
                                                                                               columnspan=2)
        tk.Button(self.frame_result, text="Открыть документ-справку", command=self.save_file).grid(row=8, column=0,
                                                                                                   columnspan=2)
        tk.Button(self.frame_result, text="Открыть интернет-справку", command=self.open_web).grid(row=9, column=0,
                                                                                                  columnspan=2)

        self.frame_canvas = tk.LabelFrame(self, text='График')
        self.frame_canvas.grid(row=0, column=1, rowspan=2)
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.plot = self.figure.add_subplot(111)
        # self.plot.plot([0,2,3,4], [0, 'b', 7, 8])
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame_canvas)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.pack()

    def open_web(self):
        webbrowser.open_new("https://lampa.io/p/%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%B5%D0%BB"
                            "%D0%B0,-%D0%B1%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%B2%D0%B5%D1%80"
                            "%D1%82%D0%B8%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B2%D0%B2%D0%B5%D1%80%D1%85-("
                            "%D0%B2%D0%BD%D0%B8%D0%B7)-00000000aec967390a34cd4976d5458f")

    def clear_entry(self):
        self.ent_v0.delete(0, tk.END)
        self.ent_x0.delete(0, tk.END)
        self.ent_g.delete(0, tk.END)

    def save_file(self):
        file_name = fd.asksaveasfilename(filetypes=[("Txt files", "*.txt")])
        config = cfg.ConfigParser()
        print(file_name)
        config['VERTICAL'] = {
            'x0': self.lbl_x0['text'],
            'v0': self.lbl_v0['text'],
            'g': self.lbl_g['text'],
            'tpod': self.lbl_tpod['text'],
            'hmax': self.lbl_hmax['text'],
            'tpol': self.lbl_tpol['text'],
            'vk': self.lbl_vk['text']
        }
        with open(file_name + ".txt", 'w') as configfile:
            config.write(configfile)

    def read_file(self):
        file_name = fd.askopenfilename(filetypes=[("Txt files", ".txt")])
        config = cfg.ConfigParser()
        config.read(file_name)
        if 'VERTICAL' not in config:
            messagebox.showerror("ОШИБКА ВВОДА", "Блок VERTICAL отсутствует в файле")
            return
        self.clear_entry()
        df = config['VERTICAL']
        if 'v0' in df:
            self.ent_v0.insert(0, df['v0'])
        if 'x0' in df:
            self.ent_x0.insert(0, df['x0'])
        if 'g' in df:
            self.ent_g.insert(0, df['g'])
        if 'tpol' in df:
            self.ent_tpol.insert(0, df['tpol'])
        if 'tpod' in df:
            self.ent_tpod.insert(0, df['tpod'])
        if 'hmax' in df:
            self.ent_hmax.insert(0, df['hmax'])
        print(file_name)

    def calc(self):
        defined = set()

        str_x0 = str(self.ent_x0.get())
        if str_x0 != "":
            try:
                x0 = float(str_x0)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле x0")
                return
            if x0 < 0:
                messagebox.showerror("ОШИБКА ВВОДА", "x0 должно быть больше 0")
                return
            defined.add('x0')

        str_v0 = str(self.ent_v0.get())
        if str_v0 != "":
            try:
                v0 = float(str_v0)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле v0")
                return
            defined.add('v0')

        str_tpod = str(self.ent_tpod.get())
        if str_tpod != "":
            try:
                tpod = float(str_tpod)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле tpod")
                return
            if tpod < 0:
                messagebox.showerror("ОШИБКА ВВОДА", "Время подъема не может быть отрицательным")
                return
            defined.add('tpod')

        str_tpol = str(self.ent_tpol.get())
        if str_tpol != "":
            try:
                tpol = float(str_tpol)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле tpol")
                return
            if tpol <= 0:
                messagebox.showerror("ОШИБКА ВВОДА", "Время полета может быть только больше нуля")
                return
            defined.add('tpol')

        str_hmax = str(self.ent_hmax.get())
        if str_hmax != "":
            try:
                hmax = float(str_hmax)
            except ValueError:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле hmax")
                return
            if hmax < 0:
                messagebox.showerror("ОШИБКА ВВОДА", "Максимальная высота не может быть отрицательной")
                return
            defined.add('hmax')

        str_g = str(self.ent_g.get())
        try:
            g = abs(float(str_g))
            if g == 0:
                messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле g")
                return
        except ValueError:
            messagebox.showerror("ОШИБКА ВВОДА", "Пожалуйста, введите число в поле g")
            return

        if len(defined) < 2:
            messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
            return

        if 'x0' in defined and 'v0' in defined:
            if v0 <= 0:
                hmax = x0
                tpod = 0
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
            else:
                hmax = x0 + (v0 ** 2) / (2 * g)
                tpod = v0 / g
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
        elif 'x0' in defined and 'tpod' in defined:
            if tpod > 0:
                v0 = g * tpod
                hmax = x0 + v0 * tpod - (g * (tpod ** 2)) / 2
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
            else:
                if 'tpol' in defined:
                    hmax = x0
                    v0 = ((g * tpol * tpol) / 2 - x0) / tpol
                else:
                    messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                    return
        elif 'x0' in defined and 'tpol' in defined:
            v0 = ((g * tpol) / 2) - (x0 / tpol)
            if v0 <= 0:
                tpod = 0
                hmax = x0
            else:
                tpod = v0 / g
                hmax = x0 + v0 * tpod - (g * (tpod ** 2)) / 2
        elif 'v0' in defined and 'tpol' in defined:
            x0 = (g * (tpol ** 2)) / 2 - v0 * tpol
            if v0 <= 0:
                tpod = 0
                hmax = x0
            else:
                tpod = v0 / g
                hmax = x0 + v0 * tpod - (g * (tpod ** 2)) / 2
        elif 'v0' in defined and 'hmax' in defined:
            if v0 <= 0:
                x0 = hmax
                tpod = 0
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
            else:
                tpod = v0 / g
                x0 = hmax + (g * (tpod ** 2)) / 2 - v0 * tpod
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
        elif 'tpod' in defined and 'hmax' in defined:
            if tpod > 0:
                v0 = g * tpod
                x0 = hmax + (g * (tpod ** 2)) / 2 - v0 * tpod
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
            else:
                messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                return
        elif 'v0' in defined and 'tpod' in defined:
            if v0 == 0 and tpod == 0:
                if 'tpol' in defined:
                    x0 = (g * tpol * tpol) / 2
                    hmax = x0
                else:
                    messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                    return
            elif v0 < 0 and tpod == 0:
                if 'tpol' in defined:
                    x0 = (g * tpol * tpol) / 2 - v0 * tpol
                    hmax = x0
                else:
                    messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                    return
            elif v0 > 0 and tpod > 0:
                if 'tpol' in defined:
                    x0 = (g * tpol * tpol) / 2 - v0 * tpol
                    hmax = x0 + v0 * tpod - (g * (tpod ** 2)) / 2
                elif 'hmax' in defined:
                    x0 = hmax - v0 * tpod + (g * tpod * tpod) / 2
                    tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
                else:
                    messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                    return
            else:
                messagebox.showerror("ОШИБКА РАСЧЕТА", "Ошибка в указании v0 и tpod")
                return
        elif 'x0' in defined and 'hmax' in defined:
            if hmax > x0:
                tpod = ((2 * (hmax - x0)) / g) ** 0.5
                v0 = g * tpod
                tpol = (v0 + (v0 ** 2 + 2 * x0 * g) ** 0.5) / g
            else:
                messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
                return
        elif 'tpol' in defined and 'tpod' in defined:
            messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
            return
        elif 'tpol' in defined and 'hmax' in defined:
            messagebox.showerror("ОШИБКА РАСЧЕТА", "Недостаточно данных для расчета")
            return

        self.lbl_x0['text'] = str(x0)
        self.lbl_v0['text'] = str(v0)
        self.lbl_g['text'] = str(g)
        self.lbl_tpol['text'] = str(tpol)
        self.lbl_hmax['text'] = str(hmax)
        self.lbl_tpod['text'] = str(tpod)
        self.lbl_vk['text'] = str(v0 - g * tpol)
        self.plot.clear()
        self.plot.plot([0, 0], [0, hmax])
        self.plot.scatter(0, x0, color='orange', s=40, marker='o')
        self.canvas.draw()
