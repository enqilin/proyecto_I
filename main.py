from modeloAlemán import *
from modeloAmericano import *
from modeloFrances import *
from colorama import *
from termcolor import colored

def main():
    print(colored(Fore.LIGHTGREEN_EX + "\nMODELO AMORTIZACIÓN ALEMÁN"))
    amortizacion_alemana = AmortizacionAlemana(prestamo, interes, cuotas)
    tabla_amortizacion = amortizacion_alemana.calcula_amortizacion_alemana()

    print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
    print("-"*85)

    for fila in tabla_amortizacion:
        print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))

    cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
    print("\nTotal a pagar: {:,.2f}".format(cuota_sum),"€")
    intereses_sum = sum([x['intereses_mes'] for x in tabla_amortizacion])
    print("\nTotal de intereses: {:,.2f}".format(intereses_sum),"€")

    print(colored(Fore.LIGHTGREEN_EX+"\n \n MODELO AMORTIZACIÓN AMERICANO"))
    amortizacion_americana = AmortizacionAmericana(prestamo, interes, cuotas)
    tabla_amortizacion = amortizacion_americana.calcula_amortizacion_americana()

    print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
    print("-"*85)

    for fila in tabla_amortizacion:
        print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['intereses_mes'], fila['capital_mes'], fila['saldo_pendiente']))
    cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
    print("\nTotal a pagar: {:,.2f}".format(cuota_sum),"€")
    intereses_sum = sum([x['intereses_mes'] for x in tabla_amortizacion])
    print("\nTotal de intereses: {:,.2f}".format(intereses_sum),"€")

    print(colored(Fore.LIGHTGREEN_EX+"\n \n MODELO AMORTIZACIÓN FRANCÉS"))
    amortizacion_francesa = AmortizacionFrancesa(prestamo, interes, cuotas)
    tabla_amortizacion = amortizacion_francesa.calcula_amortizacion_francesa()

    print("\n{:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^15s}".format("Mes", "Cuota", "Interés", "Amortización", "Saldo de deuda"))
    print("-"*85)

    for fila in tabla_amortizacion:
        print("{:^10d} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f} | {:>15,.2f}".format(fila['mes'], fila['cuota'], fila['interes'], fila['amortizacion'], fila['saldo_deuda']))

    cuota_sum = sum([x['cuota'] for x in tabla_amortizacion])
    print("\nTotal a pagar: {:,.2f}".format(cuota_sum), "€")
    interes_sum = sum([x['interes'] for x in tabla_amortizacion])
    print("\nTotal de intereses: {:,.2f}".format(interes_sum), "€\n")

if __name__ == "__main__":
    prestamo = 10000
    interes = 0.03
    cuotas = 5
    main()