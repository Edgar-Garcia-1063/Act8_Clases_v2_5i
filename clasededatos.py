class Informacion:
    
    def  mi_lista(self):
        lista_Nomperras=["max", "lowez.cesar", "emi.dss"]
        for x in lista_Nomperras:
            print(x)

    def mi_conjunto(self):
        tamaños=["grandotas", "maso", "chiquillas"]
        for z in tamaños:
            print(z)


    def mi_tupla(self):
        razas=("pastor", "dalmata", "golden retriever")
        for y in razas:
            print(y)

    def mi_diccionario(self):
        carros2 = {
    "naco: ": "emoliano",
    "roblocs: ": "guisho",
    "wey: ": "larrondito"}

        for x, y in carros2.items():
            print(x,y)

datos=Informacion()


print("Listado de nombre de perros")
datos.mi_lista()
print("")
print("Conjunto de tamaños de perros")
datos.mi_conjunto()
print("")
print("Tuplas de razas de perros")
datos.mi_tupla()
print("")
print("Diccionario de dueños de perros")
datos.mi_diccionario()