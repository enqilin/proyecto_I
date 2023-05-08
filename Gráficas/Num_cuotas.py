import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con Pandas
df = pd.read_csv('Gráficas/24461bsc.csv', sep=';')

# Contar las veces que se repite cada número en la columna "Total"
counts = df['Total'].value_counts()

# Crear un gráfico circular
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title('Número de cuotas más común entre 2003-2023')
plt.show()