rehber={
    "Engin":"05550635759",
    "Fırat":"05428854745",
    "Catar":"05065428683"
}
def rehber():
 while True:
    print(list(rehber))
    print("""
       [1] Kişi Ekle
       [2] Kişi Sorgula
       [3] Kişi Sil
       [Q] Çık 
    """)
    secim=input("Seçim:")
    if secim=="1":
        kisi=input("Kişi:")
        numara=input("Numara:")
        rehber.setdefault((kisi,numara))
        print(rehber)
    elif secim=="2":
        isim=input("Sorgu İsmi:")
        if isim in rehber.keys():
            print(rehber.get(isim))
        else:
            print("Aranan kişi rehberde bulunamıyor!")
    elif secim=="3":
        kisi=input("Silinecek Kişi:")
        varmi=kisi in rehber.keys()
        if varmi:
            rehber.pop(kisi)
        else:
            print("Silinmesi istenen {} kişisi rehberde yer almıyor".format(kisi))
    elif secim=="q" or "Q":
        break
    else:
        print("Hatalı Giriş Değeri!")
