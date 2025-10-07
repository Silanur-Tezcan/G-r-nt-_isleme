
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


img=cv2.imread("./latte.jpg")
img.shape

# my_rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# plt.title("orginal img")
# plt.axis("off")
# plt.imshow(my_rgb_img)
# plt.show()
# _,my_binary_tresh_img=cv2.threshold(my_rgb_img,thresh=125,maxval=255,type=cv2.THRESH_BINARY)
# _,my_binary_inv_img=cv2.threshold(my_rgb_img,thresh=125,maxval=255,type=cv2.THRESH_BINARY_INV)
# _,my_binary_trunc_img=cv2.threshold(my_rgb_img,thresh=125,maxval=255,type=cv2.THRESH_TRUNC)
# _,my_tozero_binary_img=cv2.threshold(my_rgb_img,thresh=125,maxval=255,type=cv2.THRESH_TOZERO)
# _,my_inv_tozero_img=cv2.threshold(my_rgb_img,thresh=125,maxval=255,type=cv2.THRESH_TOZERO_INV)
# fig=plt.figure(figsize=(8,5))

# plt.subplot(1,5,1)
# plt.title("Thresh img")
# plt.axis("off")
# plt.imshow(my_binary_tresh_img)

# plt.subplot(1,5,2)
# plt.title("Inverse img")
# plt.axis("off")
# plt.imshow(my_binary_inv_img)


# plt.subplot(1,5,3)
# plt.title("Trunc img")
# plt.axis("off")
# plt.imshow(my_binary_trunc_img)

# plt.subplot(1,5,4)
# plt.title("Tozero img")
# plt.axis("off")
# plt.imshow(my_tozero_binary_img)

# plt.subplot(1,5,5)
# plt.title("hem tozero hem ınverse   img")
# plt.axis("off")
# plt.imshow(my_inv_tozero_img)
# plt.show()
# **********************************************************************
my_gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,my_inv_binary_img=cv2.threshold(my_gray_img,thresh=125,maxval=255,type=cv2.THRESH_BINARY_INV)
_,my_thresh_binary_img=cv2.threshold(my_gray_img,thresh=125,maxval=255,type=cv2.THRESH_BINARY)
_,my_trunc_img=cv2.threshold(my_gray_img,thresh=125,maxval=255,type=cv2.THRESH_TRUNC)
_,my_tozero_img=cv2.threshold(my_gray_img,thresh=125,maxval=255,type=cv2.THRESH_TOZERO)
_,my_tozero_inv_img=cv2.threshold(my_gray_img,thresh=125,maxval=255,type=cv2.THRESH_TOZERO_INV)

fig=plt.figure(figsize=(10,8))

plt.subplot(1,6,1)
plt.title("orginal img")
plt.axis("off")
plt.imshow(my_gray_img,cmap="gray")

plt.subplot(1,6,2)
plt.title("ınverse img")
plt.axis("off")
plt.imshow(my_inv_binary_img,cmap="gray")

plt.subplot(1,6,3)
plt.title("thresh img")
plt.axis("off")
plt.imshow(my_thresh_binary_img,cmap="gray")

plt.subplot(1,6,4)
plt.title("trunc img")
plt.axis("off")
plt.imshow(my_trunc_img,cmap="gray")

plt.subplot(1,6,5)
plt.title("tozero img")
plt.axis("off")
plt.imshow(my_tozero_img,cmap="gray")

plt.subplot(1,6,6)
plt.title("ınverse ve tozero img")
plt.axis("off")
plt.imshow(my_tozero_inv_img,cmap="gray")
plt.show()