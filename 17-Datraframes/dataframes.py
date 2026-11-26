import pandas as pd

data = [[1, 'Juan', 23], [2, 'Ana', 25], [3, 'Luis', 30]]
df = pd.DataFrame(data, columns=['ID', 'Nombre', 'Edad'])
print(df)

# Seleccionar una fila por índice
print(df.loc[1])

# Seleccionar múltiples filas
print(df.loc[[0, 2]])

# Seleccionar una columna específica
print(df.loc[:, 'Nombre'])

# Seleccionar un subconjunto específico
print(df.loc[0:2, ['ID', 'Edad']])

print(df.head())  # Muestra las primeras 5 filas (por defecto)
print(df.tail(2))  # Muestra las últimas 2 filas

print(df.describe())  # Estadísticas de las columnas numéricas