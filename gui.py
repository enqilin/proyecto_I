import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from modelo_aleman import *
from modelo_americano import *
from modelo_frances import *



class VentanaAmortizacion:
    
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de Amortización")
        self.ventana.geometry("1200x800")
        
        # Crear los widgets
        lbl_prestamo = ttk.Label(self.ventana, text="Monto del préstamo en euros:")
        self.entry_prestamo = ttk.Entry(self.ventana)
        
        lbl_tasa = ttk.Label(self.ventana, text="Tasa de interés:\n(en %)")
        self.entry_tasa = ttk.Entry(self.ventana)
        
        lbl_plazo = ttk.Label(self.ventana, text="Plazo en meses:")
        self.entry_plazo = ttk.Entry(self.ventana)
        
        lbl_tipo_amortizacion = ttk.Label(self.ventana, text="Tipo de modelo de amortización:")
        self.combo_tipo_amortizacion = ttk.Combobox(self.ventana, values=["Alemán", "Americano", "Francés"])
        self.combo_tipo_amortizacion.current(0)
        
        btn_calcular = ttk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.tabla_amortizacion = ttk.Treeview(self.ventana, columns=("mes", "cuota", "intereses", "capital", "saldo"), show="headings", height=24)
        
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
        
        btn_calcular.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        self.tabla_amortizacion.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
        
        # Configurar la tabla de amortización
        self.tabla_amortizacion.column("#0", width=0, stretch=tk.NO)
        self.tabla_amortizacion.column("mes", anchor=tk.CENTER, width=100)
        self.tabla_amortizacion.column("cuota", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("intereses", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("capital", anchor=tk.CENTER, width=200)
        self.tabla_amortizacion.column("saldo", anchor=tk.CENTER, width=200)

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
            

        # Suma de las columnan de las cuotas y de los intereses
        suma_cuotas = 0
        suma_intereses = 0
        for registro in tabla_amortizacion:
            suma_cuotas += registro["cuota"]
            suma_intereses += registro["intereses_mes"]

        # Insertar el total de las cuotas y de los intereses
        self.tabla_amortizacion.insert("", tk.END, text="", values=(
            "Total",
            round(suma_cuotas,2),
            round(suma_intereses,2),
            "" ))

        # resaltar el total de las cuotas y de los intereses
        self.tabla_amortizacion.item(self.tabla_amortizacion.get_children()[-1], tags=("total",))
        self.tabla_amortizacion.tag_configure("total", background="#BBDEFB")
        
        # Mostrar el total de las cuotas y de los intereses
        lbl_total_cuotas = ttk.Label(self.ventana, text="Total de las cuotas: ")
        lbl_total_cuotas.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        lbl_total_cuotas_valor = ttk.Label(self.ventana, text=round(suma_cuotas,2))
        lbl_total_cuotas_valor.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        lbl_total_intereses = ttk.Label(self.ventana, text="Total de los intereses: ")
        lbl_total_intereses.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        lbl_total_intereses_valor = ttk.Label(self.ventana, text=round(suma_intereses,2))
        lbl_total_intereses_valor.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        lbl_total_pagado = ttk.Label(self.ventana, text="Total pagado: ")
        lbl_total_pagado.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        lbl_total_pagado_valor = ttk.Label(self.ventana, text=round(suma_cuotas + suma_intereses,2))
        lbl_total_pagado_valor.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        # Guardar la tabla de amortización en un archivo csv en un botón
        btn_guardar_csv = ttk.Button(self.ventana, text="Guardar tabla", command=lambda: self.guardar_tabla_amortizacion(tabla_amortizacion))
        btn_guardar_csv.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        # Crear botón para guardar la tabla como png
        btn_guardar_png = ttk.Button(self.ventana, text="Guardar tabla como png", command=self.guardar_tabla_amortizacion_png)
        btn_guardar_png.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        


    def guardar_tabla_amortizacion(self, tabla_amortizacion):
        # Guardar el archivo
        nombre_archivo = filedialog.asksaveasfilename(
            initialdir="data",
            filetypes=(("Archivo CSV", "*.csv"), ("Archivo PDF", "*.pdf")),
            title="Guardar la tabla de amortización como"
        )

        # Obtener la extensión del archivo
        extension = nombre_archivo.split(".")[-1]

        if extension == "csv":
            # Crear el archivo CSV
            archivo = open(nombre_archivo, "w", newline="")
            escritor = csv.writer(archivo, delimiter=",")
            escritor.writerow(("mes", "cuota", "intereses", "capital", "saldo"))
            for registro in tabla_amortizacion:
                escritor.writerow((
                    registro["mes"],
                    registro["cuota"],
                    registro["intereses_mes"],
                    registro["capital_mes"],
                    registro["saldo_pendiente"]
                ))
            archivo.close()
            messagebox.showinfo("Tabla guardada", "La tabla de amortización se ha guardado como archivo CSV.")
        
        else:
            messagebox.showwarning("Extensión incorrecta")


if __name__ == "__main__":
    ventana = VentanaAmortizacion() 