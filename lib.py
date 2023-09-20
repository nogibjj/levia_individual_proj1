import os
import polars as pl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #Show Chinese label
plt.rcParams['axes.unicode_minus']=False

def read_csv(file_path):
    return pl.read_csv(file_path)

def calculate_statistics(data):
    selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
    data = data[selected_columns]
    return data.describe()

def visualize_data(data, save_path):
     
    if not isinstance(data, pl.DataFrame):
        raise ValueError("Input is not a Polar DataFrame")
        # Create a directory to store the plots if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)

        # Iterate over each numeric column and create a histogram
    histogram_paths = []
    plt.figure(figsize=(8, 6))
    plt.hist(data["energy"], bins=20, edgecolor='k', alpha=0.7)
    plt.xlabel("energy")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of energy")
    plt.grid(True)
    if save_path:
        histogram_path = os.path.join(save_path, f"energy_histogram.png")
        plt.savefig(histogram_path)
        plt.close()
        histogram_paths.append(histogram_path)
    return histogram_paths
