import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

my_img = cv2.imread("./latte.jpg", 1)
print(type(my_img))

my_rgb_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)

# plt.imshow(my_rgb_img)
# plt.axis("off")
# plt.show()  # Bu satır eksikti, pencereyi açar

# görüntüleri çevirme : cv2.flip(görüntünüzü,parametre), yatay,dikey ve hem yatay hem dikey eksenlerde çevirebiliyorsun
# iki parametre alır , ilk olarak görüntünün kendisi, ikinci olarak  da 
# döndüreceğiniz eksen
# döndürme ekseni:0 = dikey eksen
# döndürme ekseni:1 = yatay eksen
# döndürme ekseni:-1 = hem yatay hem dikey eksen


# my_rgb_vertical_img = cv2.flip(my_rgb_img, 0)     # Dikey çevir
# my_rgb_horizontal_img = cv2.flip(my_rgb_img, 1)   # Yatay çevir
# my_rgb_both_img = cv2.flip(my_rgb_img, -1)        # Hem yatay hem dikey

# fig= plt.figure(figsize=(10,10))
# plt.subplot(2,2,1)
# plt.imshow(my_rgb_img)
# plt.title("orjinal")
# plt.axis("off")


# plt.subplot(2,2,2)
# plt.imshow(my_rgb_vertical_img)
# plt.title("vertical")
# plt.axis("off")


# plt.subplot(2,2,3)
# plt.imshow(my_rgb_horizontal_img)
# plt.title("hortizonal")
# plt.axis("off")


# plt.subplot(2,2,4)
# plt.imshow(my_rgb_both_img)
# plt.title("both")
# plt.axis("off")
# plt.show() 

# my_new_vertical_img= my_img[::-1,:,:]
# plt.imshow(my_new_vertical_img)

# # ters çeviriyor
# my_new_hortizonal_img=my_rgb_img[:,::-1,:]   

# plt.show()
# # hem dikey hem yatay ters çevir
# my_new_both_img= my_rgb_img[::-1,::-1,:]



# fig= plt.figure(figsize=(10,10))
# plt.subplot(2,2,1)
# plt.imshow(my_rgb_img)
# plt.title("orjinal")
# plt.axis("off")


# plt.subplot(2,2,2)
# plt.imshow(my_new_vertical_img)
# plt.title("vertical")
# plt.axis("off")


# plt.subplot(2,2,3)
# plt.imshow(my_new_hortizonal_img)
# plt.title("hortizonal")
# plt.axis("off")


# plt.subplot(2,2,4)
# plt.imshow(my_rgb_both_img)
# plt.title("both")
# plt.axis("off")
# plt.show() 

# sıfırdan kendi fonksiyonumuzu yazıyorum
# 1-) cv2.flip() fonskiyonu iki parametreli oldugu içinde tanımlarken iki parametre tanımlıyoruz
# 2-) ilk parametre, dönüştürülmek istenen orjinal görüntü(numpy.ndarray),ilk parametre tipi numpy.ndarray, 2. parametre tipi int

def my_flip(org_img,flip_number):
 
    if flip_number==0:
        org_img= org_img[::]
    elif flip_number==1:
        org_img=org_img[:,::-1,:]
    elif flip_number==-1:
        org_img=org_img[::-1,::-1,:]
    else:
        print("lütfen doğru bir parametre girin")
    return org_img


my_flip_0=my_flip(my_rgb_img,0)
my_flip_1=my_flip(my_rgb_img,1)
my_flip_2=my_flip(my_rgb_img,2)


fig= plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(my_rgb_img)
plt.title("orjinal")
plt.axis("off")


plt.subplot(2,2,2)
plt.imshow(my_flip_0)
plt.title("vertical")
plt.axis("off")


plt.subplot(2,2,3)
plt.imshow(my_flip_1)
plt.title("hortizonal")
plt.axis("off")


plt.subplot(2,2,4)
plt.imshow(my_rgb_img)
plt.title("both")
plt.axis("off")
plt.show() 


# elinizdeki görüntünün sağ en alt tarafını gösteren kısmı parçala. crop ile 

my_rgb_img.shape
bilgi_satir=int(my_rgb_img.shape[0]*0.75)
bilgi_sutun=int(my_rgb_img.shape[0]*0.75)

new_crop_1=my_rgb_img[bilgi_satir:,bilgi_sutun:,:]

plt.subplot(1,2,1)
plt.imshow(my_rgb_img)
plt.title("hortizonal")
plt.axis("off")


plt.subplot(1,2,2)
plt.imshow(new_crop_1)
plt.title("both")
plt.axis("off")
plt.show() 






# ! copilot ile olan çalışan kod
# if my_rgb_img is None:
#     print("Görüntü yüklenemedi.")
# else:
#     dikey = cv2.flip(my_rgb_img, 0)
#     yatay = cv2.flip(my_rgb_img, 1)
#     ikisi = cv2.flip(my_rgb_img, -1)

#     cv2.imshow("Orijinal", my_rgb_img)
#     cv2.imshow("Dikey Flip (0)", dikey)
#     cv2.imshow("Yatay Flip (1)", yatay)
#     cv2.imshow("Dikey + Yatay Flip (-1)", ikisi)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
