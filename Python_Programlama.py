#SAYILAR VE STRINGLERE GIRIS
9
9.2
9+9

print('HELLO AI ERA')
"HELLO AI ERA"

type(9)
type(9.1)
type("hello aÄ± era")

#STRINGLERE yakından bakalım:
    
type(123)
type("123")

'a' + 'a'
"a" + "a"
a * a

#STRING METHODLARI - LEN

gel_yaz = "gelecegi_yazanlar"
#del mvk

a = 9
b = 10

a*b

len(gel_yaz)

#STRING METHODLARI - upper() & lower()

gel_yaz = "gelecegi_yazanlar"

gel_yaz.upper()

gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()

B.islower()
B.isupper()


#STRING METHODLARI - replace

gel_yaz = "gelecegi_yazanlar"

gel_yaz.replace("e","a")

gel_yaz.replace("a","i")


#STRING METHODLARI - strip()

gel_yaz = " gelecegi_yazanlar    "
gel_yaz.strip()


gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*")


#METHODLARA GENEL BAKIS

gel_yaz = "gelecegi_yazanlar"

dir(gel_yaz)

gel_yaz.capitalize()

gel_yaz.title()


#INDEKSLEME

gel_yaz = "gelecegi_yazanlar"

gel_yaz[0]
gel_yaz[5]
gel_yaz[20]

gel_yaz[0:3]

gel_yaz[3:7]

#DEGISKENLER

a = 99999
b = "ali uzaya git"

c = a*6

a / c

a*c
a*5

type(100)
type(1000.3)
type(1+2j)

#TYPE_DONUSUMLERI

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)


str(12)

float(124)


int(10.0000)

12


#print()

print("HELLO AI ERA")


print("gelecegi","yazanlar")

print("gelecegi","yazanlar", sep = "_")

print()

type()

a = ["1,2,3"]

a.append(8)

print(a)

"9" + "1"


a = "gelecek"
a.lower()

"3"
type("3")

ifade = "1012340"
ifade = ifade + "1"
ifade.strip("1")

"9" + 1

ifade = "gelecegi yaziyoruz"
ifade[1]


print("uzaya", "git", sep = "**")


#VERI YAPILARI

#Listeler

#[]
#list()


notlar = [90,70,55,40]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90,notlar]

len(list_genis)

list_genis[3]
list_genis[1]
type(list_genis[0])

tumListe = [liste,list_genis]

del tumListe

#Listeler - Eleman Islemleri

liste = [10,20,30,40,50]

liste[1]
liste[0]

liste[6]

liste[0:2]

liste[:2]

liste[2:]


yeniListe = ["a",10,[20,30,40,50]]

yeniListe

yeniListe[2]

yeniListe[0:2]

yeniListe[2][1]


#Listeler - Eleman Degistirme

liste = ["ali","veli", "berkcan","ayse"]
liste 


liste[1] = "velininBabasi"

liste

liste[1]= "veli"

liste[0:3] = "alininBabasi","velininBabasi","berkcaninBabasi"
liste

liste = ["ali","veli","berkan","ayse"]

liste

liste = liste + ["kemal"]
liste

del liste[2]
liste

#Listeler - Liste Methodlar

liste = ["ali","veli","isik"]

dir(liste)

liste

#append

liste.append("berkcan")
liste

liste.remove("berkcan")
liste

#insert

liste = ["ali","veli","isik"]

liste

liste.insert(0,"ayse")
liste

liste.insert(2,"mehmet")
liste

liste.insert(5,"berk")
liste

len(liste)

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

listeYedek = liste.copy()


#extend

liste.extend(["a","b",10])
liste

#index

liste.index("ali")


#reverse()

liste.reverse()
liste


#sort()

liste = [60,2,50,88,54]
liste.sort()
liste


#clear

liste.clear()
liste


#Veri Yapıları - Tuple


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


# Veri Yapıları - Dictionary(Sözlük)


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

benimSozluk = {"REG" :["RMSE", 10,],
          "LOJ" : ["MSE" ,20],
          "CART" : ["SSE",30]}

sozluk



benimSozluk["REG"]


benimSozluk = {"REG" :["RMSE", 10,],
          "LOJ" : ["MSE" ,20],
          "CART" : ["SSE",30]}


benimSozluk["REG"]

benimSozluk = {"REG" : {"RMSE": 10,
                       "MSE": 20,
                       "SSE": 30},
               
               "LOJ" : {"RMSE": 10,
                       "MSE": 20,
                       "SSE": 30},
               
               "CART" : {"RMSE": 10,
                       "MSE" : 20,
                       "SSE" : 30}}

benimSozluk
benimSozluk["REG"]["SSE"]


#Szoluk - eleman Eklemek & Degistirmek

benimSozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

benimSozluk["GBM"] = "Gradient Boosting Mac"
benimSozluk

benimSozluk["REG"] = "Çoklu Dogrusal Regresyon"
benimSozluk

benimSozluk[1] = "Yapay SinirAglari"

benimSozluk

l =[1]
l
benimSozluk[l] ="yeni bir sey"

t = ("tuple",)

benimSozluk[t] = "yeni bir sey"
benimSozluk



#Veri Yapilari - Setler

#Set Olusturmak

s = set()
s

l = [1,"ali",1234]
s = set(l)
s


t = ("a","ali")

s = set(t)
s

ali = "lutfen ata bakma uzaya git"
type(ali)

s =set(ali)
s


l = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]

l

s =set(l)
s

len(s)

l[0]

l[0]

s[0]


#Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]

s = set(l)
s

dir(s)

s.add("ile")
s

s.add("gelecege git")
s

s.add("ile")
s
s

s.remove("ile")
s

s.remove("ile")
s

s.discard("ile")
s

#Setler - Klasik Kume Islemleri

# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi 
# synmetric_difference() ikisinde de olmayanlari.




set1 = set([1,3,5])
set2 = set([1,3,4])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)

set1-set2
set2-set1


#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


#Set Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kumenin kesisiminin bos olup 
#olmadiginin sorgulanmasi

set1.isdisjoint(set2)


#bir kumenin butun elemanlarinin baska 
#bir kume icerisinde yer alip almadigi

set1.issubset(set2)

#bir kumenin bir diger kumeyi kapsayip kapsamadigi

set1.issuperset(set1)

liste = ["a","b","c"]
liste.reverse()
print(liste)

liste = [50,10,30,40]
liste.sort()
liste


sozluk = {"REG" : {"RMSE": 10,
                   "MSE": 11,
                   "SSE": 12},
 
          "LOJ" : {"RMSE": 111,
                   "MSE": 2222,
                   "SSE": 333},
 
          "CART" : {"RMSE": 99,
                    "MSE": 00,
                    "SSE": 66}}

sozluk["CART"]["SSE"]



liste = [10,10,20,40]
liste.clear()
liste


set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

liste = ["A","B","C"]

liste.append("D")
liste



liste = ["A","B","C"]
liste.insert(0, "D")
liste

liste = ["a","b","c"]
liste.index("b")

set([1,3,6,19])
print(type(set))
type



#*****************************************



#FONKSİYONLARA GIRIS VE FONKSİYON OKURYAZARLIGI


print("a","b", sep = "-")
?print
print()

len("a")



#Matematiksel Islemler

4*4
5-1
3**2
6+3


#Fonksiyon Nasil Yazilir?

#Bilgi Notuyla Cıktı Uretmek

def kareAl(x):
    print(x**2)
    
kareAl(5)    

def kareAl(x):
    print("Girilen Sayinin Karesi:" + str(x**2))

kareAl(3)


def kareAl(x):
    print("Girilen Sayisi:" + 
          str(x) + 
          ", Karesi:" +
          str(x**2))

kareAl(3)


#Iki Argumanli Fonksiyon Tanimlamak

def kareAl(x):
    print(x**2)

def carpmaYap(x,y):
    print(x*y)
    
carpmaYap(2,3)


#On Tanımlı Argumanlar

?print

def carpmaYap(x,y=2):
    print(x*y)

carpmaYap(3,4)

print("HELLO AI ERA")

#Argumanlarin Sıralamasi

def carpmaYap(x,y=1):
    print(x*y)

carpmaYap(2,3)

#Ne Zaman Fonksiyon Yazilir?

#isi, nem, sarj

(40 + 25) / 90


def direkHesap(isi,nem,sarj):
    print((isi+nem)/sarj)

direkHesap(25,40,70)

#Ciktiyi Girdi Olarak Kullanmak

def direkHesap(isi,nem,sarj):
    print((isi+nem)/sarj)
    
cikti = direkHesap(25,40,70)
cikti
print(cikti)

direkHesap(25,40,70)*9


def direkHesap(isi,nem,sarj):
    return (isi+nem)/sarj


cikti = direkHesap(25,40,70)
cikti
print(cikti)
direkHesap(25,40,70)*9


#Local ve Global Degiskenler


x = 10
y = 20

def carpmaYap(x,y):
    return x*y

carpmaYap(2,3)

#Local Etki Alanindan Global Etki Alanini Degistirmek

x = []

def elemanEkle(y):
    x.append(y)
    print(str(y)+ " ifadesi eklendi")

elemanEkle("ali")

elemanEkle("veli")
x


# KARAR & KONTROL YAPILARI

# True-False Sorgulamaları

sinir = 5000
sinir == 1000
sinir == 5000

5 == 4
5 == 5


#if

sinir = 50000
gelir = 60000

gelir < sinir


if gelir < sinir:
    print("Gelir sinirdan küçük")
    
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
gelir = 50000

if gelir == sinir:
    print("Gelir sinira eşittir")

else:
    print("Gelir sinira eşit değildir")


#elif 

sinir = 50000
gelir = 60000
gelir2 = 50000
gelir3 = 35000

if gelir > sinir:
    print("Tebrikler, hediye kazandınız.")
    
elif gelir <sinir:
    print("Uyarı!")
    
else:
    print("Takibe devam")




if gelir3 > sinir:
    print("Tebrikler, hediye kazandınız.")
    
elif gelir3 <sinir:
    print("Uyarı!")
    
else:
    print("Takibe devam")
50000

if gelir2 > sinir:
    print("Tebrikler, hediye kazandınız.")
    
elif gelir2 <sinir:
    print("Uyarı!")
    
else:
    print("Takibe devam")


#mini uygulama

sinir = 50000
magazaAdi = input("Magaza Adi Nedir: ")
gelir = int(input("Gelirinizi Giriniz: "))

if gelir > sinir:
    print("Tebrikler:" + magazaAdi + " promosyon kazandiniz")
    
elif gelir < sinir:
    print("Uyarı! Çok dusuk gelir:" + str(gelir))

else:
    print("Takibe Devam")
    
    
    
    
#DONGULER - for

ogrenci = ["ali","veli","isik","berk"]

ogrenci[0]
ogrenci[3]
ogrenci[1]

for a in ogrenci:
    print(a)


maaslar = [1000,2000,3000,4000,5000,6000]

for maas in maaslar:
    print(maas)


#dongu ve fonksiyonları birlikte kullanmak

def kareAl(x):
    print(x**2)

kareAl(2)


maaslar = [1000,2000,3000,4000,5000,6000]
for i in maaslar:
    print(i)


#maaslara yuzde 20 zam yapılacak gerekli kodlari
#yaziniz.

1000*20/1000



#mini uygulama
#if, for ve fonksiyonları birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maasUst(x):
    print(x*10/100 + x)
 
def maasAlt(x):
    print(x*20/100 + x)
    
for i in maaslar:
    if i>=3000:
        maasUst(i)
        
    else:
        maasAlt(i)

#break & continue

maaslar = [8000,5000,1000,2000,3000,7000,1000]

dir()

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


#while


sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)




def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)


def islem(x):
    if (x<0):
        return "NO"
    else:
        x*5
 
islem(4)


def harf_say(x):
    return (x)
 
harf_say("Merhaba!")


if [1,2,3,4][2] == 2:
    print("YES")
else:
    print("NO")


def mesaj():
    print("Merhaba!")    
    
mesaj()  


39/2


urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)


def kup_al(x):
     print(x**3)

kup_al(2)


if [1,2,3,4][1] == 2:
    print("YES".lower())
else:
    print("NO")

**********************************

if [1,2,3,4][2] == 2:
    print("YES")
else:
    print("NO")

for i in ["a",11]:
    print(i)


def islem(x, y):
    print(x + y)
 
islem(1,9)



A = []
B = []

for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)

A[1]

def yazdir(metin):
    print(metin, "yazanlar")
 
yazdir("gelecegi")


def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")

liste = ["a","b","c"]
liste.reverse()
print(liste)

a = [1,2,3]
b = []
for i in a:
    b.append(i**2)
b

A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A)

def islem(x, y):
    print(x - y)

islem(3)

a = [2,4,6,8]
for i in a:
    print(i**2)
    
    
sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        continue
    print(i)
    
*****************************************
    
    
#NESNE YONELİMLİ PROGRAMLAMA

#Sinif Nedir?

class VeriBilimci():
    print("Bu Bir Siniftir")

    
#Sinif Ozellikleri (Class Attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyimYili = 0
    bildigiDiller = []
    
#Siniflarin ozelliklerine erismek    
VeriBilimci.bolum    
VeriBilimci.sql
    
    
#Siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayir"
VeriBilimci.sql
    
    
#Sinif Orneklendirmesi (Instantiation)

ali = VeriBilimci()

ali.sql    
ali.deneyimYili
ali.bolum   
ali.bildigiDiller.append("Python") 
ali.bildigiDiller    
    
veli = VeriBilimci()   
veli.sql    

veli.bildigiDiller    
    
    
#Ornek Ozellikleri 
    
class VeriBilimci():
    bildigiDiller = ["R","Python"]
    bolum = ''
    sql = ''
    deneyimYili = 0
    def __init__(self):
        self.bildigiDiller = []
    
    
ali = VeriBilimci()  
ali.bildigiDiller    

veli = VeriBilimci()    
veli.bildigiDiller    
    

ali.bildigiDiller.append("Python")
ali.bildigiDiller    

veli.bildigiDiller    
veli.bildigiDiller.append("R")        
veli.bildigiDiller    

#Ornek Methodlar

class VeriBilimci():
    Calısanlar = []
    def __init__(self):
        self.bildigiDiller = []
        self.bolum = ''
    def dilEkle(self, yeniDil):        
        self.bildigiDiller.append(yeniDil)


ali = VeriBilimci()
ali.bildigiDiller
ali.bolum

veli = VeriBilimci()
veli.bildigiDiller
veli.bolum

dir(VeriBilimci)

VeriBilimci.dilEkle
VeriBilimci.dilEkle("R")

ali.dilEkle("R")
ali.bildigiDiller

veli.dilEkle("Python")
veli.bildigiDiller

#Miras Yapilari (Inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""


class DataScience(Employees):
    def __init__(self):
        self.Programming = ""
        
        
veriBilimci1 = DataScience()
veriBilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
mar1.

class Employee_yeni():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employee_yeni("a","b","c")
ali.FirstName


#Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin Bastacidir
#Birinci sinif nesnelerdir
#Yan etkisiz fonkisyonlar. (satateless, girdi-cikti)
#Yuksek seviye fonksiyonlar.
#Vektorel operasyonlar


#Yan Etkisiz Fonksiyonlar(Pure Functions)

#Ornek1:Bagimsizlik

A = 9

def impureSum(b):
    return b + A

def pureSum(a,b):
    return a + b
    
    
impureSum(6)   

pureSum(3,4) 
    
    
#Ornek2: Olumcul yan etkiler
#OOP


    
    
#Isimsiz Fonksiyonlar ( Anonymus Functions)

    
    
#Vektorel Operasyonlar (Vektorel Operations)    
#OOP
a = [1,2,3,4]    
b = [2,3,4,5]    

ab = []    

range(0,len(a))    

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
    
ab    
    
#FP    

import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])   

a*b 
    
#map & filter & reduce

liste = [1,2,3,4,5]   
    
for i in liste:
    print(i+10)
    
      
list(map(lambda x: x*10, liste))    

#filter

liste = [1,2,3,4,5,6,7,8,9,10]    

list(filter(lambda x: x % 2 == 0, liste))    
    
  
#reduce

from functools import reduce
liste = [1,2,3,4]
reduce(lambda a,b: a+b , liste) 




list(map(lambda x: x.capitalize(), ["abc","bcd","cde"]))


liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))




*****************************************

class Masa:
    en = 60S
    boy = 120
    yukseklik = 70
    renk = "kahverengi"
    
    print(en*boy)


masa1 = Masa()

print(masa1.en)
print(masa1.boy)
print(masa1.yukseklik)
print(masa1.renk)



*****************************************








































