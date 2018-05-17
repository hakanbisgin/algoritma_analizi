import time
import numpy as np
import matplotlib.pyplot as plt
import math

def ekrana_yaz(deneme,dagilim):
    plt.plot(deneme,dagilim,linewidth=4)
    plt.plot(deneme,dagilim,linewidth=4)

    plt.title('Cizilen fonksiyon')
    plt.ylabel('dagilim')
    plt.xlabel('deneme')
    plt.show()

def b_katsayi(n,p,k):
    return (p**k)*((1-p)**(n-k))

def b_secim(n,k):
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    
def bernoulli():
    N = input("Deneme sayısı girin: ")
    p = input("başarı olasılığı girin: ")
    q = 1 - p
    x = []
    y = []
        
    for k in range(N):
        olasilik = b_katsayi(N,p,k) * b_secim(N,k)
        y.append(olasilik)
        x.append(k)
    
    ekrana_yaz(x,y)
    
def negat():
    N1 = input("son basari girin: ")
    t = input("toplam basari: ")
    p = input("başarı olasılığı girin: ")
    q = 1 - p
    
    for N in range(t,N1):
        olasilik = (b_secim(N-1,t-1) * p**(t-1) * q**(N-t)) * p
        x.append(N)
        y.append(olasilik)
    
    ekrana_yaz(x,y)
    
def geometrik():
    N = input("Deneme sayısı girin: ")
    p = input("başarı olasılığı girin: ")
    q = 1-p
    x=[]
    y=[]
    
    for k in range(N):
        x.append(k)
        y.append(p*(q**(N-1)))
        
    ekrana_yaz(x,y)

def poi_olasilik(x,lam):
    return ((lam**x)*exp(-lam))/math.factorial(x)

def poi_capraz(olusma,lamb,sure):
    return (sure*lamb)/olusma

def poisson():
    olusma = input("olusma sıklıgı: ")
    lamb = input("başarı olasılığı girin: ")
    sure = input("sure girin: ")
    x=[]
    y=[]
    
    lamb1 = poi_capraz(olusma,lamb,sure)
    
    k = 0
    olasilik = 1
    while (olasilik>0.001):
        olasilik = poi_olasilik(k,lamb1)
        x.append(olasilik)
        y.append(k)
        k += 1
    
    ekrana_yaz(x,y)

def hypergeo():
    n1 = input("ornek sayisi: ")
    M1 = input("basari populasyonu: ")
    N = input("populasyon boyutu: ")
    x=[]
    y=[]
    
    for k in range(n1):
        olasilik = b_secim(M1,k) * b_secim(N-M1,n1-k) / b_secim(N,n1)
        x.append(olasilik)
        y.append(k)
    
    ekrana_yaz(x,y)
