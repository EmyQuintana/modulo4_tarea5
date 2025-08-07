class FormatoRutInvalido(Exception):
    def __init__(self, rut):
        self.rut = rut
        super().__init__(f"El RUT '{rut}' no tiene el formato válido. El rut debe tener 9 carácteres.")


    
        

