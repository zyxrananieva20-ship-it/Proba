from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

window = Tk()
window.title('Напоминание')
Label = Label(text='Установите напоминание')
Label.pack(pady=10)
set_button = Button(text='Установить напоминание', command=set)
set_button.pack

window.mainloop()