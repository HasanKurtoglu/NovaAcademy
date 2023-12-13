import random

sayi = random.randint(1, 20)
tahmin = 0

while tahmin != sayi:
    tahmin = int(input("1 ile 20 arasında bir sayı tahmin edin: "))
    if tahmin < sayi:
        print("Daha yüksek bir sayı deneyin.")
    elif tahmin > sayi:
        print("Daha düşük bir sayı deneyin.")
    else:
        print("Tebrikler, doğru tahmin!")