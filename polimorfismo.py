class auto():
    
    def desplazamiento(self):
        print("Tiene 4 ruedas")

class moto():
    def desplazamiento(self):
        print("Tiene 2 ruedas")

class camion():
    def desplazamiento(self):
        print("Tiene 6 ruedas")


def despazamiento_vehiculo(vehiculo):           #POLIMORFISMO (Puede transformarse en ncualquier clase)
    vehiculo.desplazamiento()



mi_vehiculo=camion()
despazamiento_vehiculo(mi_vehiculo)

mi_vehiculo=auto()
despazamiento_vehiculo(mi_vehiculo)

mi_vehiculo=moto()
despazamiento_vehiculo(mi_vehiculo)

"""
mi_vehiculo=moto()
mi_vehiculo.despazamiento()

mi_vehiculo2=auto()
mi_vehiculo2.desplazamiento()

mi_vehiculo3=camion()
mi_vehiculo3.desplazamiento()
"""