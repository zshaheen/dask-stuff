import subprocess
import time
import sys
import multiprocessing
from dask.distributed import Client

def square(x):
    return x**2

def start_scheduler(output):
    '''Start the scheduler, and return the address and port used'''
    # proc = subprocess.Popen('srun -N 1 dask-scheduler', shell=True, stdout=subprocess.PIPE)
    proc = subprocess.Popen('dask-scheduler', stdout=subprocess.PIPE)
    ls = proc.stdout.readlines()
    print ls
    print 'STARTING THE WHILE LOOP'
    #print type(proc.stdout)
    #print dir(proc.stdout)
    #while True:
        # print 'True'

    
    for line in proc.stdout.readlines():
        print 'line + ' + line
    #for line in iter(proc.stdout.readline, ''):
        if 'tcp' in line:
            print line
            print 'IM FUCKING DONE'
            break
    '''
    for line in iter(proc.stdout.readline, ''):
        sys.stdout.write(line)
        if 'tcp' in line:
            output['output'] = line
    '''
    #out, _ = proc.communicate()
    #print 'SCHEDULER OUTPUT'
    #print out
    #print 'SCHEDULER OUTPUT'
    #output['output'] = out

def start_workers(nprocs, scheduler_addr):
    '''Start n workers on the current machine via Slurm at scheduler schedular_addr'''
    # cmd = 'srun -N {} dask-worker 128.15.245.24:8786 --nprocs {} --no-nanny'
    cmd = 'dask-worker {} --nprocs {} --no-nanny'
    subprocess.Popen(cmd.format(scheduler_addr, nprocs))

# start the scheduler on another process so it doesn't hang the current one
# this is because the command `dask-schduler` never quits
my_dict = {}
try:
    p = multiprocessing.Process(target=start_scheduler, args=(my_dict,))
    p.start()
except:
    p.terminate()
time.sleep(3)
#start_scheduler(my_dict)
# start_workers(multiprocessing.cpu_count())

client = Client('128.15.245.24:8786') # creates workers equal to the number of logical (not physical) cores
#print client.scheduler_info()
#client.restart()
client.close()
p.terminate()
print my_dict
print 'DONE!'

