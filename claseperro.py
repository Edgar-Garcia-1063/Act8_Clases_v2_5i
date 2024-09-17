print("clases version 2 el constructor")

class perro:
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    #funciones creadas por el usuario
    def morder(self):
        print("mta, me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(self,mensajep):
        print(f"chat perra: {mensajep}")
    def datos(self):
        print(f"color {self.color} edad {self.edad}")
    
#crear objeto
chihuas=perro("negro",2)
#llamas a las funciones    
chihuas.datos()
chihuas.morder()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola totonaco")
chihuas.chatperro("quieres ser mi novia?")
chihuas.chatperra("alch no")
