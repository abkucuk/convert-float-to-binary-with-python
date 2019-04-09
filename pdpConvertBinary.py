#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 02:39:57 2019

@author: ahmetburakmac
"""

kalanlar = []
vSonrakiKalanlar = []
sonKalanlar = []
cevap32bitlik = []
def virguldenSonrakiKismiBinaryCevir(sayi,kalanyer):
    for i in range(kalanyer):
        sayi = (sayi*2)
        vSonrakiKalanlar.append(int(sayi/10))
        sayi = sayi % 10
    return
def virguldenOncekiSayiyiBinaryCevir(sayi,myArray):
    while sayi > 1: 
        kalan = sayi % 2
        bolum = sayi / 2
        sayi = bolum
        myArray.append(int(kalan))
        if sayi == 1:
            myArray.append(1)
    return
sayi = 162.4
print(sayi)
stringSayi = str(sayi)
virgulden_sonra= int(stringSayi.split(".")[1])
virgulden_once = int(stringSayi.split(".")[0])
print(virgulden_once)
print(virgulden_sonra)
print("----------------")
virguldenOncekiSayiyiBinaryCevir(virgulden_once,kalanlar)
print("virgulden once")
kalanlar.reverse()
print(kalanlar)
print("----------------")
virguldenSonrakiKismiBinaryCevir(virgulden_sonra,(22-len(kalanlar)))
print("virgulden sonra")
vSonrakiKalanlar.reverse()
print(vSonrakiKalanlar)
yeniSayi = (2**7) + (len(kalanlar) - 1) - 1
print("yeni sayı :")
print(yeniSayi)
print("----------------")
virguldenOncekiSayiyiBinaryCevir(yeniSayi,sonKalanlar)
print("exponansiyel işlem sonucu kalanlar :")
sonKalanlar.reverse()
print(sonKalanlar)
if sayi > 0:
    cevap32bitlik.append(0)
else:
    cevap32bitlik.append(1)

cevap32bitlik.extend(sonKalanlar)
kalanlar.pop(0)
cevap32bitlik.extend(kalanlar)
cevap32bitlik.extend(vSonrakiKalanlar)
print("----------------")
print("----------------")
print("32 bitlik cevap :")
print(cevap32bitlik)
