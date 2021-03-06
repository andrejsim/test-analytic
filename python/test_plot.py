import cfgrib
import matplotlib.pyplot as plt
from pprint import pprint

ds = cfgrib.open_dataset('../data/20190204T070000Z_TT.grb')
d = ds.t #.isel()

pprint(ds.to_dict(data=False))

''' all variables listed'''
print(dict(ds.variables.mapping).keys())

''' time as a dict listed'''
print(ds.time.to_dict())

''' all coordinates without central data variable'''
for k in dict(ds.coords.variables.mapping):
    print(k)
    print(ds.variables[k].data)

''' key variable is shown t'''
for k in dict(ds.data_vars.variables.mapping).keys():
    print(k)

#print(ds)
#print('-----')
#print(d)
plt.figure(1)
fig, axes = plt.subplots(nrows=2)

# plot1
d.sel().plot(ax=axes[0])

#plot2
#d.sel(longitude=slice(0, 30), latitude=slice(40, 60)).plot(ax=axes[1])

#plot3
d.sel(longitude=slice(-90, 90), latitude=slice(-90, 90)).plot(ax=axes[1])


plt.tight_layout()
plt.show()

