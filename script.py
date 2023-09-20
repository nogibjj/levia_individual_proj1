# %%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import lib




# %% [markdown]
# Note1: import libraries

# %%
data=lib.read_csv("playlist.csv")

# %% [markdown]
# Note2: call the function named read_csv in the lib.py to read csv file. Save the csv file into data variables

# %%
print("Descriptive statistics using Polars")
lib.calculate_statistics(data)

# %% [markdown]
# Note3: call the statistic function to make a descriptive statistics.

# %%
lib.visualize_data(data,"./plots")

# %% [markdown]
# Note3: use the visualize function in the lib to visualize data.
# Visulization function will automatically save pictures into "./plots" directory.
# We should open a picture file to show it.

# %%
# Specify the image path
image_path = './plots/energy_histogram.png'

# Display the image
img = mpimg.imread(image_path)
plt.imshow(img)
plt.axis('off')  # Optionally, turn off axis labels and ticks
plt.show()


