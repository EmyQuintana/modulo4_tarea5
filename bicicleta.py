class Bicicleta:  # Creamos la clase bicicleta
    def __init__(self, id_bicicleta, marca, modelo, disponibilidad, precio):
        self.id_bicicleta = id_bicicleta
        self.marca = marca
        self.modelo = modelo
        self.disponibilidad = disponibilidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_bicicleta}, Marca: {self.marca}, Modelo: {self.modelo}, Disponibilidad: {self.disponibilidad}, Precio: {self.precio}"
    
    def registrar (self):
        pass