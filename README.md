# Implementation-of-filter
## Aim:
To implement filters for smoothing and sharpening the images in the spatial domain.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1
Import the required libraries.

### Step2
Convert the image from BGR to RGB.

### Step3
Apply the required filters for the image separately

### Step4
Plot the original and filtered image by using matplotlib.pyplot.

### Step5
End the program.

## Program:
### Developed By   : Gokkul M
### Register Number: 212223240039
</br>

### 1. Smoothing Filters

i) Using Averaging Filter
```Python
import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread(r"C:\Users\admin\Downloads\image1.jpeg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB) 

# Create an averaging kernel
kernel = np.ones((11, 11), np.float32) / 121  # 11x11 kernel for averaging

# Apply the averaging filter
image3 = cv2.filter2D(image2, -1, kernel)

# Display the original and filtered images
plt.figure(figsize=(10, 8))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")

# Averaging Filtered Image
plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Averaging Filter Applied")
plt.axis("off")

plt.show()

```
ii) Using Weighted Averaging Filter
```Python
import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread(r"C:\Users\admin\Downloads\image1.jpeg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# Define the kernel for a weighted average filter
kernel1 = np.ones((5, 5), np.float32) / 25
image3 = cv2.filter2D(image2, -1, kernel1)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(image3)
plt.title("Weighted Average Filter Image")
plt.axis("off")

plt.show()

```
iii) Using Gausian Filter
```Python
import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread(r"C:\Users\admin\Downloads\gray .jpg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
gaussian_blur = cv2.GaussianBlur(image2, (15, 15), 0)

plt.figure(figsize=(8,8))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gaussian_blur)
plt.title("Gaussian Blur")
plt.axis("off")

plt.show()
```

iv) Using Median Filter
```Python
import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread(r"C:\Users\admin\Downloads\gray .jpg")
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

median = cv2.medianBlur(image2, 5)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(image2)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(median)
plt.title("Median Blurred Image")
plt.axis("off")

plt.show()


```

### 2. Sharpening Filters
i) Using Laplacian Linear Kernal
```Python
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
```
ii) Using Laplacian Operator
```Python
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

```

## OUTPUT:
### 1. Smoothing Filters
</br>

i) Using Averaging Filter
![image](https://github.com/user-attachments/assets/061cc7ad-7889-43f7-85fa-ae3436d21dfa)

ii)Using Weighted Averaging Filter
![image](https://github.com/user-attachments/assets/5e3fa5f8-edcb-46a9-aab0-8e8e57860d61)

iii) Using Minimum Filter
![image](https://github.com/user-attachments/assets/05f29ff2-b315-47c3-b50b-dccfde443403)

iv) Using Median Filter
![image](https://github.com/user-attachments/assets/06340ce1-5324-4c06-97b5-e009d63d3ebd)

### 2. Sharpening Filters
</br>
i) Using Laplacian Kernal

![Screenshot 2024-09-26 154809](https://github.com/user-attachments/assets/d9c755d0-b814-41e8-9b6c-617cbdb0ef12)


ii) Using Laplacian Operator
![image](https://github.com/user-attachments/assets/aa119ec7-64fc-4647-87a2-a7694a641780)

## Result:
Thus the filters are designed for smoothing and sharpening the images in the spatial domain.
