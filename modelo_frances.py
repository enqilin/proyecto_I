
class AmortizacionFrancesa:
    
    def __init__(self, prestamo, tasa, plazo):
        self.prestamo = prestamo
        self.tasa = tasa
        self.plazo = plazo

    def calcula_amortizacion_francesa(self):
        saldo_deudor = self.prestamo
        cuota = 0
        tabla_amortizacion = []

        # Agregar diccionario para el mes 0
        tabla_amortizacion.append({
            "mes": 0,
            "saldo_pendiente": saldo_deudor,
            "capital_mes": 0,
            "intereses_mes": 0,
            "cuota": 0
        })

        cuota = self.prestamo / ((1 - ((1 + self.tasa) ** (-self.plazo))) / self.tasa)
        

        for mes in range(1, self.plazo + 1):
            interes_mensual = saldo_deudor * (self.tasa)
            amortizacion_mensual = cuota - interes_mensual
            saldo_deudor -= amortizacion_mensual
            tabla_amortizacion.append({
                "mes": mes,
                "saldo_pendiente": round(saldo_deudor, 2),
                "capital_mes": round(amortizacion_mensual, 2),
                "intereses_mes": round(interes_mensual, 2),
                "cuota": round(cuota, 2)
                  })


        return tabla_amortizacion