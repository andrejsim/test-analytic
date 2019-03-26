from dask.distributed import Client, progress

# pip install dask[complete]
client = Client(processes=False,
                threads_per_worker=4,
                n_workers=1,
                memory_limit='2GB')

print(client)

import dask.array as da
x = da.random.random((10000, 10000), chunks=(1000, 1000))
y = x + x.T
z = y[::2, 5000:].mean(axis=1)
print(z.compute())

y.sum().compute()


