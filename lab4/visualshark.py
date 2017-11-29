from tkinter import *
import tkinter.ttk as ttk

root = Tk()#создание окна
root.title('Packages')#установка заголовка окна
nb = ttk.Notebook(root)#виджет с вкладками
nb.pack(fill='both', expand='yes')#вывод виджета с вкладками
TCP = Text(root)#класс многострочного текстогого поля
UDP = Text(root)#класс многострочного текстогого поля
ALL = Text(root)#класс многострочного текстогого поля
try:
    with open('packets.txt') as fTCP: #добавление
        for line in fTCP:             #пакетов на  
            TCP.insert(END,line)      #на вкладку
            TCP.pack()
except Exception:
    print("File with TCP packages is not exist")
    exit()
try:
    with open('packets1.txt') as fUDP: #добавление
        for line in fUDP:              #пакетов
            UDP.insert(END,line)       #на вкладку
            UDP.pack()
except Exception:
    print("File with UDP packages is not exist")
    exit()
try:
    with open('packets2.txt') as fALL: #добавление
        for line in fALL:              #пакетов
            ALL.insert(END,line)       #на вкладку
            ALL.pack()
except Exception:
    print("File with all packages is not exist")
    exit()

nb.add(TCP, text='TCP')#вывод вкладки на экран
nb.add(UDP, text='UDP')#вывод вкладки на экран
nb.add(ALL, text='TCP/UDP')#вывод вкладки на экран

root.mainloop()








