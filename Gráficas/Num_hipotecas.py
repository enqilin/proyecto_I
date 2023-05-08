import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Gráficas/series2146907883c.csv')

df = df.sort_values(by='PERIODO')

plt.plot(df['PERIODO'], df['VALOR'])
plt.xlabel('Periodo')
plt.ylabel('Número de hipotecas registradas (miles)')
plt.title('Gráfica de periodo vs valor')
# ajustar el eje x para mostrar solo un valor cada 12 datos
plt.xticks(range(0, len(df['PERIODO']), 12), df['PERIODO'][::12])
plt.xticks(rotation=90)
plt.show()


# Encontrar el índice del valor más grande y del más pequeño
indice_maximo = df['VALOR'].idxmax()
indice_minimo = df['VALOR'].idxmin()

# Encontrar el periodo correspondiente a cada índice
periodo_maximo = df.at[indice_maximo, 'PERIODO']
periodo_minimo = df.at[indice_minimo, 'PERIODO']

# Imprimir los resultados
print("El valor más grande es:", df.at[indice_maximo, 'VALOR'], "en el periodo", periodo_maximo)
print("El valor más pequeño es:", df.at[indice_minimo, 'VALOR'], "en el periodo", periodo_minimo)