
class AmortizacionAlemana:

    def __init__(self, prestamo, tasa, plazo):
        self.prestamo = prestamo
        self.tasa = tasa
        self.plazo = plazo
        self.total_cuotas = 0
        self.total_intereses = 0

    def calcula_amortizacion_alemana(self):
        saldo_deudor = self.prestamo
        cuota = 0
        interes_total = 0
        cuota_total = 0
        capital_total = 0
        tabla_amortizacion = []
        
        # Agregar diccionario para el mes 0
        tabla_amortizacion.append({
                    "mes": 0,
                    "saldo_pendiente": saldo_deudor,
                    "capital_mes": 0,
                    "intereses_mes": 0,
                    "cuota" :0})

        amortizacion = self.prestamo / (self.plazo)

        for mes in range(1, self.plazo + 1):
            cuota_interes = saldo_deudor * (self.tasa)
            interes_total += cuota_interes

            capital_amortizado = amortizacion
            cuota = cuota_interes + capital_amortizado
            cuota_total += cuota
            capital_total += capital_amortizado
            self.total_cuotas = cuota_total
            self.total_intereses = interes_total

            saldo_deudor -= capital_amortizado
            tabla_amortizacion.append({
            "mes": mes,
            "saldo_pendiente": round(saldo_deudor, 2),
            "capital_mes": round(capital_amortizado, 2),
            "intereses_mes": round(cuota_interes, 2),
            "cuota": round(cuota, 2)
        })


        tabla_amortizacion[-1]["capital_mes"] += round(saldo_deudor,2)
        tabla_amortizacion[-1]["cuota"] += round(saldo_deudor,2)

        return tabla_amortizacion
    