import random
from tkinter import *
import tkinter as tk
def globpass():
    lb=counter1.get() #Количество символов с верхним регистром
    ll=counter2.get() #Количество символов с нижним регистром
    ln=counter3.get() #Количество цифр
    ls=counter4.get()#Количество спец символов
        
    def Big():#Для символов с верхним регистром
        Pass=""
        for i in range(lb):                      
            n=random.randrange(len(Big_S))
            Pass=Pass+Big_S[n]
        return Pass
     
    def Low():#Для символов с нижним регистром
        Pass=""
        for i in range(ll):
            n=random.randrange(len(Low_S))
            Pass=Pass+Low_S[n]
        return Pass
     
    def Num():#Для цифр
        Pass=""
        for i in range(ln):
            n=random.randrange(len(Num_S))
            Pass=Pass+Num_S[n]
        return Pass
     
    def Spe():#Для спецсимволов
        Pass=""
        for i in range(ls):
            n=random.randrange(len(Spe_S))
            Pass=Pass+Spe_S[n]
        return Pass
     
    def All():
        Passlb,Passll,Passln,Passls="","","",""
        if lb>0:
            Passlb=Big()            
        if ll>0:
            Passll=Low()
        if ln>0:
            Passln=Num()
        if ls>0:
            Passls=Spe()
            
        PassA=Passlb+Passll+Passln+Passls
        PassR=list(PassA)
        random.shuffle(PassR)
        PassEnd=""
        
        for i in range(len(PassR)):
            PassEnd=PassEnd+PassR[i]
               
        return PassEnd
    
    passw.set("")
    passw.set(passw.get()+All())
    
def click1():
        counter1.set(counter1.get()+1)
def click1_2():
    if (counter1.get()<=0):
        counter1.set(0)
    else:
        counter1.set(counter1.get()-1)
def click2():
   counter2.set(counter2.get()+1)
def click2_1():
    if (counter2.get()<=0):
       
       counter2.set(0)
    else:
       counter2.set(counter2.get()-1)
def click3():
   counter3.set(counter3.get()+1)
def click3_1():
    if(counter3.get()<=0):
       counter3.set(0)
    else:
       counter3.set(counter3.get()-1)
def click4():
   counter4.set(counter4.get()+1)
def click4_1():
    if (counter4.get()<=0):
        counter4.set(0)
    else:
        counter4.set(counter4.get()-1)
Big_S=list('QWERTYUIOPASDFGHJKLZXCVBNM')
Low_S=list('qwertyuiopasdfghjklzxcvbnm')
Num_S=list('1234567890')
Spe_S=list('!@#$%^&;*()')    
Pass,PassA,passw="","",""     
window=Tk()
window.title("Password Generator")
window["bg"] = "#DDC6E2"
window.geometry("500x250+300+300")
texts=['▲','▼','▲','▼','▲','▼','▲','▼']
rows=[3,4,3,4,3,4,3,4]
cols=[0,0,1,1,2,2,3,3]
func=[click1,click1_2,click2,click2_1,click3,click3_1,click4,click4_1]#список ф-й, обрабатывающих клики
counter1,counter2,counter3,counter4=IntVar(),IntVar(),IntVar(),IntVar()
passw=StringVar()
counter1.set(0)
counter2.set(0)
counter3.set(0)
counter4.set(0)
passw.set("")
colorofbg="#DDC6E2"
colorfg="#BE2746"
counters=[counter1,counter2,counter3,counter4]
for t,r,c,z in zip(texts,rows,cols,func): #добавление кнопок,регулирующих кол-во символов в пароле
    Button(window,text=t,command=z,fg=colorofbg,activebackground="#D5BEBF",activeforeground="#C2191D",bg=colorfg).grid(row=r,column=c)

r=0
for r,c in zip (range (0,4),counters):
    Label(window,textvariable=c,bg=colorofbg,fg=colorfg).grid(row=1,column=r)
    r=r+1
 
Submit_Button=Button(window,text="Generate!",command=globpass,activebackground="#D5BEBF",
activeforeground="#C2191D",fg=colorofbg,bg=colorfg).grid(row=10,column=5)
Label_Pass=Label(window,textvariable=passw,bg=colorofbg,fg=colorfg,font=("Helvetica", 14)).grid(row=12,column=11)
Label_Text=Label(window,text="Password is: ",bg=colorofbg,fg=colorfg,font=("Helvetica", 14)).grid(row=12,column=5)
Big = Label(window, text="Big", font=("Helvetica", 9),bg=colorofbg,fg=colorfg).grid(row=5,column=0)
Small = Label(window, text="Small", font=("Helvetica", 9),bg=colorofbg,fg=colorfg).grid(row=5,column=1)
Digit = Label(window, text="Digit", font=("Helvetica", 9),bg=colorofbg,fg=colorfg).grid(row=5,column=2)
Spec = Label(window, text="Spec", font=("Helvetica", 9),bg=colorofbg,fg=colorfg).grid(row=5,column=3)
passw.set("")
window.mainloop()

 







