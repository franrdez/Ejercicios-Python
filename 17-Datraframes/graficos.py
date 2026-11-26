import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
        'Ventas': [100, 120, 130, 90, 150]}
df = pd.DataFrame(data)

# Generar el gráfico de líneas
df.plot(x='Día', y='Ventas', kind='line', marker='o')
plt.title('Ventas diarias')
plt.xlabel('Día')
plt.ylabel('Ventas')
plt.grid()
plt.show()