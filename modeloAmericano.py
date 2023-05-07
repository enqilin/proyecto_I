
class AmortizacionAmericana:
    def __init__(self,prestamo,tasa,plazo):
        self.prestamo = prestamo
        self.plazo = plazo
        self.tasa = tasa

    def calcula_amortizacion_americana(self):
        amor_pendiente = self.prestamo
        cuota = 0
        tabla_amortizacion = []
        # Agregar diccionario para el mes 0
        tabla_amortizacion.append({
                    "mes": 0,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": 0,
                    "intereses_mes": 0,
                    "cuota" :0})
        for mes in range(1 , self.plazo + 1):
            interes_mensual = (self.tasa) * amor_pendiente
            if mes == self.plazo:
                capital_mensual = self.prestamo
                amor_pendiente -= capital_mensual
                cuota = (self.tasa) * capital_mensual + self.prestamo
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes": interes_mensual,
                    "cuota": cuota})
            else:
                capital_mensual = 0
                cuota = (self.tasa) * amor_pendiente
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": amor_pendiente,
                    "capital_mes": capital_mensual,
                    "intereses_mes": interes_mensual,
                    "cuota": cuota})
            amor_pendiente -= capital_mensual
        return tabla_amortizacion

    def tabla_amortizacion_americana(self):
        tabla_amortizacion = self.calcula_amortizacion_americana()
        print("\n MODELO AMORTIZACIÓN AMERICANO")
        print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
        print("-"*85)

        for fila in tabla_amortizacion:
            print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))
        cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
        print("\nTotal a pagar: {:,.2f}".format(cuota_sum),"€")
        intereses_sum = sum([x['intereses_mes'] for x in tabla_amortizacion])
        print("\nTotal de intereses: {:,.2f}".format(intereses_sum),"€\n")