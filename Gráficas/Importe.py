import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con Pandas
df = pd.read_csv('Gráficas/series873286655c.csv')

df = df.sort_values(by='PERIODO')

# Crear la gráfica con Matplotlib
plt.plot(df['PERIODO'], df['VALOR'])
plt.xlabel('Periodo')
plt.ylabel('Importe medio (€)')
plt.title('Gráfica de periodo vs valor')
plt.xticks(rotation=90)
plt.show()
