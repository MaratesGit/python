import pprint
import time
class Human:
    def __init__(self,name,age=0):
        self.name=name
        self.age=age
class Planet:
    def __init__(self,name,population=None):
        self.name=name
        self.population=population or []
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Planet {self.population}"

    def add_human(self,human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)
        
class Robot:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    
class timer:
    def __init__(self):
        self.start=time.time()

    def __enter__(self):
        return

    def __exit__(self,*args):
        print(time.time()-self.start)

with timer():

    time.sleep(5)
    

wallee=Robot("wallee")
print(wallee.name)


Earth=Planet("Earth")
Mark=Human("Mark",19)

Earth.add_human(Mark)
print(Earth.population)
