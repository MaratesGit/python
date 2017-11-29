import socket
import time
import pickle
import json
import string
HOST = '127.0.0.1'        
PORT = 50009
def config_connection(HOST,PORT):   
    s = socket.socket()
    try:
        s.bind((HOST, PORT))
    except ConnectionError:
        print("Ошибка соединения с сервером")
        exit(2)
    s.listen(5)
    conn, addr = s.accept()
    #print('Connected client',addr)
    conn.send(byte_processes)
    print('Config files sended: ', processes)
    conn.close()
try:
    with open("conf.txt") as file:#получение из конф.файла имена нужных процессов
        processes = [row.strip() for row in file]
except FileNotFoundError:
    print("Ошибка открытия конфигурационного файла")
    exit(1)
byte_processes = pickle.dumps(processes, protocol=0)# перевод процессов в байт-код

config_connection(HOST,PORT)
#вторая передача
while 1:
    s = socket.socket()
    try:
        s.bind((HOST, PORT))
    except ConnectionError:
        print("Ошибка соединения с сервером")
        exit(3)
    s.listen(5)
    conn, addr = s.accept()
    #print('Connected client',addr)
    
    while 1:
        pid_time_pickled = conn.recv(4096)
        if not pid_time_pickled:
            break
        else:
            try:
                pickleddata=pickle.loads(pid_time_pickled)
            except Exception:
                print("Конфигурационные данные повреждены / не получены в полном объеме")
                exit(9)
            print('Connected client',addr)
            print("Название".ljust(15),"Время работы".rjust(15))
           
            for key in pickleddata:
                print (key.ljust(15),pickleddata[key].rjust(15))
            print('\n')
    conn.close()
    
                 
    with open ('monitor.txt','a') as f:#запись словаря с полученными данными в файл
        for key in pickleddata:
              f.write(key.ljust(15))
              f.write(pickleddata[key].rjust(15))
        f.write('\n')
      
      



"""
    with open ('monitor.txt','a') as f: #запись словаря с полученными данными в файл
	json.dump(pickleddata, f)
	f.write('\n')



"""
        
