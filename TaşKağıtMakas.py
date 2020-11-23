
taskagitmakas=("taş","kağıt","makas")
import random
while True:
    sen=0
    bilgisayar=0
    taş=taskagitmakas[0]
    kağıt=taskagitmakas[1]
    makas=taskagitmakas[2]
    secim=input("Taş mı?,Kağıt mı?,Makas mı?:")
    pc=random.choice(taskagitmakas)
 
    print("Bilgisayar",pc,"elemanını seçti.")

    if secim==taş:
        if pc==taş:
           print("Berabere sonuçlandı.")
        elif pc==kağıt:
           print("Kaybettiniz.")
        elif pc==makas:
           print("Kazandınız.")
    elif secim==kağıt:
        if pc==kağıt:
           print("Berabere sonuçlandı.")
        elif pc==taş:
           print("Kazandınız."),
        elif pc==makas:
           print("Kaybettiniz.")
    elif secim==makas:
        if pc==makas:
           print("Berabere sonuçlandı.")
        elif pc==taş:
           print("Kaybettiniz.")
        elif pc==kağıt:
           print("Kazandınız.")
