class americano:
    def __init__(self,prestamo,tasa,plazo):
        self.prestamo = prestamo
        self.plazo = plazo
        self.tasa = tasa

    def calcula_amortizacion(self):
        amor_pendiente = self.prestamo
        cuota = 0
        tabla_amortizacion =[]
        for mes in range(1 , self.plazo + 1):
            interes_mensual = (self.tasa )*self.prestamo
            amor_pendiente = self.prestamo
            if mes == self.plazo:
                capital_mensual = self.prestamo
                amor_pendiente-= capital_mensual
                cuota = (self.tasa) *self.prestamo + self.prestamo
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes":interes_mensual,
                    "cuota" :cuota})
            else:
                capital_mensual = 0
                cuota = (self.tasa) *self.prestamo
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes":interes_mensual,
                    "cuota" :cuota})
        return tabla_amortizacion



amortizacion = americano(10000, 0.025, 10)
tabla_amortizacion = amortizacion.calcula_amortizacion()

print("{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
print("-"*75)

for fila in tabla_amortizacion:
    print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))
cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
print("\nTotal a pagar: {:,.2f}".format(cuota_sum),"€")