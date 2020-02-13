class Carrito():

    def __init__(self):                 #CONSTRUCTOR
        self.largo=250                  #PROPERTY
        self.ancho=160                  #PROPERTY
        self.__ruedas=4                 #PROPERTY AND ENCAPSULATED (ONLY can be modified from inside the class)
        self.__prendido=False           #PROPERTY AND ENCAPCULATED (ONLY can be modified from inside the class)

    def prender(self, estado):          #METHOD
        self.__prendido=estado
        if self.__prendido:
            checked=self.__check()
        if self.__prendido and checked:
            return "prendido"
        elif self.__prendido and not checked:
            return "con problemas"
        elif not self.__prendido:
            return "apagado"


    def data(self):                       #METHOD
        print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.ancho}, y un largo de {self.largo}.")


    def __check(self):                    #METHOD AND ENCAPSULATED (ONLY can be accesed by another methods inside the class)
        print("Checking car...")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False





#class partesCarrito()


print()
AMScar=Carrito()                        #OBJECT
prendido=AMScar.prender(True)

print(f"Mi carrito esta {prendido}")
AMScar.data()

print("-----------------------------------")


Jcar=Carrito()                          #OBJECT
Jcar.__ruedas=6                         #__ruedas cannot be modified cause of it is encapsulated
prendido2=Jcar.prender(False)
print(f"Mi carrito esta {prendido2}")
Jcar.data()
print()