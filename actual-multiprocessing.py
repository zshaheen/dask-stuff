import dask.bag
import dask.multiprocessing 

class Parameters(object):
    def __init__(self, x):
        self.x = x

def give_x(p):
    return p.x

params = [Parameters(i) for i in range(0, 3)]

bag = dask.bag.from_sequence(params)

num_workers = 4
with dask.set_options(get=dask.multiprocessing.get):
    if num_workers:
        results = bag.map(give_x).compute(num_workers=num_workers) 
    else:
        # num of workers is defaulted to the number of processes
        results = bag.map(give_x).compute()
print results 
