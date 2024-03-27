import numpy as np
import matplotlib.pyplot as plt

"""
N = 11 # sayı adedi
x = np.linspace(0,10,N) # ile 10 arası N kadar sayılı eşit aralıkta dizi verir

y = x

plt.plot(x,y,"o--")
plt.axis("off") # eksenleri yok et
plt.show()
"""

x = [1,2,3,4]
plt.plot(x,[y**2 for y in x])
plt.show()
