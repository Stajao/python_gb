"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""

import tkinter as tk
from time import sleep
from tkinter import Frame


class TrafficLight(tk.Frame):
    def __init__(self, parent, *args, default_color='grey'):
        tk.Frame.__init__(self)
        self.parent = parent
        self.lights = (args[0], args[1], args[2], default_color)
        self.upper_light, self.middle_light, self.lower_light = self.lights[3], self.lights[3], self.lights[3]
        self.parent.title('Traffic Light v.3.98')
        self.frame = tk.Frame(self.parent, bg='black')
        self.traffic_upper = tk.Frame(self.frame, width=200, height=200, bg=self.upper_light,
                                      highlightbackground="black",
                                      highlightthickness=2)
        self.traffic_middle: Frame = tk.Frame(self.frame, width=200, height=200, bg=self.middle_light,
                                              highlightbackground="black",
                                              highlightthickness=2)
        self.traffic_lower = tk.Frame(self.frame, width=200, height=200, bg=self.lower_light,
                                      highlightbackground="black",
                                      highlightthickness=2)
        self.but = tk.Button(self.frame, text='Старт!', command=self.__running)
        self.but2 = tk.Button(self.frame, text='Сломать!', command=self.__out_of_order)
        self.frame.pack(ipadx=10, ipady=10)
        self.traffic_upper.pack(padx=10, pady=10)
        self.traffic_middle.pack(padx=10, pady=10)
        self.traffic_lower.pack(padx=10, pady=10)
        self.but.pack(padx=10, pady=10)
        self.but2.pack()

    def __running(self):
        self.traffic_upper.config(bg=self.lights[0])
        self.traffic_middle.config(bg=self.lights[3])
        self.traffic_lower.config(bg=self.lights[3])
        self.frame.update()
        sleep(7)
        self.traffic_upper.config(bg=self.lights[3])
        self.traffic_middle.config(bg=self.lights[1])
        self.traffic_lower.config(bg=self.lights[3])
        self.frame.update()
        sleep(2)
        self.traffic_upper.config(bg=self.lights[3])
        self.traffic_middle.config(bg=self.lights[3])
        self.traffic_lower.config(bg=self.lights[2])
        self.frame.update()
        sleep(5)
        self.traffic_upper.config(bg=self.lights[3])
        self.traffic_middle.config(bg=self.lights[3])
        self.traffic_lower.config(bg=self.lights[3])
        self.frame.update()
        # self.frame.after(50, self.__running)

    def __out_of_order(self):
        self.traffic_upper.config(bg=self.lights[3])
        self.traffic_middle.config(bg=self.lights[3])
        self.traffic_lower.config(bg=self.lights[3])
        self.frame.update()
        sleep(0.5)
        self.traffic_middle.config(bg=self.lights[1])
        self.frame.update()
        self.frame.after(500, self.__out_of_order)


root = tk.Tk()
TrafficLight(root, 'red', 'yellow', 'green')
root.mainloop()
