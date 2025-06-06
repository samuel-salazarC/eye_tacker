import cv2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cargar_datos(ruta_imagen, ruta_csv):
    imagen = cv2.imread(ruta_imagen)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    datos = pd.read_csv(ruta_csv)
    return imagen, datos

def generar_heatmap(imagen, datos, titulo='Heatmap'):
    plt.figure(figsize=(12, 8))
    plt.imshow(imagen)

    sns.kdeplot(
        x=datos['x'],
        y=datos['y'],
        cmap='plasma',
        fill=True,
        alpha=0.5,
        thresh=0.05,
        levels=100
    )

    plt.axis('off')
    plt.title(titulo)
    plt.show()

if __name__ == "__main__":
    ruta_mockup = 'mockup_bueno.png'
    ruta_datos = 'datos_mockup_generado.csv'

    imagen, datos = cargar_datos(ruta_mockup, ruta_datos)
    generar_heatmap(imagen, datos, titulo='Heatmap - Eye Tracking')
