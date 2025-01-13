from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./queensland_rail_cover.jpg'))
print(repr(img))

imgplot = plt.imshow(img)

# Apply a color filter to highlight data
# Pick one channel for out data
lum_img = img[:,:,0]

# Choose color to luminate the image
plt.imshow(lum_img, cmap="hot")

# Examine a specific data range
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0, 175)
plt.show()