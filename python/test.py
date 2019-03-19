import cfgrib
import matplotlib.pyplot as plt


ds = cfgrib.open_dataset('../data/20190204T070000Z_TT.grb')
d = ds.t.isel()
print(d)
d.plot()
plt.show()

