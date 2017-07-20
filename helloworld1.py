import multiprocessing
from threading import Thread
from dask.distributed import Scheduler, Worker
from tornado.ioloop import IOLoop

def square(x):
    return x**2

def start_worker():
    """Starts a single worker on the current process"""
    # Needs to be an other process or you get: RuntimeError: IOLoop is already running
    #loop = IOLoop.current()
    t = Thread(target=loop.start)
    t.daemon = True
    t.start()
    w = Worker('tcp://127.0.0.1:8786', loop=loop)
    w.start()  # choose randomly assigned port
    print 'Starting a worker'
    return


# Start the scheduler
loop = IOLoop.current()
t = Thread(target=loop.start)
t.daemon = True
t.start()
s = Scheduler(loop=loop)
s.start('tcp://:8786')
print s.workers

jobs = []
for i in range(8):
    p = multiprocessing.Process(target=start_worker)
    jobs.append(p)
    p.start()
