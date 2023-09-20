import os
import polars as pl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #Show Chinese label
plt.rcParams['axes.unicode_minus']=False

def read_csv(file_path):
    print("Successfully read!")
    return pl.read_csv(file_path)

def calculate_statistics(data):
    selected_columns = ['danceability', 'energy', 'artist_popularity', 'loudness']
    data = data[selected_columns]
    return data.describe()

def visualize_data(data, save_path):
    # Check if the 'energy' column exists in the data
    if 'energy' not in data.columns:
        print("Error: 'energy' column not found in the data.")
        return

    # Create a plot of the 'energy' column
    plt.figure(figsize=(10, 6))
    plt.plot(data['energy'], label='Energy')
    plt.title('Energy Data Visualization')
    plt.xlabel('Data Points')
    plt.ylabel('Energy')
    plt.legend()

    # Save the plot to the specified save_path
    plt.savefig(save_path)

    # Close the plot to release resources (optional)
    plt.close()