import numpy as np
import matplotlib.pyplot as pt
from PIL import Image
x = np.arange(0,360)
y = np.sin(x*np.pi/180.0)
pt.plot(x,y)
pt.xlim(0,360)
pt.ylim(-1.2,1.2)
pt.title("func")
pt.show()
