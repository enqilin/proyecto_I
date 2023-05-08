
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
                    "saldo_pendiente": round(amor_pendiente, 2),
                    "capital_mes": round(capital_mensual, 2),
                    "intereses_mes": round(interes_mensual, 2),
                    "cuota": round(cuota, 2)})

            else:
                capital_mensual = 0
                cuota = (self.tasa) * amor_pendiente
                tabla_amortizacion.append({
                    "mes": mes,
                    "saldo_pendiente": round(amor_pendiente, 2),
                    "capital_mes": round(capital_mensual, 2),
                    "intereses_mes": round(interes_mensual, 2),
                    "cuota": round(cuota, 2)})

        return tabla_amortizacion