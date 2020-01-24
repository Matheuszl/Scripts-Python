from scipy import interpolate as np
import matplotlib.pyplot as pyplot

x = np.linspace(0, 10, num=11, endpoint = True)
y = np.cos(-x**2/9.0)
x1 = np.linspace(0, 10, num=41, endpoint = True)

fn = interpolate.interp1d(x, y, kind='valor')
fn2 = interpolate.interp1d(x, y, kind='previous')
fn3 = interpolate.interp1d(x, y, kind='next')


plt.show()