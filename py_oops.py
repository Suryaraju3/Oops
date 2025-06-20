


class WhatsApp:
    app="Whatsapp is a chatting app"
wtsapp=WhatsApp()
print(wtsapp.app)


# self ==>abc
class Whats_app:
    def __init__(abc,co_found,launchedyear):
        abc.co_found=co_found
        abc.lyear=launchedyear
        
wtsapp2=Whats_app("Jan Koum and Brian Acton", 2009)
print(wtsapp2.co_found)
print(wtsapp2.lyear)

# 1.Inheritance
class Whtsapp_v1:
    def contact(self):
        print("contact added on the whatsapp chatbox")

class Whtsapp_v2(Whtsapp_v1):
    def camara(self):
        print("camara added on the whatsapp chatbox")
ob=Whtsapp_v2()
ob.contact()
ob.camara()


# 2.multilevel inheritance
class Whtsapp_v1:
    def contact(self):
        print("contact added on the whatsapp chatbox")

class Whtsapp_v2(Whtsapp_v1):
    def camara(self):
        print("camara added on the whatsapp chatbox")

class Whtsapp_v3(Whtsapp_v2):
    def document(self):
        print("Document added on the whatsapp chatbox")
obj2=Whtsapp_v3() 
obj2.contact()
obj2.camara()
obj2.document()


# 3.Hierarchical inheritance
class Whtsapp_v1:
    def contact(self):
        print("contact added on the whatsapp chatbox")

class Whtsapp_v2(Whtsapp_v1):
    def camara(self):
        print("camara added on the whatsapp chatbox")

class Whtsapp_v3(Whtsapp_v1):
    def document(self):
        print("Document added on the whatsapp chatbox")
obj2=Whtsapp_v3() 
obj2.contact()
obj2.document()
#=================
obj1=Whtsapp_v2()
obj1.contact()
obj1.camara()


# 4.multiple inheritance

class Whtsapp_v1:
    def contact(self):
        print("contact added on the whatsapp chatbox")

class Whtsapp_v2():
    def camara(self):
        print("camara added on the whatsapp chatbox")

class Whtsapp_v3():
    def document(self):
        print("Document added on the whatsapp chatbox")

class Whtsapp_v4(Whtsapp_v1,Whtsapp_v2,Whtsapp_v3):
    def ai_images(self):
        print("AI images added on the whatsapp chatbox")
objl=Whtsapp_v4()
objl.contact()
objl.camara()
objl.document()
objl.ai_images()


# 5.Hybrid inheritance
class Whtsapp_v1:
    def contact(self):
        print("contact added on the whatsapp chatbox")

class Whtsapp_v2(Whtsapp_v1):
    def camara(self):
        print("camara added on the whatsapp chatbox")

class Whtsapp_v3(Whtsapp_v1):
    def document(self):
        print("Document added on the whatsapp chatbox")

class Whtsapp_v4(Whtsapp_v2,Whtsapp_v3):
    def ai_images(self):
        print("AI images added on the whatsapp chatbox")

Obj1=Whtsapp_v2()
Obj1.contact()
Obj1.camara()
#==============
Obj2=Whtsapp_v3()
Obj2.contact()
Obj2.document()
#============
Obj3=Whtsapp_v4()
Obj3.contact()
Obj3.camara()
Obj3.document()
Obj3.ai_images()

# 2.Polymorphism
#Inbuild function
a = "Whatsapp"
print(len(a))

tuple = ("apple", "banana", "cherry")
print(len(tuple))

car = {
  "name": "BMW",
  "model": "Mustang",
  "year": 1940
}
print(len(car))



# Class Polymorphism
class Tamilnadu():
    def whatsapp(self):
        print("tamilnadu people using whatsapp")

class Andhra:
    def whatsapp(self):
        print("andhra people using whatsapp")

class kerala:
    def whatsapp(self):
        print("kerala people using whatsapp")

tamil=Tamilnadu()
andh=Andhra()
kera=kerala()
for x in (tamil,andh,kera):
    x.whatsapp()
        
        
# Inheritance    
class Whatsapp:
  def __init__(self,co_found,launchedyear):
    self.found = co_found
    self.lyear = launchedyear

class kerala(Whatsapp):
    def kerala(self):
        print("kerala people using whatsapp")


class andhra(Whatsapp):
  def andhra(self):
    print("andhra people using whatsapp!")
    
kk = kerala("Jan Koum and Brian Acton", 2009)       
aa = andhra("Jan Koum and Brian Acton", 2009)
kk.kerala()
aa.andhra()

# Method overriding&shadowing
class Whatsapp_v1:
    def chat(self):
        print("cotact,camara")

class Whatsapp_v2(Whatsapp_v1):
    def chat(self):
        print("location,document")
        super().chat
w2=Whatsapp_v2()
w2.chat()

# 3.Abstraction
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def account_no(self):
        pass           #This is an abstract method, no implementation here.
    @abstractmethod
    def ifsc_no(self):
        pass           #This is an abstract method, no implementation here.
class Bank_Book(Bank):
    def account_no(self):
        print("account number") # Abstract method, to be implemented by subclasses
    def ifsc_no(self):
        print("ifsc number")
B=Bank_Book()
B.account_no()
B.ifsc_no()

# 4.Encapsulation
# public access specifier
class Whatsapp:
    def __init__(self,co_found,launchedyear):
        self.found=co_found
        self.lyear=launchedyear
        #self is an object storing 
w=Whatsapp("Jan Koum and Brian Acton", 2009)
print(w.found)
print(w.lyear)

# Producted access specifier
class Whatsapp:
    def __init__(self,co_found,launchedyear):
        self._found=co_found
        self._lyear=launchedyear
        #self is an object storing 
wa=Whatsapp("Jan Koum and Brian Acton", 2009)
print(wa._found)
print(wa._lyear)
    
# Private access specifier   
class Whatsapp:
    def __init__(self,co_found,launchedyear):
        self.__found=co_found
        self.__lyear=launchedyear
        #self is an object storing 
wap=Whatsapp("surya",2009)
print(wap.__found)
print(wap.__lyear)

# # getter and setter
class Whatsapp: 
	def __init__(self, age=0): 
		self._mno = age 
  
	def get_age(self):  # getter method 
		return self._age 
 
	def set_age(self, x): # setter method
		self._age = x 

objset = Whatsapp() 
objset.set_age(55)  # setting the age using setter 
print(objset.get_age())  # retrieving age using getter 
print(objset._age)
        
