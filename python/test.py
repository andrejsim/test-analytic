import cfgrib
import matplotlib.pyplot as plt
from pprint import pprint

ds = cfgrib.open_dataset('../data/20190204T070000Z_TT.grb')
d = ds.t.isel()

pprint(ds.to_dict(data=False))

print(dict(ds.variables.mapping).keys())
print(ds.time.to_dict())
print(ds.time.data)
print(ds.step.data)
print(dict(ds.coords.variables.mapping).keys())

#print(ds.coords.variables)

#print(ds.data_vars.variables.mapping)

#print(ds)
#print('-----')
#print(d)

d.plot()
plt.show()

