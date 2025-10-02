
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')


my_img=cv2.imread("./latte.jpg")
print(type(my_img))
my_img.shape

my_gray_img=cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
plt.imshow(my_gray_img,cmap="gray")
plt.title("gri rengine çevirme")
plt.axis("off")
plt.show()
# binary thresh: ikili eşikleme, veriilen thres(eşik)  degeri baz alınarak
# bu eşik değerinini altında kalan piksel değerleri yani örneğin 123'ten küçük
# piksel degerleri siyah rengini alacak(0), buyuk veya eşit olanlar ise
# beyaz rengini (255) alacak

# ? TRESH BINARY
_, my_binary_tresh_img= cv2.threshold(my_gray_img,thresh=125, maxval=255, type=cv2.THRESH_BINARY)

fig=plt.figure(figsize=(10,7))

plt.subplot(1,2,1)
plt.imshow(my_gray_img,cmap="gray")
plt.axis("off")
plt.title("orginal gray ımage")

plt.subplot(1,2,2)
plt.imshow(my_binary_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary tresh ımage")
plt.show()

my_gray_img[100,100]
my_binary_tresh_img[100,100]
# 125den küçükse siyah olur ve 0 sayısı verir
# 125den büyükse beyaz olur sayı olarak 255 verir
# uint8=işaretsiz demek u bunu ifade ediyor
# inv=eşik değerinden eşit olanlar ve kucuk olanlar 255 büyük olan 0
# tam tersi yapıyor

# ? İNVERSE BINARY
_, my_binary_inv_tresh_img= cv2.threshold(my_gray_img,thresh=125,
 maxval=255, type=cv2.THRESH_BINARY_INV)

fig=plt.figure(figsize=(10,7))

plt.subplot(1,3,1)
plt.imshow(my_gray_img,cmap="gray")
plt.axis("off")
plt.title("orginal gray ımage")

plt.subplot(1,3,2)
plt.imshow(my_binary_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary tresh ımage")

plt.subplot(1,3,3)
plt.imshow(my_binary_inv_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary inverse tresh ımage")
plt.show()


# print(f"orginal={my_gray_img[500,850]}")
# print(f"tresh={my_binary_tresh_img[500,850]}")
# print(f"ınv_tresh={my_binary_inv_tresh_img[500,850]}")

# # ? TRUNC
_, my_trunc_tresh_img= cv2.threshold(my_gray_img,thresh=125,
 maxval=255, type=cv2.THRESH_TRUNC)

fig=plt.figure(figsize=(10,7))

plt.subplot(1,4,1)
plt.imshow(my_gray_img,cmap="gray")
plt.axis("off")
plt.title("orginal gray ımage")

plt.subplot(1,4,2)
plt.imshow(my_binary_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary tresh ımage")

plt.subplot(1,4,3)
plt.imshow(my_binary_inv_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary inverse tresh ımage")

plt.subplot(1,4,4)
plt.imshow(my_trunc_tresh_img,cmap="gray")
plt.axis("off")
plt.title("turnc tresh ımage")
plt.show()

# #! binary thresholding= belirlenen eşik degerine göre(thresh value)
# # orjinal görüntünün pikseli, bu eşik degerinden küçükse siyah rengine
# # dönüştürülür yani 0 degerini alır, ilgli piksel eşik degerinden büyükse
# # beyaz rengine dönüştürülür yani 255 degerini alır

# #! binary ınverse8binary_inv thresholding= binary thresholding in tam tersidir
# # ilgili pikseli, eşik değerinden küçükse 255 degerini alır(beyaz rengine)
# # ,eşik 
# # ! TOZERO THRESHOLDİNG: eğer ilgili piksel eşik değerinden buyukse oldugu gibi korunur yani değişmez
# # yok eger piksel değeridnen buuykse 0 yapılır yani siyah rengine dönüşür.
# # eger küçükse 

# # ? TOZERO
_, my_tozero_tresh_img= cv2.threshold(my_gray_img,thresh=125,
 maxval=255, type=cv2.THRESH_TOZERO)

fig=plt.figure(figsize=(10,7))

plt.subplot(1,5,1)
plt.imshow(my_gray_img,cmap="gray")
plt.axis("off")
plt.title("orginal gray ımage")

plt.subplot(1,5,2)
plt.imshow(my_binary_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary tresh ımage")

plt.subplot(1,5,3)
plt.imshow(my_binary_inv_tresh_img,cmap="gray")
plt.axis("off")
plt.title("bınary inverse tresh ımage")

plt.subplot(1,5,4)
plt.imshow(my_trunc_tresh_img,cmap="gray")
plt.axis("off")
plt.title("turnc tresh ımage")

plt.subplot(1,5,5)
plt.imshow(my_tozero_tresh_img,cmap="gray")
plt.axis("off")
plt.title("tozero tresh ımage")
plt.show()


_, my_tozero_inv_tresh_img= cv2.threshold(my_gray_img,thresh=125,
 maxval=255, type=cv2.THRESH_TOZERO_INV)

fig=plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(my_gray_img,cmap="gray")
plt.axis("off")
plt.title("orginal gray ımage")

plt.subplot(1,2,2)
plt.imshow(my_tozero_inv_tresh_img,cmap="gray")
plt.axis("off")
plt.title("TOZERO INV ımage")

plt.tight_layout()
plt.savefig("./thresholding Types.png",dpi=300)
plt.show()
#? GÖRÜNTÜDE 

#  pythondan 2 adet cv2:resize() fonskisyonu yazınız.
#  bu fonksiyonlar 1 adet parametre alacak. o da görüntünün kendisi olacak.
# görüntüyü büyütürken de küçültürken de genişlik ve yüksekliğinin
# %25'i kadra olacaktır. Her iki fonksiyon da geriye, işlenmiş görüntünün
# kendisini döndürecektir.

# cv2.resize() kullanımı

def img_zoom(orginal_img):
    # görüntünün satırının yüksekliğinin %25 ini hesapladık
    new_height= orginal_img.shape[0]+int(orginal_img.shape[0]*0.25)
    new_weight=orginal_img.shape[1]+int(orginal_img.shape[1]*0.25)

    new_img=cv2.resize(orginal_img,(new_height,new_weight),cv2.INTER_LANCZOS4)
    return new_img

def img_out(orginal_img):
    # görüntünün satırının yüksekliğinin %25 ini hesapladık
    new_height= orginal_img.shape[0]-int(orginal_img.shape[0]*0.75)
    new_weight=orginal_img.shape[1]-int(orginal_img.shape[1]*0.75)

    new_img1=cv2.resize(orginal_img,(new_height,new_weight),cv2.INTER_LANCZOS4)
    return new_img1
my_rgb_img=cv2.cvtColor(my_img,cv2.COLOR_BGR2RGB)

img_new=img_zoom(my_rgb_img)
out_img_new=img_out(my_rgb_img)
fig= plt.figure(figsize=(5,4))


print(f"orjinal görüntü= {my_rgb_img.shape[:2]}")
print(f"büyütülmüş görüntü= {img_new.shape[:2]}")
print(f"küçük görüntü= {out_img_new.shape[:2]}")

fig=plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.imshow(my_rgb_img)
plt.axis("off")
plt.title("orginal ")

plt.subplot(1,3,2)
plt.imshow(img_new,cmap="gray")
plt.axis("off")
plt.title("büyük ımage")

plt.subplot(1,3,3)
plt.imshow(out_img_new,cmap="gray")
plt.axis("off")
plt.title("küçük ımage")

plt.tight_layout()
plt.savefig("./buyuk_kucuk Types.png",dpi=300)
plt.show()
