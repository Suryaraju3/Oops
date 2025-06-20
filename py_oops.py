

#Ex:1
# class WhatsApp:
#     app="Whatsapp is a chatting app"
# wtsapp=WhatsApp()
# print(wtsapp.app)

#Ex:2
#self ==>abc
# class Whats_app:
#     def __init__(abc,co_found,launchedyear):
#         abc.co_found=co_found
#         abc.lyear=launchedyear
# wtsapp2=Whats_app("Jan Koum and Brian Acton", 2009)
# print(wtsapp2.co_found)
# print(wtsapp2.lyear)

# 1.Inheritance
# class Whtsapp_v1:
#     def contact(self):
#         print("contact added on the whatsapp chatbox")
# class Whtsapp_v2(Whtsapp_v1):
#     def camara(self):
#         print("camara added on the whatsapp chatbox")
# ob=Whtsapp_v2()
# ob.contact()
# ob.camara()


#2.multilevel inheritance
# class Whtsapp_v1:
#     def contact(self):
#         print("contact added on the whatsapp chatbox")
# class Whtsapp_v2(Whtsapp_v1):
#     def camara(self):
#         print("camara added on the whatsapp chatbox")
# class Whtsapp_v3(Whtsapp_v2):
#     def document(self):
#         print("Document added on the whatsapp chatbox")
# obj2=Whtsapp_v3() 
# obj2.contact()
# obj2.camara()
# obj2.document()


# Hierarchical inheritance
# class Whtsapp_v1:
#     def contact(self):
#         print("contact added on the whatsapp chatbox")
# class Whtsapp_v2(Whtsapp_v1):
#     def camara(self):
#         print("camara added on the whatsapp chatbox")
# class Whtsapp_v3(Whtsapp_v1):
#     def document(self):
#         print("Document added on the whatsapp chatbox")
# obj2=Whtsapp_v3() 
# obj2.contact()
# obj2.document()
# #=================
# obj1=Whtsapp_v2()
# obj1.contact()
# obj1.camara()


#.multiple inheritance

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

        