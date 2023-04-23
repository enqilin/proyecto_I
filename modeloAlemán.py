class AmortizacionAlemana:
    def __init__(self, prestamo, tasa, plazo):
        self.prestamo = prestamo
        self.tasa = tasa
        self.plazo = plazo

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

            saldo_deudor -= capital_amortizado
            tabla_amortizacion.append({
                "mes": mes,
                "saldo_pendiente": saldo_deudor,
                "capital_mes": capital_amortizado,
                "intereses_mes": cuota_interes,
                "cuota": cuota
            })

        tabla_amortizacion[-1]["capital_mes"] += saldo_deudor
        tabla_amortizacion[-1]["cuota"] += saldo_deudor

        return tabla_amortizacion
