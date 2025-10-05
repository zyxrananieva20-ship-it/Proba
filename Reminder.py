from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set():
    rem = sd.askstring('Время напоминания', 'Введите время напоминания в формате ЧЧ:ММ (в 24 часовом формате)')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка {e}')



window = Tk()
window.title('Напоминание')
Label = Label(text='Установите напоминание')
Label.pack(pady=10)
set_button = Button(text='Установить напоминание', command=set)
set_button.pack()

window.mainloop()