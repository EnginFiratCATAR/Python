def topla(x,y):
    return x+y
def cıkar(x,y):
    return x-y
def carp(x,y):
    return x*y
def bol(x,y):
    return x/y
while True:
  print("""
      [1]Toplama İşlemi Yap.
      [2]Çıkarma İşlemi Yap.
      [3]Çarpma İşlemi Yap.
      [4]Bölme İşlemi Yap.
     """)
  secim=input("Seçiminiz:")
  if secim=="1":
    sayı1=int(input("1.Sayı'yı Giriniz:"))
    sayı2=int(input("2.Sayı'yı Giriniz:"))
    print(sayı1,"+",sayı2,"=",topla(sayı1,sayı2))
  elif secim=="2":
    sayı1=int(input("1.Sayı'yı Giriniz:"))
    sayı2=int(input("2.Sayı'yı Giriniz:"))
    print(sayı1,"-",sayı2,"=",cıkar(sayı1,sayı2))
  elif secim=="3":
    sayı1=int(input("1.Sayı'yı Giriniz:"))
    sayı2=int(input("2.Sayı'yı Giriniz:"))
    print(sayı1,"*",sayı2,"=",carp(sayı1,sayı2))
  elif secim=="4":
    sayı1=int(input("1.Sayı'yı Giriniz:"))
    sayı2=int(input("2.Sayı'yı Giriniz:"))
    print(sayı1,"/",sayı2,"=",bol(sayı1,sayı2))
  else:
    print("Hatalı Giriş!","\n","Lütfen Tekrar Deneyiniz.")
    break
    