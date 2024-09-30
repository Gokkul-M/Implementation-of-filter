###Sharpening Filters
# In[4]: Using Laplacian Kernal


import cv2
import matplotlib.pyplot as plt
import numpy as np
image1 = cv2.imread(r"C:\Users\admin\Downloads\image1.jpeg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB) 
kernel = np.ones((11, 11), np.float32) / 121 
blurred_image = cv2.filter2D(image2, -1, kernel)
kernel2 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
sharpened_image = cv2.filter2D(image2, -1, kernel2) 
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(sharpened_image)
plt.title("Sharpened Image")
plt.axis("off")
plt.show()


# In[5]:Using Laplacian Operator

import cv2
import matplotlib.pyplot as plt
import numpy as np
image1 = cv2.imread(r"C:\Users\admin\Downloads\image1.jpeg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB) 
laplacian = cv2.Laplacian(image2, cv2.CV_64F)
plt.figure(figsize=(8,8))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title("Laplacian Image")
plt.axis("off")
plt.show()






