english = input("For english write 'Yes', Türkçe devam etmek istiyorsan 'Evet yaz': ")
if english == "Yes":
    print("Enter the number for which you want to find the square root.")
elif english == "Evet":
    print("Karekökünü bulmak istediğiniz sayıyı giriniz: ")
else: 
    print("Only numbers are allowed/Sadece sayılar geçerlidir")
    
sayi = float(input())

karekok = sayi ** 0.5

print(f"{int(sayi)} Sayısının karekökü: {karekok}")
