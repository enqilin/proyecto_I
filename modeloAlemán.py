class aleman:
    def __init__(self, prestamo, tasa, plazo):
        self.prestamo = prestamo
        self.tasa = tasa
        self.plazo = plazo

    def calcula_amortizacion(self):
        saldo_deudor = self.prestamo
        cuota = 0
        interes_total = 0
        cuota_total = 0
        capital_total = 0
        tabla_amortizacion = []

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

    def imprimir_tabla_amortizacion(self):
        tabla_amortizacion = self.calcula_amortizacion()
        print("{:^10s}{:^20s}{:^20s}{:^20s}{:^20s}".format("Mes", "Saldo Pendiente", "Capital Mes", "Intereses Mes", "Cuota"))
        for registro in tabla_amortizacion:
            print("{:^10d}{:^20.2f}{:^20.2f}{:^20.2f}{:^20.2f}".format(registro["mes"], registro["saldo_pendiente"], registro["capital_mes"], registro["intereses_mes"], registro["cuota"]))

amortizacion = aleman(4000, 0.0385, 24)
tabla_amortizacion = amortizacion.calcula_amortizacion()

print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
print("-"*75)

for fila in tabla_amortizacion:
    print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))

cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
print("\nTotal a pagar: {:,.2f}".format(cuota_sum),"€")