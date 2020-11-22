print("ENGİN FIRAT CATAR...")
print("""
!!!UYARI!!!\n
Kullanıcı adı en az 5 karaktere sahip olmalıdır.
""")
while True:
  kull_ad=str(input("Kullanıcı Adı Oluşturunuz:"))
  if len(kull_ad)==1:
      print("Kullanıcı Adı Çok Kısa.","\n","Tekrar Deneyiniz.")
  elif len(kull_ad)==2:
      print("Kullanıcı Adı Çok Kısa.", "\n", "Tekrar Deneyiniz.")
  elif len(kull_ad)==3:
      print("Kullanıcı Adı Kısa.", "\n", "Tekrar Deneyiniz.")
  elif len(kull_ad)==4:
      print("Kullanıcı Adı Kısa.", "\n", "Tekrar Deneyiniz.")
  else:
      print("Geçerli Kullanıcı Adı Oluşturma.")
      break
print("""
!!!UYARI!!!\n
Şifre en az 6 karaktere sahip olmalıdır.
""")
while True:
    şifre = input("Şifre Oluşturunuz:")
    if len(şifre)==1:
        print("Şifre Çok Kısa","\n","Tekrar Deneyiniz.")
    elif len(şifre)==2:
        print("Şifre Çok Kısa", "\n", "Tekrar Deneyiniz.")
    elif len(şifre) == 3:
        print("Şifre Çok Kısa", "\n", "Tekrar Deneyiniz.")
    elif len(şifre)==4:
        print("Şifre Çok Kısa", "\n", "Tekrar Deneyiniz.")
    elif len(şifre)==5:
        print("Şifre Çok Kısa", "\n", "Tekrar Deneyiniz.")
    else:
        print("Geçerli Şifre Oluşturma.")
        break
###KAYIT YERİ###
print("Oluşturduğunuz bilgileri giriniz.")
while True:
    ad_kull = input("Kullanıcı Adınızı Giriniz:")
    parola = input("Parolanızı Giriniz:")
    if (ad_kull == kull_ad) and (şifre == parola):
        print("Doğru Giriş")
        break
    else:
        print("Kullanıcı Adı ve ya Parola yanlış!!!","\n","Tekrar Deneyiniz...")

