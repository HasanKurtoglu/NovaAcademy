print("""
      Not hesaplama sistemine hoş geldiniz.
      
      Sınavlarınızın toplam nota etkisi şu şekildedir;
      
      Birinci vize %30
      
      İkinci vize %30
      
      Final %40
      
      """)

vize1 = int(input("Birinci vize sınavı notunu yaz: "))
vize2 = int(input("İkinci vize sınavı notunu yaz: "))
final = int(input("Final sınavı notunu yaz: "))

vize1_not = ( vize1 / 100 ) * 30
vize2_not = ( vize2 / 100 ) * 30
final_not = ( final / 100 ) * 40

toplam_not = vize1_not + vize2_not + final_not

if toplam_not >= 90:
      notunuz = "AA"
elif toplam_not >= 85:
      notunuz = "BA"
elif toplam_not >= 80:
      notunuz = "BB"
elif toplam_not >= 75:
      notunuz = "CB"
elif toplam_not >= 70:
      notunuz = "CC"
elif toplam_not >= 65:
      notunuz = "DC"
elif toplam_not >= 60:
      notunuz = "DD"
elif toplam_not >= 55:
      notunuz = "FD"
elif toplam_not < 55:
      notunuz = "FF"
      

print(f"""Verdiğiniz notlara göre toplam notunuz {toplam_not}, harf notunuz {notunuz}.
      Vize 1 notunuz {vize1}.
      Vize 2 notunuz {vize2}.
      Final notunuz {final}.
      Eğer görünen notlarda bir yanlışlık varsa tekrar hesaplayınız...""")