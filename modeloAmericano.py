class americano:
    def __init__(self,prestamo,tasa,plazo):
        self.prestamo = prestamo
        self.plazo = plazo
        self.tasa = tasa

    def calcula_amortizacion(self):
        amor_pendiente = self.prestamo
        cuota = 0
        interes_total = 0
        cuota_total = 0
        capital_total = 0
        tabla_amortizacion =[]
        for mes in range(1 , self.plazo * 12 + 1):
            interes_mensual = (self.tasa /12)*self.prestamo
            interes_total += interes_mensual
            amor_pendiente = self.prestamo
            if mes == self.plazo*12:
                capital_mensual = self.tasa / 12 +self.prestamo
                amor_pendiente-= capital_mensual
                cuota = (self.tasa/ 12) *self.prestamo + self.prestamo
                cuota_total+=cuota
                capital_total+=capital_mensual
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes":interes_mensual,
                    "cuota" :cuota})
                
            elif mes == self.plazo*12 +1:
                capital_mensual = self.tasa / 12
                cuota = (self.tasa/ 12) *self.prestamo
                cuota_total+=cuota
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente":amor_pendiente ,
                    "capital_mes": capital_total,
                    "intereses_mes":interes_total,
                    "cuota" :cuota_total})
            else:
                capital_mensual = self.tasa / 12
                cuota = (self.tasa/ 12) *self.prestamo
                cuota_total+=cuota
                capital_total+=capital_mensual
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes":interes_mensual,
                    "cuota" :cuota})
        return tabla_amortizacion
    
    
    def imprimir_tabla_amortizacion(self):
        tabla_amortizacion = self.calcula_amortizacion()
        print("{:^10s}{:^20s}{:^20s}{:^20s}{:^20s}".format("Mes", "Saldo Pendiente", "Capital Mes", "Intereses Mes", "Cuota"))
        for registro in tabla_amortizacion:
            print("{:^10d}{:^20.2f}{:^20.2f}{:^20.2f}{:^20.2f}".format(registro["mes"], registro["saldo_pendiente"], registro["capital_mes"], registro["intereses_mes"], registro["cuota"]))
            
           



amortizacion = americano(100000, 0.025, 10)
tabla_amortizacion = amortizacion.calcula_amortizacion()

print("{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
print("-"*75)

for fila in tabla_amortizacion:
    print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))
cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
print("\nSuma de cuotas: {:,.2f}".format(cuota_sum))