import datetime
from bicicleta import Bicicleta
from error import FormatoRutInvalido

class Reservas (Bicicleta): 
    def __init__(self, rut_cliente, id_reserva, fecha_inicio, fecha_fin, bicicleta): 
        # La reserva tiene una bicicleta como atributo
        self.bicicleta = bicicleta
        self.rut_cliente = rut_cliente
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


    def reserva (self):
        try:
            cliente = input("Ingrese su rut (sin puntos ni guión):")
            if len(cliente) == 9:
                print(f"El rut es: {cliente}")
            else:
                raise FormatoRutInvalido(cliente)
        except FormatoRutInvalido as e:
            print(f"Error: {e}")


        if self.disponibilidad == True:
            print(f"La bicicleta {self.id_bicicleta} está Disponible")
        else:
            print(f"La bicicleta {self.id_bicicleta} está Reservada")
    

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

            
        
        