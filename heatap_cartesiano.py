import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generar_heatmap_cartesiano(ruta_csv, titulo='Heatmap Cartesiano'):
    # Leer datos del CSV
    datos = pd.read_csv(ruta_csv)

    # Crear gráfico
    plt.figure(figsize=(10, 8))
    sns.kdeplot(
        x=datos['x'],
        y=datos['y'],
        cmap='inferno',
        fill=True,
        alpha=0.6,
        thresh=0.05,
        levels=100
    )
    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().invert_yaxis()  # Para que el eje Y coincida con coordenadas de pantalla
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ruta_datos = 'datos_mockup_generado.csv'  # Usa el archivo generado por eye_tracker.py
    generar_heatmap_cartesiano(ruta_datos)
