class Modelo_Aleman():
    def __init__(self, V, interes, n):
        self.V=V
        self.interes=interes
        self.n=n
        self.capital_amortizado=self.V/self.n


    def intereses(self):
        lista_intereses=[]
        lista_saldoDeudor=[]

        for i in range (self.n):
            if i==1:
                cuota_interes=self.V*self.interes

                lista_intereses.append(cuota_interes)
                lista_saldoDeudor.append(self.V)
            else:
                saldo_deudor-=self.capital_amortizado
                cuota_interes=saldo_deudor*self.interes

                lista_intereses.append(cuota_interes)
                lista_saldoDeudor.append(saldo_deudor)

        return lista_saldoDeudor, lista_intereses
    
    def cuota(self, lista2):
        lista_cuota=[]
        for i in range(self.n):
            cuota=self.capital_amortizado+lista2[i]
            lista_cuota.append(cuota)
        return lista_cuota
    
    def main(self):
        lista1, lista2=intereses()        #lista1=lista_saldoDeudor #lista2=lista_intereses
        lista3=cuota(lista2)            #lista3=lista_cuota
        for i in range(self.n):
            print ("Saldo Deudor: {} Interes: {} Capital amortizado: {} Cuota: {}\n".format(lista1[i], lista2[i], self.capital_amortizado, lista3[i]))



valor_prestamo = input("Indique el valor del préstamo\n")
interes = input("Indique el tipo de interes\n")
nºcuotas = input("Indique el número de cuotas\n")

Modelo_Aleman(valor_prestamo, interes, nºcuotas)
