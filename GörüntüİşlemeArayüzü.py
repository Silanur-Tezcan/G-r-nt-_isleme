import matplotlib
matplotlib.use('TKAgg')  # Bu satır önce gelmeli

import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

def resize_to_fit(img, max_width=800, max_height=600):
    h, w = img.shape[:2]
    scale = min(max_width / w, max_height / h)
    new_size = (int(w * scale), int(h * scale))
    return cv2.resize(img, new_size)

def load_image():
    global img, tk_img
    file_path = filedialog.askopenfilename(
        title="Görsel Seç",
        filetypes=[("Görsel Dosyaları", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    print("Seçilen dosya:", file_path)
    if file_path:
        try:
            pil_img = Image.open(file_path)
            img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            show_image(img)
        except Exception as e:
            print("Görsel yüklenemedi:", e)

def show_image(img):
    global tk_img
    img_resized = resize_to_fit(img)
    rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(rgb)
    tk_img = ImageTk.PhotoImage(im_pil)

    canvas_width = im_pil.width
    canvas_height = im_pil.height
    canvas.config(width=canvas_width, height=canvas_height)
    canvas.delete("all")
    canvas.create_image(canvas_width // 2, canvas_height // 2, anchor="center", image=tk_img)
def vertical():
    vertical=cv2.flip(img,0)
    show_image(vertical)
def horizontal():
    horizontal=cv2.flip(img,1)
    show_image(horizontal)
def convert_to_gray():
    global img
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

def crop_image():
    global img
    if img is not None:
      img.shape
      bilgi_satir=int(img.shape[0]*0.75)
      bilgi_sutun=int(img.shape[0]*0.75)

      new_crop_1=img[bilgi_satir:,bilgi_sutun:,:]
      show_image(new_crop_1)

def save_image():
    global img
    if img is not None:
        resized = cv2.resize(img, (300, 300))  # örnek boyut
        cv2.imwrite("kaydedilen.jpg", resized)
        print("Görsel kaydedildi: kaydedilen.jpg")

root = tk.Tk()
root.title("Görüntü İşleme Arayüzü")

canvas = tk.Canvas(root, bg="white")
canvas.pack()


button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(button_frame, text="Görseli Yükle", command=load_image).pack(side="left", padx=5)
tk.Button(button_frame, text="Griye Çevir", command=convert_to_gray).pack(side="left", padx=5)
tk.Button(button_frame, text="%25 Kırp", command=crop_image).pack(side="left", padx=5)
tk.Button(button_frame, text="Dikey Çevir", command=vertical).pack(side="left", padx=5)
tk.Button(button_frame, text="Yatay Çevir", command=horizontal).pack(side="left", padx=5)
tk.Button(button_frame, text="Kaydet", command=save_image).pack(side="left", padx=5)



root.mainloop()