import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#function makes a mandelbroth set with n amount of iterations using the complex value x+yj (n,x,y)
def mandelbroth(n,x,y):
    c = complex(x,y)
    a=np.array([0])
    for i in range(n):
        a=np.append(a,a[i]**2+c)
    return a

#function draws a mandelbroth graph of size (x,y)
def draw_mandelbroth(x,y):
    a=np.array([1]*x*y).reshape(x,y)
    ii=-1
    for n1 in np.arange(-1.5,0.5,1/y*2):
        ii+=1
        i=-1
        for n2 in np.arange(-1,1,1/x*2):
            i+=1
            if abs(mandelbroth(101,n1,n2)[100]) < 2:
                a[i,ii]=0
    plt.imshow(a)


draw_mandelbroth(200,200)