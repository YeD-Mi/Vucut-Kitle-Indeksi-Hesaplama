def hesaplasayi(en,boy):
    VKI=int(en)/(int(boy)/100*int(boy)/100)
    return VKI
def hesaplasinif(VKI_sayisi):
    if(VKI_sayisi>=30):
        VKI_sinifi="Obezite"
    elif (VKI_sayisi<30) and (VKI_sayisi>=25):
        VKI_sinifi="Asiri Kilo"
    elif (VKI_sayisi<25) and (VKI_sayisi>=18.5):
        VKI_sinifi="Normal"
    elif (VKI_sayisi<18.5):
        VKI_sinifi="Dusuk Kilo"
    else:
        VKI_sinifi="Gecersiz islem"
    return VKI_sinifi
try:
   with open("output.txt", "w") as yazdir:
      with open ("input.txt","r",encoding="utf-8") as data:
       for satir in data:
        veri=satir.split()
        ad=veri[0]
        VKI_sayisi=round(hesaplasayi(veri[1],veri[2]),2)
        VKI_sinifi=hesaplasinif(VKI_sayisi)
        yazdir.writelines("%s - %g - %s \n" % (ad,VKI_sayisi,VKI_sinifi))
   yazdir.close()
   print("İslem tamamlandi. Output dosyasını kontrol edebilirsiniz.")
except IOError:
    print("Text dosyasi bulunamadi!")
finally:
    data.close()
