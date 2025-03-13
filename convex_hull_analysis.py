import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import cv2

# Given fielder positions (x, y coordinates)
fielders = np.array([
    [307, 564], [246, 324], [58, 338], 
    [303, 51], [187, 97], [502, 148], 
    [554, 346], [519, 446]
])

# Load cricket field background image
field_image_path = "fielders.png"  # ✅ Update with your correct image file
field_img = cv2.imread(field_image_path)

# Convert from BGR to RGB (Matplotlib uses RGB format)
if field_img is not None:
    field_img = cv2.cvtColor(field_img, cv2.COLOR_BGR2RGB)
else:
    print("⚠️ Error: Image 'fielders.png' not found!")

# Compute Convex Hull
hull = ConvexHull(fielders)

# Plot the field with the image as background
fig, ax = plt.subplots(figsize=(6,6))
ax.set_title("Convex Hull of Fielders")

# Display cricket field image
if field_img is not None:
    ax.imshow(field_img, extent=[0, 600, 600, 0])  # ✅ Adjust extent based on image size

# Plot fielder positions
plt.scatter(fielders[:, 0], fielders[:, 1], color='blue', s=50, label="Fielders")

# Draw Convex Hull boundary
for simplex in hull.simplices:
    plt.plot(fielders[simplex, 0], fielders[simplex, 1], 'r-', linewidth=2)

# Labels and Legends
plt.legend()
plt.xlabel("X Position")
plt.ylabel("Y Position")

# Show the plot
plt.show()



