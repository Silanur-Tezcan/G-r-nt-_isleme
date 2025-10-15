
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

# # istediğimiz boyutlarda rastgele degerlerden oluşan bir matris tanımlayalım
# my_arr_1 = np.random.randint(0, 101, size=(5,5), dtype=np.uint8)
# print(my_arr_1)
# print(my_arr_1.shape)

# # boyut olarak sadece (()) şeklinde olur
height,width,channel=150,210,3
# my_black_img=np.zeros((height,width,channel),dtype=np.uint8)

# my_white_img=np.ones((height,width,channel),dtype=np.uint8)*255
# # iki farklı yooldan gri oluşturma
# # iki farklı yooldan gri oluşturma
# my_gray_img1 = np.random.randint(127, 128, size=(height, width, channel), dtype=np.uint8)
# my_gray_img2=np.ones((height,width,channel),dtype=np.uint8)*127

# fig=plt.figure(figsize=(10,7),facecolor="pink")

# plt.subplot(2,2,1)
# plt.imshow(my_black_img)
# plt.axis("off")
# plt.title("black ımage")

# plt.subplot(2,2,2)
# plt.imshow(my_white_img)
# plt.axis("off")
# plt.title("white ımage")

# plt.subplot(2,2,3)
# plt.imshow(my_gray_img1)
# plt.axis("off")
# plt.title("gray 1 ımage")

# plt.subplot(2,2,4)
# plt.imshow(my_gray_img2)
# plt.axis("off")
# plt.title("gray 2 ımage")
# plt.show()

# #  3 kanallı bir görüntüde kırmızı rengini [255,0,0]
# # bu şu anlama gelir red=255 green=0 blue=0 
# # yeşil rengi kodları [0,255,0]
# # mavi rengi kodları [0,0,255]

# #  red, green , blue renklerini oluşturup tek flap

# my_red_img=np.zeros((height,width,channel),dtype=np.uint8)
# my_red_img[:,:,0]=255

# my_green_img=np.zeros((height,width,channel),dtype=np.uint8)
# my_green_img[:,:,1]=255

# my_blue_img=np.zeros((height,width,channel),dtype=np.uint8)
# my_blue_img[:,:,2]=255

# fig=plt.figure(figsize=(10,7),facecolor="pink")


# plt.subplot(1,3,1)
# plt.imshow(my_red_img)
# plt.axis("off")
# plt.title("red ımage")

# plt.subplot(1,3,2)
# plt.imshow(my_green_img)
# plt.axis("off")
# plt.title("green ımage")

# plt.subplot(1,3,3)
# plt.imshow(my_blue_img)
# plt.axis("off")
# plt.title("blue ımage")
# plt.show()

# my_new_black_img=my_red_img*my_green_img*my_blue_img
# my_new_white_img=my_red_img+my_green_img+my_blue_img
# my_new_color=(my_red_img-my_green_img-my_blue_img)*255
# fig=plt.figure(figsize=(10,7),facecolor="pink")


# plt.subplot(1,3,1)
# plt.imshow(my_new_white_img)
# plt.axis("off")
# plt.title("birleşimden çıkan beyaz ımage")

# plt.subplot(1,3,2)
# plt.imshow(my_new_black_img)
# plt.axis("off")
# plt.title("çarpımından çıkan siyah ımage")

# plt.subplot(2,3,3)
# plt.imshow(my_new_color)
# plt.axis("off")
# plt.title("renklerin çıkılması ve 255 ile çarpılması  ımage")

# plt.show()

# # tanımlanan my_blue my_red my_green renkleri ile sarı ve mor renkleri elde et
# my_new_pruple_img=(my_red_img+my_blue_img)*195
# my_new_yellow_img=my_red_img+my_green_img

# fig=plt.figure(figsize=(10,7),facecolor="pink")


# plt.subplot(1,3,1)
# plt.imshow(my_new_pruple_img)
# plt.axis("off")
# plt.title("purple ımage")

# plt.subplot(1,3,2)
# plt.imshow(my_new_yellow_img)
# plt.axis("off")
# plt.title("yellow ımage")
# plt.show()

# fenerbahçe renklerini çiziniz
# fb_img=np.zeros((height,width,channel),dtype=np.uint8)
# fb_img[:, :fb_img.shape[1]//2, :] = [255, 255, 0]  # Üst yarı kırmızı
# fb_img[:, fb_img.shape[1]//2:,  :] = [0,0,255] 

# fig=plt.figure(figsize=(10,7),facecolor="pink")
# eğer bir resmi eşit şekilde parçalayıp farklı renklere 
# boyamak istiyorsanız satır veya sutun 

# plt.subplot(1,1,1)
# plt.imshow(fb_img)
# plt.axis("off")
# plt.title("fenerbahçe ımage")
# plt.show()
# color detectıon(renk tespit etme): bu işlem için görüntünün tüm
# satır ve sutununda veya istediğimiz ya da tüm
# kanallarında gezmek durumundayız

# örneğin fenerbahçe renklerine gb renklerine dönüştürmek için
#  önce fb bayragında ki mavi rengi tespit etmemiz lazım sonra bunun kordinat sistemini
#  çıkarmamız lazım daha sonra bu kordinat sistemini  tekrar bir bütün indeks olarak kullanıp
# bunun değerini kırmızı rengi olarak atamamız lazım

# ilk olarak fb amblemindeki mavi rengi tespit edioyurz
# mavi rengi kodları=[0,0,255]
# yani görüntünün kanalındaki . . indeksinin degeri =0
#  görüntünün kanalındaki 1. indeksi=0
# görüntünün kanalındaki 2. indeksi=255

# koordinat_mavi=(fb_img[:,:,0]==0)&(fb_img[:,:,1]==0) & (fb_img[:,:,2]==255)

# mavi renginin kordinatlarını tekrar fb amblemine yerleştiriyoruz
# bu defa artık karşıma artık kordinat değil o kordinat daki renkler geliyor
# bu aşamadan sonra ise mavi rengi değil red renk kodlarını yazıyoruz [255,0,0]

# fb_img[koordinat_mavi]=[255,0,0]
# plt.subplot(1,1,1)
# plt.imshow(fb_img)
# plt.axis("off")
# plt.title(" değiştirilmiş takım")
# plt.show()

#  gs bayrağının amblemindeki sarı rangini beyaza,
# kırmızı rengi de siyaha dönüştürün
#  bu defa 2 rengi tespit edip ikisini değiştirin

# koordinat_sari=(fb_img[:,:,0]==255)&(fb_img[:,:,1]==255) & (fb_img[:,:,2]==0)
# fb_img[koordinat_sari]=[255,255,255]

# koordinat_kirmizi=(fb_img[:,:,0]==255)&(fb_img[:,:,1]==0) & (fb_img[:,:,2]==0)
# fb_img[koordinat_kirmizi]=[0,0,0]

# fig=plt.figure(figsize=(10,7),facecolor="pink")
# plt.subplot(1,1,1)
# plt.imshow(fb_img)
# plt.axis("off")
# plt.title(" değiştirilmiş takım")
# plt.show()

my_img = cv2.imread('./fallani.jpg')  
type(my_img)
my_rgb_img=cv2.cvtColor(my_img,cv2.COLOR_BGR2RGB)
my_rgb_img2=cv2.cvtColor(my_img,cv2.COLOR_BGR2RGB)



koordinat_siyah=(my_rgb_img[:,:,0]<50)&(my_rgb_img[:,:,1]<50)&(my_rgb_img[:,:,2]<50)
my_rgb_img[koordinat_siyah]=[0,255,255]
plt.imshow(my_rgb_img)
plt.axis("off")
plt.show()
# ilk okudugunuz bgr kanal sıralamasına sahip değişkeni rgb ye dönüştürerek
# başka bir değişkene aktarın
# sonra bu görüntüdeki rengi mavi 
koordinat_kirmizi=(my_rgb_img2[:,:,0]>135)&(my_rgb_img2[:,:,1]<80)&(my_rgb_img2[:,:,2]<80)
my_rgb_img2[koordinat_kirmizi]=[0,0,255]
plt.imshow(my_rgb_img2)
plt.axis("off")
plt.show()