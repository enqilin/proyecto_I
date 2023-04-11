import math
def amortizacion_americana():
    prestamo = int(input("Cuanto quieres prestar: "))
    cuota = int(input("El periodo "))
    return prestamo,cuota


class americana(amortizacion_americana):
    def __init__(self,prestamo,cuota):
        self.prestamo = prestamo
        self.cuota = cuota

    def calculo_interes(self):
        inter=5
        interes= 
