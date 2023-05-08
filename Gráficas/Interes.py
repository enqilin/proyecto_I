import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con Pandas
df = pd.read_csv('Gráficas/series1645008194c.csv')

df = df.sort_values(by='PeRIODO')

# Crear la gráfica con Matplotlib
plt.plot(df['PeRIODO'], df['VaLOR'])
plt.xlabel('Periodo')
plt.ylabel('Tipo de interés medio (%)')
plt.title('Gráfica de periodo vs valor')
plt.xticks(rotation=90)
plt.show()
