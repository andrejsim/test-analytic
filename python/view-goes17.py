import xarray
from pprint import pprint
import json
import matplotlib.pyplot as plt
import numpy as np

# https://registry.opendata.aws/

#http://edc.occ-data.org/goes16/python/#initial-radiance-plot


def read_metadata_and_write_to_json(filename):
    ds = xarray.open_dataset(filename)
    outname =filename.replace(".nc",".metadata.json")
    with open(outname, 'w') as outfile:
        json.dump(ds.to_dict(data=False), outfile, indent=4)

    return ds

g17nc = read_metadata_and_write_to_json("../data/OR_ABI-L1b-RadC-M3C01_G17_s20183381642189_e20183381644502_c20183381644536.nc")

read_metadata_and_write_to_json("../data/OR_GLM-L2-LCFA_G17_s20190850300000_e20190850300200_c20190850300325.nc")

plt.figure(1)

radiance = g17nc.variables['Rad'][:]
fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(radiance, cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
cb.set_label('Radiance (W m-2 sr-1 um-1)')
plt.show()

print(g17nc.variables.keys())

# Define some constants needed for the conversion. From the pdf linked above
Esun_Ch_01 = 726.721072
Esun_Ch_02 = 663.274497
Esun_Ch_03 = 441.868715
d2 = 0.3
# Apply the formula to convert radiance to reflectance
ref = (radiance * np.pi * d2) / Esun_Ch_02

# Make sure all data is in the valid data range
ref = np.maximum(ref, 0.0)
ref = np.minimum(ref, 1.0)
# Plot reflectance
fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(ref, vmin=0.0, vmax=1.0, cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_label('Reflectance')
plt.show()


# dipper
# https://github.com/occ-data/goes16-jupyter