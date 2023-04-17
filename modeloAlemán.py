class Modelo_Aleman():
    def __init__(self, V, interes, n):
        self.V=V
        self.interes=interes
        self.n=n
    
    def capital_amortizado(self):
        capital_amortizado=self.V/self.n
        return capital_amortizado

    def saldo_deudor(self):
        capital_amortizado=capital_amortizado()
        saldo_deudor-=capital_amortizado
        return saldo_deudor

    def cuota_interes(self):
        x=saldo_deudor()
        interes=x*self.interes


def aleman():
    lista_cuota_interes=[]    
    lista_saldo_deudor=[]
    lista_cuota=[]

    capital_amortizado=V/n
    saldo_deudor=V
    i=0
    while i<=12:      
        cuota_interes=saldo_deudor*interes
        lista_cuota_interes.append(cuota_interes)

        saldo_deudor=saldo_deudor-capital_amortizado
        lista_saldo_deudor.append(saldo_deudor)

        cuota=cuota_interes + capital_amortizado
        lista_cuota.append(cuota)
        print ("Cuota: {} Interes: {} Capital amortizado: {}\n".format(cuota, cuota_interes, capital_amortizado))
    
        i+=1
        

aleman()



valor_prestamo = input("Indique el valor del préstamo\n")
interes = input("Indique el tipo de interes\n")
nºcuotas = input("Indique el número de cuotas\n")

Modelo_Aleman(valor_prestamo, interes, nºcuotas)
