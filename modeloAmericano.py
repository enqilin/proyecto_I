class AmortizacionAlemana:
    def __init__(self, monto, tasa, plazo):
        self.monto = monto
        self.tasa = tasa
        self.plazo = plazo

    def calcula_cuota(self):
        tasa_mensual = self.tasa / 12
        plazo_meses = self.plazo * 12
        cuota = (self.monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo_meses)
        return cuota

    def calcula_amortizacion(self):
        cuota = self.calcula_cuota()
        saldo_pendiente = self.monto
        intereses_total = 0
        tabla_amortizacion = []

        for mes in range(1, self.plazo * 12 + 1):
            intereses_mes = saldo_pendiente * self.tasa / 12
            capital_mes = cuota - intereses_mes
            saldo_pendiente -= capital_mes
            intereses_total += intereses_mes

            tabla_amortizacion.append({
                "mes": mes,
                "saldo_pendiente": saldo_pendiente,
                "capital_mes": capital_mes,
                "intereses_mes": intereses_mes,
                "cuota": cuota
            })

        return tabla_amortizacion

    def imprime_amortizacion(self):
        tabla_amortizacion = self.calcula_amortizacion()

        print("{:^10s}{:^20s}{:^20s}{:^20s}{:^20s}".format("Mes", "Saldo Pendiente", "Capital Mes", "Intereses Mes", "Cuota"))

        for registro in tabla_amortizacion:
            print("{:^10d}{:^20.2f}{:^20.2f}{:^20.2f}{:^20.2f}".format(registro["mes"], registro["saldo_pendiente"], registro["capital_mes"], registro["intereses_mes"], registro["cuota"]))

amortizacion = AmortizacionAlemana(100000, 0.05, 10)
amortizacion.imprime_amortizacion()
