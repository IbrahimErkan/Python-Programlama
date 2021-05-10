#SAYILAR VE STRINGLERE GIRIS

9
9.2
9+9
9*9

print("HELLO AI ERA")
'HELLO AI ERA'

type(9)
type(9.2)
type("HELLO AI ERA")



#STRİNGLERE YAKINDAN BAKALIM


""
''

123
type(123)
"123"
type("123")

"a" + "b"
"a" "b"
"a" " b"
"a" + "-b"

"a" - "b"

"a "*3
"a"/3



#STRING METODLARI - LEN

gel_yaz = "gelecegi_yazanlar"
#del mvk

a = 9
b = 10

a*b


len(gel_yaz)
len("gelecegi_yazanlar")

#del a
#del b



#STRİNG METODLARI - upper() & lower()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.islower()
B.isupper()



#STRİNG METODLARI - replace()

gel_yaz  = "geleceği_yazanlar"

gel_yaz.replace("e","a")

gel_yaz.replace("a","i")



#STRİNG METODLARI - strip()

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()

gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")

gel_yaz = "llgelecegi_yazanlar"
gel_yaz.strip("l")



#METODLARA GENEL BAKIS

gel_yaz = "gelecegi_yazanlar"


dir(gel_yaz)

gel_yaz.capitalize()
gel_yaz.title()



#SUBSTRINGLER

gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]

gel_yaz[20]

gel_yaz[0:3]

gel_yaz[3:7]



#DEGISKENLER

a = 9
b = "ali_uzaya_git"
c = a*6


a/c
a*c
a*5

type(100)
type(100.2)
type(1+4j)

a = 100.2



#TYPE_DONUSUMLERI

toplama_bir = input()
toplama_iki = input()


type(toplama_bir)

toplama_bir + toplama_iki


int(toplama_bir) + int(toplama_iki)


int(11.0)

12

float(12)

type(str(12))



#print()

print("HELLO AI ERA")

print("gelecegi","yazanlar")

print("gelecegi","yazanlar", sep = "_")

print()

type()

print()

?print



#VERI YAPILARI - Listeler

# 1-Kapsayıcıdır
# 2-Değiştirilebilir
# 3-Sıralıdır


#[]
#list()

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90, notlar]

len(list_genis)

list_genis[0]
list_genis[1]
list_genis[3]

type(list_genis[1])

tum_liste = [liste, list_genis]

#del tum_liste



#Listeler - Eleman Islemleri

liste = [10,20,30,40,50]

liste[0]
liste[1]

liste[6]

liste[0:2]

liste[:2]

liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste

yeni_liste[2]

yeni_liste[0:2]

yeni_liste[2][1]



#Listeler - Eleman Degistirme 

liste = ["ali", "veli", "berkcan", "ayse"]
liste

liste[1] = "velinin_babasi"
liste

liste[1] = "veli"

liste[0:3] = ["alinin_babasi","velinin_babasi","berkcanin_babasi"]
liste

liste = ["ali","veli","berkcan","ayse"]
liste

liste = liste + ["kemal"]
liste

del liste[4]
liste



#Listeler - Liste Metodları

liste = ["ali", "veli", "isik"]

dir(liste)

liste

#append & remove

liste.append("berkcan")
liste

liste.remove("berkcan")
liste



#insert

liste = ["ali", "veli", "isik"]
liste

liste.insert(0,"ayse")
liste

liste = ["ali", "veli", "isik"]

liste[0] = "ayse"
liste

liste.insert(0,"ayse")
liste

liste[1] = "ali"
liste

liste.insert(2,"mehmet")
liste

liste.insert(5,"berk")
liste

#***
liste.insert(len(liste),"beren")
liste


#pop

liste.pop(0)
liste

liste.pop(4)
liste


#count

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")


#copy

liste_yedek = liste.copy()


#extend

liste.extend(["a","b",10])
liste


#index()

liste.index("ali")


#reverse()

liste.reverse()
liste


#sort()

liste = [10,40,5,80,1,56]
liste.sort()
liste


#clear

liste.clear()
liste



#VERI YAPILARI - Tuple

# 1-Kapsayıcıdır
# 2-Sıralıdır
# 3-Değiştirilemez

#Tuple Olusturma

t = ("ali","veli",1,2,3.2,[1,2,3,4])

t = "ali","veli",1,2,3.2,[1,2,3,4]

#tuple()

t = ("eleman",)

type(t)


#Tuple Eleman Islemleri

t = ("ali","veli",1,2,3,[1,2,3,4])
t

t[1]
t[0:3]

t[2] = 99



#VERİ YAPILARI - Dictionary (Sözlük)

# 1-Kapsayıcıdır
# 2-Sırasızdır
# 3-Değiştirilebilirdir

#Listelerde oldugu gibi index işlemleri yapılamaz.

#Sozluk Olusturma

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk

len(sozluk)

sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk


sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}

sozluk


#Sozluk Eleman Islemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}


sozluk[0]

sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}

sozluk["REG"]

sozluk = {"REG" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "LOJ" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "CART" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30}}

sozluk

sozluk["REG"]["MSE"]


#Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk["GBM"] = "Gradient Boosting Mac"

sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1] = "Yapay Sinir Aglari"
sozluk

l = [1]
l

sozluk[l] = "yeni bir sey"

t = ("tuple",)

sozluk[t] = "yeni bir şey"
sozluk



#VERI YAPILARI - Setler

# 1-Sırasızdır
# 2-Değerleri eşsizdir
# 3-Değiştirilebilirdir
# 4-Farklı tipleri barındırabilir

#Set Oluşturmak

s =set()
s

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")

s = set(t)
s

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s

l = ["ali", "lutfen", "ata", "bakma", "uzaya", "git", "git", "ali", "git"]
l

s = set(l)
s

len(s)

l[0]

s[0]



#Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]

s = set(l)
s

dir(s)

s.add("ile")
s

s.add("ahmet")
s

s.remove("ahmet")
s

s.add("gelecege_git")
s

s.add("ali")
s

s.add("ile")
s

s.remove("ali")
s

s.remove("ali")
s

s.discard("ali")
s


#Setler - Klasik Kume Islemleri

# =============================================================================
# differnce() ile iki kumenin farkini ya da "-" ifadesi intersection() iki kume 
# kesisimi ya da "&" ifadesi union() iki kumenin birlesimi symmetric_difference() 
# ikisinde de olmayanlari.
# =============================================================================


#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1


#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


kesisim = set1 & set2
kesisim


set1.union(set2)

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


#Set Sorgu Islemleri


set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


# iki kumenin kesisiminin bos olup 
# olmadiginin sorgulanması

set1.isdisjoint(set2)


<<<<<<< Updated upstream
=======
#bir kumenin butun elemanlarinin baska bir kume
#icerisinde yer alıp almadıgı

set1.issubset(set2)


#bir kumenin bir diger kumeyi kapsayıp kapsamadıgı

set2.issuperset(set1)



#Veri Yapıları - özet

#Listeler: Değiştirilebilir
#          Sıralıdır
#          Kapsayıcıdır

#Tuple:    Değiştirilemez
#          Sıralıdır
#          Kapsayıcıdır

#Sözlük:   Değiştirilebilir
#          Sırasızdır
#          Kapsayıcıdır

#Setler:   Değiştirilebilir
#          Sırasız + Eşsizdir
#          Kapsayıcıdır



# FONKSİYONLARA GIRIS VE FONKSİYON OKURYAZIRLIGI


print("A","B",sep="_")
?print
print()

len("a")


#Matematiksel Islemler

4*4
4/4
5-1
6+3
3**2


#Fonksiyon Nasil Yazilir?

4**2

def kare_al(x):
    print(x**2)

kare_al(5)


#Bilgi Notuyla Cikti Uretmek

def kare_al(x):
    print(x**2)

kare_al(5)

def kare_al(x):
    print("Girilen Sayinin Karesi:" + str(x**2))

kare_al(3)


def kare_al(x):
    print("Girilen Sayi:" + str(x) + " Karesi:" + str(x**2))

kare_al(3)


#Iki Argümanli Fonksiyon Tanimlamak

def kare_al(x):
    print(x**2)
    

def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(3,5)


#On Tanımlı Argumanlar

?print

def carpma_yap(x,y=4):
    print(x*y)
    
carpma_yap(3)

print("HELLO AI ERA")

#Argumanlarin Siralamasi

def carpma_yap(x, y=1):
    print(x*y)

carpma_yap(y = 2, x = 3)

carpma_yap(2,3)


#Ne Zaman Fonksiyon Yazilir?

#!Fonksiyonlar, sık tekrar eden ya da uzun işlemlerden kurtulmak adına yazdığımız şeylerdir.

def direk_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)

direk_hesap(25,40,70)


#Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi, nem, sarj):
    print((isi + nem)/sarj)
    
cikti = direk_hesap(25,40,70)
cikti
print(cikti)
direk_hesap(25,40,70)*9


#!Yazmış oldugumuz bir fonksiyonun çıktısını başka bir işlemin girdisi olarak 
#kullanmak istiyorsak return ifadesini kullanıyoruz.

def direk_hesap(isi, nem, sarj):
    return (isi + nem)/sarj

cikti = direk_hesap(25,40,70)
cikti
print(cikti)


def direk_hesap(isi, nem, sarj):
    return 
    (isi + nem)/sarj

direk_hesap(25,40,70)



#Local ve Global Degiskenler

x = 10                                 # Global degiskenler                      
y = 20


def carpma_yap(x = 2, y = 1):          # Local degiskenler
    return x*y

carpma_yap(2,3)


#Local Etki Alanindan Global Etki Alanini Degistirmek

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
eleman_ekle("ali")
eleman_ekle("mustafa")

x



# KARAR & KONTROL YAPILARI

#True-False Sorgulamaları

sinir = 5000
sinir == 4000
sinir == 5000

5 == 4
5 == 5 


#if 


sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
    print("Gelir sinirdan kucuk")
    
    
if gelir > sinir:
    print("Gelir sinirdan kucuk")


#else

sinir = 50000
gelir = 35000

if gelir > sinir:
    print("Gelir sinirdan buyuk")
else:
    print("Gelir sinirdan kucuk")


#diger ornek
sinir = 50000
gelir = 51000

if gelir == sinir:
    print("Gelir sinira eşittir.")
else:
    print("Gelir sinira eşit degildir.")


#elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir1 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")


if gelir3 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir3 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")


if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
elif gelir2 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")



#mini uygulama

sinir = 50000
magaza_adi = input("Magazanin adını girin: ")
magaza_gelir = int(input("Magazanin gelirini girin: "))

if magaza_gelir > sinir:
    print("Tebrikler," + magaza_adi + " promosyon kazandınız!")
elif magaza_gelir < sinir:
    print("Uyari! Çok dusuk gelir: " + str(magaza_gelir))
else:
    print("Takibe devam")    



# DONGULER - for

#Verilen listenin her bir elemanını iteratif bir şekilde yakalayıp belirli bir 
#işleme tabi tutmak için for dongusu kullanılır.


ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)


maaslar  = [1000,2000,3000,4000,5000]

for maas in maaslar:
    print(maas*1/2)


for i in range(0,10):
    print(i)

#dongu ve fonksiyonları birlikte kullanmak

def kare_al(x):
    print(x**2)

kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)


#Ornek: maaslara yuzde 20 zam yapılacak gerekli kodları yaziniz.

1000*20/100 + 1000

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]

#bir şeyi çok tekrar edeceğimiz için döngü yazilacak
#bazı matematik işlemler yapagımız içinde fonksiyonlar kullanıcaz

def yeni_maas(x):
   print(x*20/100 + x)

yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)


for i in maaslar:
     yeni_maas(i)


#Ornek2: if, for ve fonksiyonları birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)

def maas_alt(x):
    print(x*20/100 + x)
    
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
        
    else:
        maas_alt(i)
>>>>>>> Stashed changes



#break & continue
#break: Bir dongu bloku  icinde verilen bir break komutu, dongunun hemen o anda bitmesine yol acar.
#continue: Türkcedeki anlamı “devam” etmek olan bu deyim, verilen kodu calıstırmadan bi sonraki koda geçer.

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
    

for i in maaslar:
    if i == 3000:
        continue
    print(i)
    


#While loop

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)




#OOP - NESNE YONELİMLİ PROGRAMLAMA

#Nesne Tabanlı Programlama gerçek hayattaki nesneleri yazılım dünyasına aktarma çabasıdır. 
#Örneğin yeni bir araba üretecek bir firmayı düşünelim. Somut olarak üretilecek olan arabanın
#tüm özellik (attributes) ve fonksiyonlarını (method) ilk olarak yazılıma aktarmak gerekiyor. 
#Bu aktarım aşamasının kendisi aslında arabanın tüm özellik ve fonksiyonlarını içerecek olan 
#bir sınıfın (class) oluşturmasıdır. Sınıf tanımlanmasından sonra ise sınıfın tüm özellik ve 
#yeteneklerine sahip olacak her kopyaya ise nesne (object) diyoruz.


#Class - Sınıf: Benzer özellikler, ortak amaclar tasıyan, icerisinde metod ve degiskenler olan yapılardır.

class VeriBilimci():
    print("Bu bir sınıftır")

#Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

#Siniflarin ozelliklerine erismek
VeriBilimci.bolum
VeriBilimci.sql

#Siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayır"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql
veli.bildigi_diller

#Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
        
ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller


ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller


VeriBilimci.bolum
ali.bolum = "istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum


#Ornek Metodlari

class VeriBilimci():
    calısanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle("R") # hata verecek

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("Python")
veli.bildigi_diller



#Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
veribilimci1.
        
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""
        
mar1 = Marketing()        
mar1. 



#Python'da Fonksiyel Programlama

#Fonksiyonlar dilin bastacidir.
#Birinci sinif nesnelerdir.
#Yan etkisiz fonksiyonlardır. (stateless, girdi-cikti)
#Yuksek seviye fonksiyonlardır.
#Vektorel operasyonlar.


#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1:Bagimsizlik

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b


impure_sum(6)
pure_sum(3,7)



    






























