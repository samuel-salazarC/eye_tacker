import cv2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(image_path, csv_path):
    # Load the image and convert BGR to RGB for proper display in matplotlib
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Load the eye tracking coordinates from CSV
    data = pd.read_csv(csv_path)
    return image, data

def generate_heatmap(image, data, title='Heatmap'):
    plt.figure(figsize=(12, 8))
    plt.imshow(image)

    sns.kdeplot(
        x=data['x'],
        y=data['y'],
        cmap='plasma',
        fill=True,
        alpha=0.5,
        thresh=0.05,
        levels=100
    )

    plt.axis('off')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    image_path = 'mockup_good.png'
    csv_path = 'generated_mockup_data.csv'

    image, data = load_data(image_path, csv_path)
    generate_heatmap(image, data, title='Eye Tracking Heatmap')
