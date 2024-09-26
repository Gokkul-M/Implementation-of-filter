# Implementation-of-filter
## Aim:
To implement filters for smoothing and sharpening the images in the spatial domain.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1
</br>
</br> 

### Step2
</br>
</br> 

### Step3
</br>
</br> 

### Step4
</br>
</br> 

### Step5
</br>
</br> 

## Program:
### Developed By   :
### Register Number:
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





```
iii) Using Minimum Filter
```Python





```

iv) Using Maximum Filter
```Python





```

v) Using Median Filter
```Python





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
</br>
</br>
</br>
</br>
</br>

iv) Using Maximum Filter
</br>
</br>
</br>
</br>
</br>

v) Using Median Filter
</br>
</br>
</br>
</br>
</br>

### 2. Sharpening Filters
</br>
i) Using Laplacian Kernal

![Screenshot 2024-09-26 154809](https://github.com/user-attachments/assets/d9c755d0-b814-41e8-9b6c-617cbdb0ef12)


ii) Using Laplacian Operator
![image](https://github.com/user-attachments/assets/aa119ec7-64fc-4647-87a2-a7694a641780)

## Result:
Thus the filters are designed for smoothing and sharpening the images in the spatial domain.
