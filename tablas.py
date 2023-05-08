"""""
# Guardar la tabla de amortización en un archivo
self.guardar_tabla_amortizacion(tabla_amortizacion)
        

    def guardar_tabla_amortizacion(self, tabla_amortizacion):
        # Obtener el nombre del archivo
        nombre_archivo = filedialog.asksaveasfilename(
            initialdir = "/",
            title = "Guardar archivo",
            filetypes = (("Archivo CSV", "*.csv"),)
        )

        # Crear el archivo
        archivo = open(nombre_archivo, "w", newline="")
        # Crear el objeto para escribir en el archivo
        escritor = csv.writer(archivo, delimiter=",")
        # Escribir los registros en el archivo
        escritor.writerow(("mes", "cuota", "intereses", "capital", "saldo"))
        for registro in tabla_amortizacion:
            escritor.writerow((
                registro["mes"],
                registro["cuota"],
                registro["intereses_mes"],
                registro["capital_mes"],
                registro["saldo_pendiente"]
            ))
        # Cerrar el archivo
        2archivo.close()

"""""