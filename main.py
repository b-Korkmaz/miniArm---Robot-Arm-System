import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import datetime
from time import sleep
import RPi.GPIO as GPIO

say = 0
kutu = 0

toplam_say = 0

def nothing(x):
    # any operation
    pass

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(38, GPIO.IN)

pwm = GPIO.PWM(11,50)
pwm.start(0)


pwm2 = GPIO.PWM(13,50)
pwm2.start(0)

pwm3 = GPIO.PWM(40,50)
pwm3.start(0)

pwm4 = GPIO.PWM(15,50)
pwm4.start(0)
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX

pencere = tk.Tk()

# Alan
entry = tk.Entry(state='disabled', bd=5, disabledbackground="white", disabledforeground="black", width=27, font="bold")
entry.place(x=10, y=290)

# Alan
entry2 = tk.Entry(state='disabled', bd=5, disabledbackground="white", disabledforeground="black", width=27, font="bold")
entry2.place(x=10, y=225)

# Alan
entry3 = tk.Entry(state='disabled', bd=5, disabledbackground="white", disabledforeground="black", width=27, font="bold")
entry3.place(x=10, y=355)



def kamera():
    while 1:

        _, frame = cap.read()
        cv2.imshow("Kamera", frame)

        key = cv2.waitKey(1)
        if key == ord("s"):
            cv2.imwrite(
                "/home/pi/robotDinamigiProV2/image1.png",
                frame)

            
            cv2.destroyAllWindows()
            break
        elif key == ord("e"):
            cv2.destroyAllWindows()
            break


######################################################

def sistem():
    global say
    global toplam_say
    global kutu    
    while 1:        
        sensor = GPIO.input(38)
        print("Malzeme Yok...")
        print("Sayilan malzeme ",say )
        sleep(3)
        
        
        
        
        if(say == 3):
            
            entry3['state']='normal'
            entry3.delete(0,tk.END)
            entry3['state']='disabled'
            
            kutu = kutu + 1
            toplam_say = kutu * 3
            entry['state']='normal'                                                
            entry.insert(0,kutu)
            entry['state']='disabled' 
            
            entry2['state']='normal'                                                
            entry2.insert(0,say)
            entry2['state']='disabled'         
            
            
            
            entry3['state']='normal'                                                
            entry3.insert(0,toplam_say)
            entry3['state']='disabled'
            
            b3['state']='disabled'
            b7['state']='normal' 
            
            break
        
        elif (sensor == 0):
            print("Malzeme Geldi...")
            print("Motorlar Çalıştırılıyor...")
            
            sleep(4)
            
            if (sensor == 0):
                while True:
                
                    sleep(4)
                    

                    pwm2.ChangeDutyCycle(6)
                    pwm2.ChangeDutyCycle(0)

                    pwm4.ChangeDutyCycle(4)
                    sleep(2)
                    pwm4.ChangeDutyCycle(0)

                    pwm.ChangeDutyCycle(8)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)

                    i = 0.5

                    ################################

                    pwm3.ChangeDutyCycle(12)
                    sleep(2)
                    pwm3.ChangeDutyCycle(0)


                    #################################

                    pwm.ChangeDutyCycle(11)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)


                    pwm2.ChangeDutyCycle(4)
                    sleep(2)
                    pwm2.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(11)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(10)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(9)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(8.7)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(8)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)                 
                   
                    
                    
                    
                    """
                    pwm3.ChangeDutyCycle(8)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    
                    pwm3.ChangeDutyCycle(7)
                    sleep(3)
                    pwm3.ChangeDutyCycle(0)
                    """
                    """
                    for i in range ():

                        pwm3.ChangeDutyCycle(12-i)
                        sleep(2)
                        pwm3.ChangeDutyCycle(0)


                    
                    """
                    """
                    pwm4.ChangeDutyCycle(7)
                    sleep(2)
                    pwm4.ChangeDutyCycle(0)

                    pwm2.ChangeDutyCycle(15)
                    sleep(2)
                    pwm2.ChangeDutyCycle(0)
                    """

                    pwm2.ChangeDutyCycle(6)
                    sleep(2)
                    pwm2.ChangeDutyCycle(0)

                    pwm4.ChangeDutyCycle(4)
                    sleep(2)
                    pwm4.ChangeDutyCycle(0)





                    #################################

                    """
                    #Mavi
                    pwm.ChangeDutyCycle(2)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)
                    """

                    """
                    #Yeşil
                    pwm.ChangeDutyCycle(5)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)
                    """
                    """
                    #Pembe
                    pwm.ChangeDutyCycle(8)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)
                    """
                    #Yeşil
                    pwm.ChangeDutyCycle(6.2)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)

                    pwm4.ChangeDutyCycle(8)
                    sleep(2)
                    pwm4.ChangeDutyCycle(0)

                    pwm3.ChangeDutyCycle(12)
                    sleep(2)
                    pwm3.ChangeDutyCycle(0)

                    pwm2.ChangeDutyCycle(6)
                    pwm2.ChangeDutyCycle(0)

                    pwm4.ChangeDutyCycle(4)
                    sleep(2)
                    pwm4.ChangeDutyCycle(0)

                    pwm.ChangeDutyCycle(8)
                    sleep(2)
                    pwm.ChangeDutyCycle(0)
                    
                    say = say + 1               
                    
                    
                    break

            
            else:
                break
        


def temizle():
    temizle_cevap=messagebox.askyesno("Temizleme","Bütün Verileri Temizlemek İstediğinizden\n Eminmisiniz ?")
    if temizle_cevap==1:
        entry['state']='normal'
        entry.delete(0,tk.END)
        entry['state']='disabled'
    
        entry2['state']='normal'
        entry2.delete(0,tk.END)
        entry2['state']='disabled'
        
        b3['state']='normal'
        b7['state']='disabled' 
        
        global say
        say = 0
        
       
    else:
        pass

######################################################

def veri_kaydet():
    
    v1=entry.get()
    v2=entry2.get()
    v3=entry3.get()   
    s2=str(datetime.datetime.now())
    
    
    dosya_2 = open("bilgiler.txt", "a", encoding="utf-8")
    dosya_2.write(s2)
    dosya_2.write("\n")
    dosya_2.write("________________________________\n")
    dosya_2.write("--------------------------------")
    dosya_2.write("\n") 
    dosya_2.write("Sayılan Malzeme : "+v2+"\nToplam Kutu Sayısı : "+v1+"\n")
    dosya_2.write("Toplam Malzeme Sayısı : "+ v3 +"\n")
    dosya_2.write("\n")
    
    dosya_2.write("--------------------------------")
    dosya_2.write("\n")
    dosya_2.write("________________________________")
    dosya_2.write("\n")   
    
    
    
    
    dosya_2.close()
    messagebox.showinfo("Kayıt","BİLGİLER KAYIT EDİLDİ")
    
def sistemi_kapat():
    cevap=messagebox.askyesno("Çıkış","Programı Kapatmak İstediğinizden\n Eminmisiniz ?")
    if cevap==1:
        exit()
    else:
        pass


    
pencere.title("miniARM -Anasayfa")
pencere.geometry("400x500+0+0")

baslik = tk.Label(text="mini-ARM", font="Verdana 22 bold", bg="white")
baslik.place(x=10, y=10)

b1 = tk.Button(text="Kamerayı Çalıştır", bg="white", command=kamera)
b1.place(x=10, y=55)

kam_yazi = tk.Label(text="Görüntüyü Kaydetmek için\n Klavyeden 'S' Tuşuna Basınız", font="Verdana 10 bold", bg="white")
kam_yazi.place(x=155, y=100)

kam_yazi2 = tk.Label(text="Kamerayı Kapatmak için\n 'E' Tuşuna Basınız", font="Verdana 10 bold", bg="white")
kam_yazi2.place(x=155, y=55)

sayilan_kutu_yazi = tk.Label(text="Toplam Kutu Sayısı", font="Verdana 10 bold", bg="white")
sayilan_kutu_yazi.place(x=10, y=265)

sayilan_malzeme_yazi = tk.Label(text="Sayılan Malzeme", font="Verdana 10 bold", bg="white")
sayilan_malzeme_yazi.place(x=10, y=200)

sayilan_top_malzeme_yazi = tk.Label(text="Toplam Sayılan Malzeme Sayısı", font="Verdana 10 bold", bg="white")
sayilan_top_malzeme_yazi.place(x=10, y=330)



b3 = tk.Button(text="Otomatik Mod", bg="white", state='normal',command = sistem)
b3.place(x=10, y=150)

b5 = tk.Button(text="Programı Kapat", command = sistemi_kapat)
b5.place(x=260, y=460)

b6 = tk.Button(text="Temizle",command = temizle)
b6.place(x=230, y=420)

b7 = tk.Button(text="Kaydet", state='disabled', command = veri_kaydet)
b7.place(x=315, y=420)


#sekil_alani = tk.Label(text=("ALANI               "), bg="white", font="Verdana 15 bold")
#sekil_alani.place(x=10, y=360)

#sekil_durumu = tk.Label(text=('ŞEKİL     '), bg="white", font="Verdana 15 bold")
#sekil_durumu.place(x=10, y=300)

# renk  = tk.Label(text=('RENGİ'), bg="white",font="Verdana 15 bold")
# renk.place(x=10, y=500)

# renk_durumu=tk.Label(text=('-----------'), bg="white",font="Verdana 15 bold")
# renk_durumu.place(x=90, y=500)

# hsv_deger  = tk.Label(text=('HSV DEĞERLERİ'), bg="white",font="Verdana 15 bold")
# hsv_deger.place(x=10, y=405)

"""
s2=datetime.datetime.now()
s3=datetime.datetime.strftime(s2,'%d.%m.%Y')
sistem_saati2=tk.Label(text=(s3), bg="white",font="Verdana 10 bold")
sistem_saati2.place(x=450,y=10)
"""
pencere.mainloop()


cap.release()
cv2.destroyAllWindows()




