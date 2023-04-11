import pandas as pd

class AmortizacionFrancesa:
    def __init__(self, capital, tasa_interes, plazo):
        self.capital = capital
        self.tasa_interes = tasa_interes
        self.plazo = plazo
    
    def calcular_cuota_mensual(self):
        r = self.tasa_interes / 12
        n = self.plazo * 12
        cuota = (self.capital * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
        return cuota
    
    def generar_tabla_amortizacion(self):
        cuota_mensual = self.calcular_cuota_mensual()
        saldo_pendiente = self.capital
        interes_total = 0
        capital_total = 0
        filas = []
        for mes in range(1, self.plazo * 12 + 1):
            interes = saldo_pendiente * (self.tasa_interes / 12)
            capital = cuota_mensual - interes
            saldo_pendiente -= capital
            interes_total += interes
            capital_total += capital
            fila = {'Mes': mes, 'Cuota': cuota_mensual, 'Intereses': interes, 'Capital': capital, 'Saldo pendiente': saldo_pendiente}
            filas.append(fila)
        
        tabla = pd.DataFrame(filas)
        tabla = tabla[['Mes', 'Cuota', 'Intereses', 'Capital', 'Saldo pendiente']]
        tabla = tabla.round(2)
        tabla = tabla.set_index('Mes')
        return tabla

prestamo = AmortizacionFrancesa(100000, 0.05, 10)
tabla = prestamo.generar_tabla_amortizacion()
print(tabla)
