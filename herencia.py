class vehiculos():
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def state(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena}")


class furgoneta(vehiculos):         #HERENCY

    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado:
            return "Se ha cargado la furgoneta"
        else:
            return "La furgoneta se encuentra sin carga"



class vehiculo_electrico(vehiculos):        #HERENCY
    def __init__(self, marca_electrico, modelo_electrico):
        super().__init__(marca_electrico,modelo_electrico)              #** To set marca and modelo for a electrical vehicle
        self.autonomia=100
        self.cargando=False
    
    def bateria(self, state):
        self.cargando=state
        

    def states(self):
        super().state()
        print(f"Autonomia {self.autonomia}\nCargando: {self.cargando}")



class bicicleta_electrica(vehiculo_electrico,vehiculos):      #MULTIPLE HERENCY
    pass
        
    

class moto(vehiculos):              #HERENCY
    dowheelie=""

    def wheelie(self):
        self.dowheelie="Va en wheelie"

    def state(self):                #Re-writing a method
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelera: {self.acelera} \nFrena: {self.frena} \nWheelie: {self.dowheelie}")





mi_furgoneta=furgoneta("Mercedes Benz","Splinter")
mi_furgoneta.arrancar()
mi_furgoneta.state()
print(mi_furgoneta.carga(True))

print()

mi_moto=moto("BMW","S1000RR")
mi_moto.wheelie()
mi_moto.state()

print()

mi_bici=bicicleta_electrica("Nissan", "Leaf")
mi_bici.bateria(False)
mi_bici.states()

#print(isinstance(mi_bici,vehiculo_electrico))