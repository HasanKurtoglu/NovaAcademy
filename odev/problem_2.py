a = input("İlk Sayıyı Giriniz: ")
b = input("İkinci Sayıyı Giriniz: ")
c = input("Üçüncü Sayıyı Giriniz: ")

if a >= b and a >= c :
    buyuk = a 
elif b >= a and b >=c :
    buyuk = b
else :
    buyuk = c
    
print(f"Verdiğin {a, b, c} sayıları arasında en büyüğü '{buyuk}' sayısıdır.")