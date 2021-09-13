from Gerencia import *
from Empleado import *

def imprimirDetalles(objeto):
        #print (objeto)
        print(type(objeto))
        print(empleado.mostrar_detalles())  #hace llamado a los str de la clase padre e hijas

empleado = Empleado('juan', 590)
imprimirDetalles(empleado)

gerente = Gerencia('Pato', 900, 'gerencia')
imprimirDetalles(gerente)