import datetime
from bicicleta import Bicicleta

class Reservas (Bicicleta): 
    def __init__(self, rut_cliente, id_reserva,fecha_inicio, fecha_fin): 
        super().__init__(id_bicicleta, marca, modelo, disponibilidad, precio)
        self.rut_cliente = rut_cliente
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def reserva (self):
        if self.disponibilidad == False:
            print(f"La bicicleta {self.id_bicicleta} está No Disponible")
        else:
            print(f"La bicicleta {self.id_bicicleta} está Disponible")
    

    def cancelar_reserva (self):
        cancelar = input("Desea cancelar la reserva : si/no")
        if cancelar == "si":
            self.disponibilidad = True
            print(f"Se ha cancelado la reserva de la bicicleta {self.id_bicicleta}")
        else:
            print(f"Se confirma la reserva de la bicicleta {self.id_bicicleta}")

        return self
    
    def monto_pagar (self):
        monto = (self.fecha_fin - self.fecha_inicio).days * self.precio
        print(f"El monto a pagar es de: ${monto}")
        return self

    def pago (self):
        input("Presente la TDC : ")
        print("Pago realizado con éxito")
        self.disponibilidad = True
        return self

            
        
        