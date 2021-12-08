import numpy as np
import matplotlib.pyplot as plt

m=0
x = []
y = []
for i in range (2):
    print('x' , i+1 , ' : ',end='')
    p = int(input(' '))
    x.append(p)
for i in range (2):
    print('y' , i+1 , ' : ',end='')
    p = int(input(' '))
    y.append(p)
xpoint,ypoint = [],[]
if x[0]==x[1]:
    xpoint = np.append(x,x[0])
    ypoint = np.append(y,y[1]+1)
elif y[0]==y[1]:
    xpoint = np.append(x,(x[0])+1)
    ypoint = np.append(y,y[1]+1)
else:
    if m<1:
        m = (y[1]-y[0])/(x[1]-x[0])
        n = abs(x[1]-x[0])
        x2 = x[0]
        i = 1
        while i <= n+1:
            y2 = y[0]+m*(x2-x[0])
            xpoint.append(x2)
            ypoint.append(round(y2))
            x2+=1
            i+=1
    else:
        m = (x[1]-x[0])/(y[1]-y[0])
        n = abs(y[1]-y[0])
        y2 = y[0]
        i = 1
        while i <= n+1:
            x2 = x[0]+m*(y2-y[0])
            ypoint.append(y2)
            xpoint.append(round(x2))
            y2+=1
            i+=1
np.array(xpoint)
np.array(ypoint)
plt.plot(x,y,'o')
print('Penghubung Garis: ',end=' ')
for i in range (len(ypoint)):
    if i < len(ypoint)-1:
        print('(',xpoint[i],',', ypoint[i],end='),')
    else:
        print('(',xpoint[i],',',ypoint[i],end=')')
print()

plt.show()