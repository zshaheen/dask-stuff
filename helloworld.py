from dask.distributed import Client

def square(x):
    return x**2

# start a schduler and client on the current machine
client = Client() # creates workers equal to the number of logical (not physical) cores

a = client.submit(square, 10) # returns a single Future object
b = client.map(square, range(10)) # returns a list of Future objects

# Getting the results
print a.result()
print client.gather(b) # returns [f.result() for f in b]
