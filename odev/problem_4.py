print("""Geometri şekil hesaplama sistemine hoş geldiniz.
      Hesaplayabileceğiniz geometrik şekilleer;
      
      Dörtgen
      Üçgen
      """)
girdi = input("Lütfen ne hesaplamak istediğinizi belirtiniz: ")

if girdi.lower() == "dörtgen":
    print("Lütfen belirtilen sırada dörtgenin kenar ölçülerini giriniz")
    ust_kenar = int(input("Üst kenar ölçüsü: "))
    sag_kenar = int(input("Sağ kenar ölçüsü: "))
    alt_kenar = int(input("Alt kenar ölçüsü: "))
    sol_kenar = int(input("Sol kenar ölçüsü: "))
    if sol_kenar == ust_kenar and sol_kenar == alt_kenar and sol_kenar == sag_kenar:
        sekil = "kare"
    elif sol_kenar == sag_kenar and ust_kenar == alt_kenar:
        sekil = "dik"
    else:
        sekil = "sıradan"
    print(f"Verilen kenarlara göre {ust_kenar, alt_kenar, sol_kenar, ust_kenar} ortaya çıkan {sekil} bir {girdi}")
elif girdi.lower() == "üçgen":
    print("Lütfen belirtilen sırada üçgenin kenar ölçülerini giriniz")
    birinci_kenar = int(input("Birinci kenar ölçüsü: "))
    ikinci_kenar = int(input("İkinci kenar ölçüsü: "))
    ucuncu_kenar = int(input("Üçüncü kenar ölçüsü: "))
    if birinci_kenar == ikinci_kenar == ucuncu_kenar:
        sekil = "eşkenar"
    elif birinci_kenar == ikinci_kenar or birinci_kenar == ucuncu_kenar or ikinci_kenar == ucuncu_kenar:
        sekil = "ikizkenar"
    else:
        sekil = "sıradan"
    print(f"Verilen kenarlara göre {birinci_kenar, ikinci_kenar, ucuncu_kenar} ortaya çıkan {sekil} bir {girdi} üçgen")
else: 
    print(f"{girdi} hatalı bir komut lütfen üçgen ya da dörtgeni deneyin")
