import matplotlib.pyplot as plt
import numpy as np

r=4.5 #radius of the fuel pin
mesh_size=1
x=np.arange(-r-10,r+10,mesh_size)
y=np.arange(-r-10,r+10,mesh_size)
theta=np.arange(0,2*np.pi,0.1)


X,Y=np.meshgrid(x,y)
for i in range(len(x)):
    plt.plot(X[i],Y[i],color='b')
    plt.plot(Y[i],X[i],color='b')

x=r*np.cos(theta)
y=r*np.sin(theta)
plt.plot(x,y,color='b')

x_new=[]
y_new=[]

for i in range (len(x)):
    for j in range (len(x)):
        if y[i]**2+x[j]**2>r**2:
            if x[j]<0:
                dx=-np.sqrt(r**2-y[i]**2)
            else:
                dx=np.sqrt(r**2-y[i]**2)
            x_new.append(x[j]-dx)
        else:
            x_new.append(x[j])
    for k in range (len(x)):
        if y[k]**2+x[i]**2>r**2:
            if y[k]<0:
                dy=-np.sqrt(r**2-x[i]**2)
            else:
                dy=np.sqrt(r**2-x[i]**2)
            y_new.append(y[k]-dy)
        else:
            y_new.append(y[k])

  
plt.scatter(x_new,y_new,color='red') 
