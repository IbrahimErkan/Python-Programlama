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























