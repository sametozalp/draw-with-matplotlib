import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5) # dizi verir 0 ile 4 arası
y = x

plt.plot(x,y,"o--")  # o, o-, o-- # çizim şekilleri
plt.plot(x,-y)
plt.plot(-x,y,"o")
plt.title("y=x, y=-x")
plt.show()
