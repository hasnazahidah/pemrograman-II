# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:19:00 2021

@author: Bani Yasir
"""

class Kelulusan():
 
    def __init__(self, masukan_nama):
        self.nama = masukan_nama
 
    def nilai(self, nilai):
        if nilai >= 50:
            print(self.nama,'Selamat anda lulus dengan nilai',nilai)
        else:
            print(self.nama,'Maaf anda tidak lulus dengan nilai',nilai)
 
mhs=Kelulusan("Hasna Zahidah")
print(mhs.nama)
mhs.nilai(100)