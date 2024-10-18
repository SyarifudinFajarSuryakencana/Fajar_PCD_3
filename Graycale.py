from imageio import imread
import numpy as np
import matplotlib.pyplot as plt


img_path = "C:\\pemandangan.jpg"
image = imread(img_path)


gray_image = np.dot(image[...,:3], [0.2989, 0.587, 0.114]).astype(np.uint8)


histogram, bin_edges = np.histogram(gray_image, bins=256, range=(0, 255))


plt.figure(figsize=(10, 6))
plt.plot(bin_edges[:-1], histogram, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig('grayscale_histogram_screenshot.png')  # Save the screenshot
plt.show()
