
class americano:
    def __init__(self,prestamo,tasa,plazo):
        self.prestamo = prestamo
        self.plazo = plazo
        self.tasa = tasa
    def calcula_cuota(self):
        tasa_mensual = self.tasa / 12
        plazo_mesual = self.plazo * 12
        for mes in range(1,plazo_mesual+1):
            if mes==self.plazo * 12:
                cuota = tasa_mensual*self.prestamo + self.prestamo
                return cuota
            else:
                cuota = tasa_mensual*self.prestamo
    def calcula_amortizacion(self):
        amor_pendiente = self.prestamo
        cuota =self.calcula_cuota()
        interes_total = 0
        tabla_amortizacion =[]
        for mes in range(1 , self.plazo * 12 + 1):
            interes_total = self.tasa / 12
            interes_mensual = (self.tasa /12)*self.prestamo
            amor_pendiente = self.prestamo
            if mes == self.plazo*12:
                capital_mensual = self.tasa / 12 +self.prestamo
                amor_pendiente-= capital_mensual
            else:
                capital_mensual = self.tasa / 12
            interes_total+= self.tasa /12
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
amortizacion = americano(100000, 0.05, 10)
amortizacion.imprimir_tabla_amortizacion()