# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:13:31 2021

@author: Bani Yasir
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! satu satu akhirnya bisa</p>"




def odd(n):
 hasil = n % 2
 if hasil != 0:
     hasilnya=True
 else:
     hasilnya=False
 return hasilnya


def pelangi(warna):
  print(f'Salah satu warna pelangi adalah {warna}')



class Kucing():
    def _init_(self):
        print("Anggora bulu putih, mata biru laut")
tampilkan = Kucing()



class Kelulusan():
 
    def __init__(self, masukan_nama):
        self.nama = masukan_nama
 
    def nilai(self, nilai):
        if nilai >= 70:
            print(self.nama,'Selamat anda lulus dengan nilai',nilai)
        else:
            print(self.nama,'Maaf anda tidak lulus dengan nilai',nilai)
 
mhs=Kelulusan("DHANTI")
print(mhs.nama)
mhs.nilai(90)
      
      