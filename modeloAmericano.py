class AmortizacionAmericana:
    def __init__(self,prestamo,tasa,plazo):
        self.prestamo = prestamo
        self.plazo = plazo
        self.tasa = tasa

    def calcula_amortizacion_americana(self):
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