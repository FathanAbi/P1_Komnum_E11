import numpy as np
import matplotlib.pyplot as plt
import math

# fungsi yang akan dicari akarnya
def f(x):
    return np.exp(x) - x -2


# metode bolzano
def bolzano(a, b, n):
    # generate x dan y untuk plot grafik fungsi
    fxlist = np.arange(-10, 10, 0.001)
    fylist = f(fxlist)
 
    # generate x dan y plot sumbu x
    xlist = np.arange(-10, 14, 2)
    ylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    

    # cek apakah batas bawah dan atas sudah benar
    if(f(a)*f(b)>=0):
        print("a dan b kurang tepat, kurva tidak memotong sumbu x antara x=a dan x=b")
        return
    
    # iterasi
    for i in range(1, n+1):
        # plot grafik fungsi
        plt.plot(fxlist, fylist, label = "f(x)")

        # plot sumbu x
        plt.plot(xlist, ylist)
        
        # metode bolzano
        c = (a+b)/2

        # title grafik
        str1 = "iterasi ke-"
        str2 = str(i)
        title = str1 + str2

        #  print dan plot hasil iterasi dan tampilkan grafik
        print("iterasi ke-", i, " = ", c)
        plt.scatter(c, f(c))
        plt.title(title)
        plt.axis([-5, 5, -2, 8])
        plt.show()

        # iterasi batas atas dan batas bawah
        if(f(a) * f(c) >= 0):
            a = c
        elif(f(c)*f(b) >= 0):
            b = c
    
    return


# driver code

# batas atas, batas bawah, dan jumlah iterasi
print("Implementasi metode bolzano untuk mencari akar persamaan f(x) = e^x - x - 2 dengan x0=0 dan x1=3, sebanyak 10 iterasi")
a = 0
b = 5
n = 10

# call function bolzano
bolzano(a,b, n)



        

    

