
class AmortizacionFrancesa:
    def __init__(self, capital_inicial, tasa_interes, plazo_meses):
        self.capital_inicial = capital_inicial
        self.tasa_interes = tasa_interes
        self.plazo_meses = plazo_meses
    
    def calcular_cuota_mensual(self):
        i = self.tasa_interes
        n = self.plazo_meses
        cuota = self.capital_inicial / ((1 - ((1+i)**(-n))) / i)
        return cuota
    
    def calcula_amortizacion_francesa(self):
        cuota_mensual = self.calcular_cuota_mensual()
        saldo_deuda = self.capital_inicial
        tabla_amortizacion = []
        
        # Agregamos el mes 0 a la tabla de amortización con los valores iniciales
        tabla_amortizacion.append({
            "mes": 0,
            "cuota": 0,
            "interes": 0,
            "amortizacion": 0,
            "saldo_deuda": saldo_deuda
        })
        
        for mes in range(1, self.plazo_meses+1):
            interes_mensual = saldo_deuda * (self.tasa_interes)
            amortizacion_mensual = cuota_mensual - interes_mensual
            saldo_deuda -= amortizacion_mensual
            tabla_amortizacion.append({
                "mes": mes,
                "cuota": cuota_mensual,
                "interes": interes_mensual,
                "amortizacion": amortizacion_mensual,
                "saldo_deuda": saldo_deuda
            })
        
        return tabla_amortizacion
    
    def tabla_amortizacion_francesa(self):
        print("\nMODELO AMORTIZACIÓN FRANCÉS")
        amortizacion_francesa = AmortizacionFrancesa(self.capital_inicial, self.tasa_interes, self.plazo_meses)
        tabla_amortizacion = amortizacion_francesa.calcula_amortizacion_francesa()
        
        print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
        print("-"*85)
        
        for fila in tabla_amortizacion:
            print("{:^10d} | {:^15.2f} | {:^15.2f} | {:^15.2f} | {:^15.2f}".format(fila["mes"], fila["cuota"], fila["interes"], fila["amortizacion"], fila["saldo_deuda"]))
