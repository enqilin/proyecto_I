import datetime

class Prestamo:
    def __init__(self, monto, tasa_interes_anual, plazo_meses, fecha_inicio):
        self.monto = monto
        self.tasa_interes_mensual = tasa_interes_anual / 12
        self.plazo_meses = plazo_meses
        self.fecha_inicio = fecha_inicio
        
    def calcular_tabla_amortizacion(self):
        saldo_pendiente = self.monto
        pago_mensual = saldo_pendiente / self.plazo_meses
        tabla = []
        
        for i in range(self.plazo_meses):
            intereses = saldo_pendiente * self.tasa_interes_mensual
            capital_amortizado = pago_mensual - intereses
            saldo_pendiente -= capital_amortizado
            fecha = self.fecha_inicio + datetime.timedelta(days=30*i)
            tabla.append((fecha.strftime('%Y-%m-%d'), pago_mensual, intereses, capital_amortizado, saldo_pendiente))
            
        return tabla

# Crear objeto Prestamo
prestamo = Prestamo(monto=10000, tasa_interes_anual=0.06, plazo_meses=12, fecha_inicio=datetime.date(2023, 1, 1))

# Calcular tabla de amortización
tabla_amortizacion = prestamo.calcular_tabla_amortizacion()

# Imprimir tabla de amortización
print("{:12} {:16} {:16} {:20} {:20}".format("Fecha", "Pago mensual", "Intereses", "Capital amortizado", "Saldo pendiente"))
for fila in tabla_amortizacion:
    print("{:12} {:16.2f} {:16.2f} {:20.2f} {:20.2f}".format(*fila))
