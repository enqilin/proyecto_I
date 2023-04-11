def aleman():    
    V = 200000
    saldo_deudor=V
    capital_amortizado=V/12

    interes = 0.05
    n = 12
    interes[1]=i*V
 

    for i in range(n):        
        cuota_interes=saldo_deudor*interes
        saldo_deudor=saldo_deudor-capital_amortizado
        cuota=cuota_interes + capital_amortizado
        print(cuota, capital_amortizado, cuota_interes)
        #print ("Cuota: {} Interes: {} Capital amortizado: {}\n".format{Cuota, cuota_interes, capital_amortizado})






