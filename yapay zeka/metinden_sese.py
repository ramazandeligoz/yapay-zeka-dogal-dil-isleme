import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from gtts import gTTS
import os
from os import path

window = tk.Tk()
window.geometry("1080x640")
window.wm_title("Metinden Sese Çevirme Uygulaması")

count = 0

## frames
frame_left = tk.Frame(window, width = 540, height = 640, bd = "2")
frame_left.grid(row = 0, column = 0)



frame2 = tk.LabelFrame(frame_left, text = "Seslendirilen Dosya Konumu ", width = 140, height = 140)
frame2.grid(row = 1, column = 0)

frame3 = tk.LabelFrame(frame_left, text = "Durum", width = 170, height = 240)
frame3.grid(row = 0, column = 0)



count = 0

   
def openDosya():
    global count
    global dosya_name
    
    
    count += 1
    if count != 1:
        messagebox.showinfo(title = "Warning", message = "Aynı anda yalnızca bir metin seslendirilebilir.")
    else:
        dosya_name = filedialog.askopenfilename(initialdir = "D:\codes",title = "metin dosyasını seçin")
        masaladi = dosya_name.split("/")[-1].split(".")[0]
        tk.Label(frame2, text =masaladi, bd = 3 ).pack(pady = 10)
        dosya = open(f"{masaladi}.txt", encoding="utf-8")
        yazi = dosya.read()
        cikti = gTTS(text=yazi, lang='tr',slow=False)
        if path.exists(f"{masaladi}.mp3"):
            print("Seslendiriliyor...")
            tk.Label(frame3, text ="Seslendiriliyor...", bd = 3 ).pack(pady = 10)
            os.system(f"{masaladi}.mp3")
        else:
            print("Dosyanız oluşturuluyor")
            tk.Label(frame3, text ="Dosyanız oluşturuluyor", bd = 3 ).pack(pady = 10)
            cikti.save(f"{masaladi}.mp3")
            print("Seslendiriliyor...")
            tk.Label(frame2, text ="Seslendiriliyor...", bd = 3 ).pack(pady = 10)
            os.system(f"{masaladi}.mp3")
    
            
# Bu kısımda bir menubar oluşturuyoruz
menubar = tk.Menu(window)
window.config(menu = menubar)

# bu menubar'a file ve edit kısımlarını ekliyoruz
file = tk.Menu(menubar)

menubar.add_cascade(label = "file", menu = file)

# file ve edit kısımlarının içine sırasıyle new file ve edit kısımlarını koyuyoruz
file.add_command(label = "open", command = openDosya )


window.mainloop()
