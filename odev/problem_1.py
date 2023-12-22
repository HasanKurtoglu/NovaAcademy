print("""
      Beden kitle indeksi hesaplamaya hoş geldiniz
      """)
kilo = float(input("Lütfen kilonuzu giriniz: "))
boy = float(input("Lütfen boyunuzu santimetre cinsinden giriniz: "))

boy = boy / 100
indeks = kilo / (boy * boy)

if indeks <= 18.5:
      seviye = "Zayıf"
elif indeks <= 25:
      seviye = "Normal"
elif indeks <= 30:
      seviye = "Fazla Kilolu"
else:
      seviye = "Obezite"
      

      
print(f"Beden kitle indeksine göre kilonuz {seviye} seviyesinde. Oranınız -> {indeks}")
