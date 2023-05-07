import tkinter as tk
from tkinter import ttk

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
            "saldo_pendiente": round(saldo_deudor, 2),
            "capital_mes": round(capital_amortizado, 2),
            "intereses_mes": round(cuota_interes, 2),
            "cuota": round(cuota, 2)
        })


        tabla_amortizacion[-1]["capital_mes"] += round(saldo_deudor,2)
        tabla_amortizacion[-1]["cuota"] += round(saldo_deudor,2)

        return tabla_amortizacion
    

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

class AmortizacionFrancesa:
    def __init__(self, prestamo, tasa, plazo):
        self.prestamo = prestamo
        self.tasa = tasa
        self.plazo = plazo

    def calcula_amortizacion_francesa(self):
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
            "cuota": 0
        })

        cuota = (self.prestamo * (self.tasa/12) * ((1 + (self.tasa/12)) ** self.plazo)) / (((1 + (self.tasa/12)) ** self.plazo) - 1)
        cuota_total = cuota * self.plazo

        for mes in range(1, self.plazo + 1):
            cuota_interes = saldo_deudor * (self.tasa/12)
            interes_total += cuota_interes

            capital_amortizado = cuota - cuota_interes
            capital_total += capital_amortizado

            saldo_deudor -= capital_amortizado
            tabla_amortizacion.append({
                "mes": mes,
                "saldo_pendiente": round(saldo_deudor, 2),
                "capital_mes": round(capital_amortizado, 2),
                "intereses_mes": round(cuota_interes, 2),
                "cuota": round(cuota, 2)    
            })

        tabla_amortizacion[-1]["capital_mes"] += saldo_deudor
        tabla_amortizacion[-1]["cuota"] += saldo_deudor

        return tabla_amortizacion

class VentanaAmortizacion:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Amortización")
        self.ventana.geometry("1200x800")
        
        # Crear los widgets
        lbl_prestamo = ttk.Label(self.ventana, text="Monto del préstamo:")
        self.entry_prestamo = ttk.Entry(self.ventana)
        
        lbl_tasa = ttk.Label(self.ventana, text="Tasa de interés:\n(en %)")
        self.entry_tasa = ttk.Entry(self.ventana)
        
        lbl_plazo = ttk.Label(self.ventana, text="Plazo en meses:")
        self.entry_plazo = ttk.Entry(self.ventana)
        
        lbl_tipo_amortizacion = ttk.Label(self.ventana, text="Tipo de modelo de amortización:")
        self.combo_tipo_amortizacion = ttk.Combobox(self.ventana, values=["Alemán", "Americano", "Francés"])
        self.combo_tipo_amortizacion.current(0)
        
        btn_calcular = ttk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.tabla_amortizacion = ttk.Treeview(self.ventana, columns=("mes", "cuota", "intereses", "capital", "saldo"))
        
        self.tabla_amortizacion.heading("mes", text="Mes")
        self.tabla_amortizacion.heading("cuota", text="Cuota")
        self.tabla_amortizacion.heading("intereses", text="Intereses")
        self.tabla_amortizacion.heading("capital", text="Capital")
        self.tabla_amortizacion.heading("saldo", text="Saldo pendiente")
        
        # Ubicar los widgets en la ventana
        lbl_prestamo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_prestamo.grid(row=0, column=1, padx=10, pady=10)
        
        lbl_tasa.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_tasa.grid(row=1, column=1, padx=10, pady=10)
        
        lbl_plazo.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_plazo.grid(row=2, column=1, padx=10, pady=10)
        
        lbl_tipo_amortizacion.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.combo_tipo_amortizacion.grid(row=3, column=1, padx=10, pady=10)
        
        btn_calcular.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        
        self.tabla_amortizacion.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # Configurar la tabla de amortización
        self.tabla_amortizacion.column("#0", width=0, stretch=tk.NO)
        self.tabla_amortizacion.column("mes", anchor=tk.CENTER, width=100)
        self.tabla_amortizacion.column("cuota", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("intereses", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("capital", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("saldo", anchor=tk.CENTER, width=200)

        # Hacer la tabla más grande

        # Mostrar la ventana
        self.ventana.mainloop()

    def calcular(self):
        # Obtener los valores de los widgets
        prestamo = float(self.entry_prestamo.get())
        tasa = float(self.entry_tasa.get()) / 100
        plazo = int(self.entry_plazo.get()) 
        tipo_amortizacion = self.combo_tipo_amortizacion.get()
        
        # Crear el objeto de la clase correspondiente
        if tipo_amortizacion == "Alemán":
            amortizacion = AmortizacionAlemana(prestamo, tasa, plazo)
            tabla_amortizacion = amortizacion.calcula_amortizacion_alemana()
        elif tipo_amortizacion == "Americano":
            amortizacion = AmortizacionAmericana(prestamo, tasa, plazo)
            tabla_amortizacion = amortizacion.calcula_amortizacion_americana()
        elif tipo_amortizacion == "Francés":
            amortizacion = AmortizacionFrancesa(prestamo, tasa, plazo)
            tabla_amortizacion = amortizacion.calcula_amortizacion_francesa()
        
        # Mostrar la tabla de amortización
        self.muestra_tabla_amortizacion(tabla_amortizacion)

    def muestra_tabla_amortizacion(self, tabla_amortizacion):
        # Eliminar los registros de la tabla de amortización
        self.tabla_amortizacion.delete(*self.tabla_amortizacion.get_children())
        
        # Insertar los registros de la tabla de amortización
        for registro in tabla_amortizacion:
            self.tabla_amortizacion.insert("", tk.END, text="", values=(
                registro["mes"],
                registro["cuota"],
                registro["intereses_mes"],
                registro["capital_mes"],
                registro["saldo_pendiente"]
            ))

if __name__ == "__main__":
    ventana = VentanaAmortizacion()
    
