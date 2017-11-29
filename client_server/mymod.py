import os, string, subprocess, re
HOST = '127.0.0.1'
PORT = 50009
def getpid(name_of_process): #функция получения pid процесса,в аргументе имя
    req="pidof "+name_of_process +"|awk '{print$1}'"
    stdoutdata1 = subprocess.check_output(req, shell=True)
    stdoutdata1=str(stdoutdata1)    
    result1 = re.findall(r'\d', stdoutdata1)
    mystr = ''.join(result1) #склеивание элементов списка result1 в строку для удобства
    if len(mystr)==0:#dlina mystr 0 esli process ne zapushen
        print("Приложение "+name_of_process+" не запущено")
        return None
    else:
      return mystr
def process_time(pid): #функция получения времени работы процесса,в аргументе pid
    result = []
    req1="ps -eo pid,etime | grep "+pid+" | awk 'NR == 1{print$2}'" #команда bash
    stdoutdata = subprocess.check_output(req1, shell=True)
    stdoutdata=str(stdoutdata)
    stdoutdata = stdoutdata.replace('b', '')   #удаление
    stdoutdata = stdoutdata.replace('\\n', '') #лишних
    stdoutdata = stdoutdata.replace('\'', '')   #символов
    result.insert(0, stdoutdata)
    return (result[0])
