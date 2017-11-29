import os, string, subprocess, re
import urllib.request
import urllib.parse
import socket
import pickle
import time
import mymod#mymod.py в нем две функции
HOST = '127.0.0.1'
PORT = 50009
pid_time = {}
s = socket.socket()
try: #проверка на ошибку соединения
    s.connect((HOST, PORT))
except ConnectionError:
    print("Ошибка соединения с сервером1")
    exit(1)
try: #проверка целостность полученных данных
    process_names = s.recv(4096)
    s.close()
    print('Received[4]: ', pickle.loads(process_names))
except Exception:
    print("Конфигурационные данные повреждены / не получены в полном объеме")
    exit(9)
process_names = pickle.loads(process_names)#передача в список названий полученных процессов

while 1:
    for i in range(len(process_names)): # в цикле перебираются полученные имена и выводится словарь {pid:time}
        pid = mymod.getpid(process_names[i])
        if (pid == None): #если ф-ия вернула none, значит приложение не запущено
            continue
        pid_time[process_names[i]] = mymod.process_time(pid)
    print("Запущенные приложения:", end=' ')
    print(pid_time)
    s = socket.socket()
    try:
        s.connect((HOST, PORT))
    except ConnectionError:
        print("Соединение с сервером потеряно")
        exit(2)
    pid_time_pickled = pickle.dumps(pid_time, protocol=0)
    s.send(pid_time_pickled)
    s.close()
    pid_time={}  #обнуление словаря
    time.sleep(5) #пауза между отправкой на сервер данных о запущенных приложениях(в сек)


# в result[0] хранится время работы процесса
#ps -eo pid,etime | grep $PID | awk '{print $2}' вывести время работы процесса!

