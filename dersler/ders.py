# Yorum Satırı



"""
Yorum
Paragrafı

ctrl-z = geri alma
ctrl-y = ileri alma
ctrl-x = kesme
ctrl-c = kopyalama
ctrl-v = yapıştırma
ctrl-s = kaydetme
"""



#print() 
"""  
Python'da herhangi bir matematiksel işlemin,string ifadenin veya bir kod çalışması sonucunda dönen değeri 
Terminal ekranında gösteren method 
2+2 
print(2+2)
print("merhaba") 
"""



#                                          string ifadeler 

"""
string ifadeler
Herhangi bir kelime,cümle,harf gibi metinsel ifadeler açıktan yazılamaz mutlaka tırnak işareti içerisinde yazılmak 
zorundadır 

print('nasılsın')
print('Doğukan'a')
print("Doğukan'a")
"""



#                                           number ifadeler 

"""
number ifadeler
Herhangi bir sayı,rakam gibi matematiksel ifadeler tırnak işareti içerisinde yazılmaz yazarsak matematiksel
bir işlem yapamayız  

print("4")
print("4+4")
print(4+4)
print(4)
print("4"+"4")
"""


#a-integer ifadeler 
""" 
Tam sayıları ifade eden sayılardır 
2,4,-5,-7,-8,1000
"""

#b-float() ifadeler 
""" 
ondalıklı sayıları ifade eden sayılardır 
0.5 , 7.8 , 6.9   
"""



#                           str() int() float() fonksiyonları 

"""
str(),int(),float() Python'daki farklı veri tiplerini birbirine dönüştürmek için kullanılan
fonksiyonlardır 
"""

#1-str()
""" 
Bir nesneyi metin haline dönüştürür.Örneğin; bir sayı veya başka bir veri türünü metinsel 
ifadeye dönüştürür 
print(2+2)
print(str(2)+str(2))
2=>'2'
"""




#2-int() 
""" 
bir ondalıklı sayıyı veya metinsel ifadeyi tam sayıya dönüştürür 


print("2"+"2")
print(int("2")+int("2"))
print(int("2+2"))
"2" =>2
"""



#3-float()
""" 
bir tam sayıyı ondalıklı sayıya dönüştürür 
print(2+2) 
print(float(2)+float(2))
"""  




#                                  Boolean yapısı 
""" 
Boolean,Python'da mantıksal ifadeleri temsil etmek için kullanılan bir veri tipidir 
Bu veri tipi sadece iki değeri alabilir 
1-TRUE 
2-FALSE 
Boolean değerleri genellikle karar yapıları oluşturmak,koşul ifadelerinde şart yazmak ve 
döngülerin kontrolünde kullanılır 
print(4<10)
print(2==3)
x=20
if x<10:
    print("nasılsın")
"""

 

#                               Aritmetik Operatörler 
#1-artı operatörü(+)
""" 
iki temel görevi vardır 
1-toplama işlemi yapar(number ifade olması gerekiyor)
2-birleştirme görevi vardır 

print(10+2)
print("Doğukan"+" "+"Yıldız")
"""


#2-yıldız operatörü(*)
""" 
iki temel görevi vardır
1-çarpma işlemi yapar(number ifade olması gerekiyor) 
2-Çoğaltma görevi vardır(kopyala yapıştır mantığı)
print(2*3)
print(-3*2)
print(2+3*5)
print(10-2*3)
print((10-2)*3+2)
"""


#Bir öğrenci Matematik dersinden 3 sınava girmiştir.Sınav notları sırasıyla 50,40,35 
#buna göre bu öğrencinin dönem sonu not ortalaması kaçtır 
""" 
print((50+40+35)/3)
"""

#Matematikte işlem önceliği 
""" 
parantez içi işlemler 
üslü ifadeler 
çarpma bölme 
toplama çıkarma 


print("merhaba "*10)
print("merhaba\n"*10)
"""



#3-Çıkarma operatörü(-)
""" 
matematiksel olarak çıkarma işlemi yapar 
"""
#print(10-2)
#print(2-10)



#4-Bölme operatörü(/-//)
# / Operatörü
""" 
matematiksel olarak bölme işlemi yapar 
sonuç olarak bölüm kısmını gösterir
sonucu float olarak döndürür  
"""

# // operatörü 
""" 
Bölme işlemi yaparken bölüm kısmının sadece tam sayı kısmını döndüren bir operatördür 
Özellikle bir sayının başka bir sayıya bölümünde tam kısmını elde etmek istediğimizde 
kullanırız

print(4//2)
print(20//4)
print(7//3)
"""



#5-Üslü işlemler için kullanılan operatör(**)
""" 
ilk yazılan sayı taban sayısıdır 
ikinci yazılan sayı kuvvet sayısıdır 
iki sayı arasında ** operatörü vardır  

print(2**3)#2 üzeri 3 demek 
print(7**2)#7 üzeri 2 demek
"""