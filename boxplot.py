# from statistics import mean
import pandas as pd
import time
import matplotlib.pyplot as plt

# Tempo inicial
start_time = time.time()
print("")
print('Estatísticas do dataset: ')
# carrega o arquivo csv
df = pd.read_csv('2022_02_15-2023_03_10.csv')
# Verifica quantas linhas estão presentes no dataset original
num_linhas_ini = len(df.index)
# remove caixa03 e testePy
df = df[~df['sensor'].isin(['testePy', 'caixa03'])]
#renomeia as unidades de medida
#df['measure'] = df['measure'].replace({'humidity': 'UR', 'temperature': 'Tmp'})

data_inicial = df['datetime'].min()
data_final = df['datetime'].max()

# filtra os dados de temperatura e umidade
df = df.loc[df['measure'].isin(['temperature', 'humidity'])]

# agrupa os dados por sensor e medida, e calcula as estatísticas
stats = df.groupby(['sensor', 'measure'])['valuemeasure'].agg(['min', 'max', 'median', 'mean'])
# exibe as estatísticas para cada sensor e medida
print(stats)
print("")

print("Data inicial dos dados em dataset:", data_inicial)
print("Data final dos dados em dataset  :", data_final)
print("Número de linhas do dataset com os sensores teste: {:,.0f}".format(num_linhas_ini).replace(",", "."))
num_linhas = len(df.index)
print("Número de linhas restantes após a retirada dos sensores de teste: {:,.0f}".format(num_linhas).replace(",", "."))


# Tempo final
end_time = time.time()

# Tempo total de execução
elapsed_time = end_time - start_time

print(f"Tempo total de execução: {elapsed_time:.2f} segundos")

# Boxplots agrupados por unidade de medida e por sensor
boxplot = df.boxplot(column='valuemeasure', by=['measure', 'sensor'], grid=True, patch_artist=False, showfliers=True)
boxplot.figure.set_size_inches(9,6)
boxplot.set_title('Medições por sensor')
boxplot.set_yticks(range(0, 101, 10))

plt.gcf().suptitle("")
plt.xlabel("Medições por sensor.")
plt.show()
