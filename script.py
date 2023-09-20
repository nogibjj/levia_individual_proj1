import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import lib


data=lib.read_csv("playlist.csv")

print("Descriptive statistics using Polars")
lib.calculate_statistics(data)

lib.visualize_data(data,"./plots")

image_path = './plots/energy_histogram.png'

img = mpimg.imread(image_path)
plt.imshow(img)
plt.axis('off')  # Optionally, turn off axis labels and ticks
plt.show()


