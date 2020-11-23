###SAAT,DAKİKA,SANİYE Çevirme Programı###

print("""
   [1]Saat'i Dakika'ya Çevir. 
   [2]Saat'i Saniye'ye Çevir. 
   [3]Dakika'yı Saat'e Çevir.
   [4]Dakika'yı Saniye'ye Çevir.
   [5]Saniye'yi Saat'e Çevir.
   [6]Saniye'yi Dakika'ya Çevir. 
""")

secim=input("Seçiminizi Giriniz:")
if secim=="1":
    saat=int(input("Saat Değeri Giriniz:"))
    dakika=int(saat*60)
    print(saat,"saat",dakika,"dakikaya eşittir.")
elif secim=="2":
    saat=int(input("Saat Değeri Giriniz:"))
    saniye=int(saat*3600)
    print(saat,"saat",saniye,"saniyeye eşittir.")
elif secim=="3":
    dakika=int(input("Dakika Değeri Giriniz:"))
    saat=float(dakika/60)
    print(dakika,"dakika",saat,"saate eşittir.")
elif secim=="4":
    dakika=int(input("Dakika Değeri Giriniz:"))
    saniye=int(dakika*60)
    print(dakika,"dakika",saniye,"saniyeye eşittir.")
elif secim=="5":
    saniye=int(input("Saniye Değeri Giriniz:"))
    saat=float(saniye/3600)
    print(saniye,"saniye",saat,"saate eşittir.")
elif secim=="6":
    saniye=int(input("Saniye Değeri Giriniz:"))
    dakika=float(saniye/60)
    print(saniye,"saniye",dakika,"dakikaya eşittir.")
