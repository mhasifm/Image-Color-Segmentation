import cv2
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt  # Import matplotlib

# Upload the image
uploaded = files.upload()
image_path = list(uploaded.keys())[0] 

# Read and display the image
img = cv2.imread(image_path)  # Load image here
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for displaying with matplotlib
plt.imshow(img)
plt.title("Original Image")
plt.show()

# Example color ranges (adjust these based on your image)
wall_color_lower = np.array([100, 100, 100])  # Lower bound for wall color (RGB)
wall_color_upper = np.array([200, 200, 200])  # Upper bound for wall color (RGB)

floor_color_lower = np.array([50, 50, 50])  # Lower bound for floor color (RGB)
floor_color_upper = np.array([100, 100, 100])  # Upper bound for floor color (RGB)

wall_mask = cv2.inRange(img, wall_color_lower, wall_color_upper)
floor_mask = cv2.inRange(img, floor_color_lower, floor_color_upper)  # Removed the extra spaces before this line

img[wall_mask > 0] = [255, 0, 0]  # Change wall color to red (RGB)
img[floor_mask > 0] = [0, 255, 0]  # Change floor color to green (RGB)

plt.imshow(img)
plt.title("Modified Image")
plt.show()

cv2.imwrite("modified_image.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))  # Save image

files.download('modified_image.jpg')  # Replace with the actual filename
