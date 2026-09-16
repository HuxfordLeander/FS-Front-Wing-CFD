import numpy as np
import matplotlib.pyplot as plt
c=0.20
t=0.12
n=101
beta=np.linspace(0, np.pi, n)
print(beta[:5])
x= 0.5*c*(1 - np.cos(beta))
x_over_c=x/c
term1=0.2969*np.sqrt(x_over_c)
print(term1[:5])
print(x[:5])
term2= -0.1260*x_over_c
print(term2[:5])
partical=term1+term2
print(partical[:5])
term3= -0.3516*x_over_c**2
print(term3[:5])
partial3= term1+term2+term3
print(partial3[:5])
term4= 0.2843*x_over_c**3
print(term4[:5])
partial4= term1+term2+term3+term4
print(partial4[:5])
term5=-0.1015*x_over_c**4
print(term5[:5])
shape=term1+term2+term3+term4+term5
print(shape[:5])
yt=5*t*c*shape
y_upper = yt
y_lower = -yt
print(yt[:5])
uiuc_data=np.loadtxt('/Users/huxford/Desktop/n0012.dat.txt',skiprows=2)
print(uiuc_data[:5])
uiuc_x=uiuc_data[:,0]
uiuc_y=uiuc_data[:,1]
uiuc_x_m=uiuc_x*c
uiuc_y_m=uiuc_y*c
plt.plot(x, y_upper,label='Python Upper')
plt.plot(x, y_lower,label='Python Lower')
plt.scatter(uiuc_x_m, uiuc_y_m, s=10, label='UIUC Data')
plt.axis('equal')
plt.legend()
uiuc_x_upper=uiuc_x[:66]
uiuc_y_upper=uiuc_y[:66]

shape_uiuc = (
    0.2969*np.sqrt(uiuc_x_upper)
    -0.1260*uiuc_x_upper
    -0.3516*uiuc_x_upper**2
    +0.2843*uiuc_x_upper**3
    -0.1015*uiuc_x_upper**4
)

python_y_upper=5*t*shape_uiuc

error=python_y_upper-uiuc_y_upper
max_error=np.max(np.abs(error))

print("Maximum error =", max_error)

x_upper_ordered=x[::-1]
y_upper_ordered=y_upper[::-1]

x_lower_ordered= x[1:]
y_lower_ordered=y_lower[1:]

print(x_upper_ordered[:5])

x_airfoil=np.concatenate((x_upper_ordered, x_lower_ordered))
y_airfoil=np.concatenate((y_upper_ordered, y_lower_ordered))

print(x_airfoil[:5])
print(x_airfoil[-5:])

airfoil_coordinates=np.column_stack((x_airfoil, y_airfoil))

np.savetxt(
    '/Users/huxford/Desktop/naca0012_generated.txt',
    airfoil_coordinates,
    fmt='%.8f'
)

plt.show()