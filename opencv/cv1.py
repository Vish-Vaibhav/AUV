import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('im1.jpg')
assert img is not None, "file could not be read, check with os.path.exist()"


px = img[100,100]
print(px)

#accessing only blue pixel
blue = img[100,100,0]
print(blue)

#modify the pixel value
img[100,100] = [255,255,255]
print(img[100,100])

#accessing RED value
img.item(10,10,2)

#modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.shape)

print(img.size) #total number of pixel accessed by img.size

print(img.dtype) #image datatype

# plt.figure(figsize = (10,10))
# plt.imshow(img)
# plt.show()
#new_img = cv.cvtColor(img.cv.COLOR_BGR2RGB)

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

#splitting and merging image channel
b,g,r = cv.split(img)
img = cv.merge((b,g,r))



BLUE = [255,0,0]
img1 = cv.imread('im1.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
