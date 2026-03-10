# Kullanıcıdan iki sayı alalım
sayi1 = input("Birinci sayıyı girin: ")
sayi2 = input("İkinci sayıyı girin: ")

print(f"Değiştirilmeden önce: Sayı 1 = {sayi1}, Sayı 2 = {sayi2}")

# Değerleri değiştirme
sayi1, sayi2 = sayi2, sayi1

print(f"Değiştirildikten sonra: Sayı 1 = {sayi1}, Sayı 2 = {sayi2}")