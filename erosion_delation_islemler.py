import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

new_binary_img=cv2.imread("./binary_1.png",0)
print(type(new_binary_img))
my_kernel=np.ones((5,5),dtype=np.uint8)
my_erosion_img=cv2.erode(new_binary_img,my_kernel,iterations=6)

my_delation_img=cv2.dilate(new_binary_img,my_kernel,iterations=6)

fig=plt.figure(figsize=(7,7))

plt.subplot(2,2,1)
plt.imshow(new_binary_img)
plt.axis("off")
plt.title("Orginal Img")

plt.subplot(2,2,2)
plt.imshow(my_erosion_img)
plt.axis("off")
plt.title("Erosion Img")

plt.subplot(2,2,3)
plt.imshow(my_delation_img)
plt.axis("off")
plt.title("Delation Img")
plt.show()

# ******************************* YENİ GÖRÜNTÜ İLE BEYAZ VE SİAY GÜRÜLTÜ
new_binary_img_1=cv2.imread("./binary_2.png",0)
new_binary_img_1.shape
my_white_noise=np.random.randint(0,2,size=new_binary_img_1.shape[:2])*255
my_noised_img=new_binary_img_1+my_white_noise

my_opening_img=cv2.morphologyEx(my_noised_img.astype(np.float32),cv2.MORPH_OPEN,my_kernel)

my_black_noise=np.random.randint(0,2,size=new_binary_img_1.shape[:2])*-255

my_noised_img_2 = my_black_noise + new_binary_img_1
my_black_noise[my_black_noise <= -245] = 0
my_closeing_img=cv2.morphologyEx(my_noised_img.astype(np.float32),cv2.MORPH_CLOSE,my_kernel)



fig=plt.figure(figsize=(8,6))
plt.subplot(3,3,1)
plt.imshow(new_binary_img_1,cmap="gray")
plt.title("Orginal Img")
plt.axis("off")

plt.subplot(3,3,2)
plt.imshow(my_white_noise,cmap="gray")
plt.title("White Img")
plt.axis("off")

plt.subplot(3,3,3)
plt.imshow(my_opening_img,cmap="gray")
plt.title("Opening Img")
plt.axis("off")

plt.subplot(3,3,4)
plt.imshow(my_black_noise,cmap="gray")
plt.title("Black Noise Img")
plt.axis("off")

plt.subplot(3,3,5)
plt.imshow(my_closeing_img,cmap="gray")
plt.title("Closing Img")
plt.axis("off")
plt.show()

# ************************** GRADIENT 
my_grandient_1=cv2.morphologyEx(new_binary_img,cv2.MORPH_GRADIENT,my_kernel)
my_grandient_2=cv2.morphologyEx(new_binary_img_1,cv2.MORPH_GRADIENT,my_kernel)
fig=plt.figure(figsize=(8,6))
plt.subplot(2,2,1)
plt.imshow(new_binary_img,cmap="gray")
plt.axis("off")
plt.title("Original-1 Image")

plt.subplot(2,2,2)
plt.imshow(my_grandient_1,cmap="gray")
plt.axis("off")
plt.title("Gradient-1 Image")

plt.subplot(2,2,3)
plt.imshow(new_binary_img_1,cmap="gray")
plt.axis("off")
plt.title("Original-2 Image")

plt.subplot(2,2,4)
plt.imshow(my_grandient_2,cmap="gray")
plt.axis("off")
plt.title("Gradient-2 Image")

plt.show()

# *************************************VE FLAG
flag_germany=np.zeros((225,500,3))
flag_germany[:75,:,:]=[0,0,0]
flag_germany[75:150,:,:]=[255,0,0]
flag_germany[150:,:,:]=[240,220,0]
plt.imshow(flag_germany)
plt.axis("off")
plt.title("Germany flag")
plt.show()