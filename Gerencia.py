from Empleado import *

class Gerencia(Empleado):

    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerencia: [Depto: {self.departamento}] {super().__str__()}'
