import time

def time_execute(timevalue):
    def wrapper():
        start_time=time.time()
        timevalue()
        print(time.time()-start_time)
    return wrapper
@time_execute
def example():
    print("The time of execuation is as follows")
example()






""" start_time=time.time()
total=0
for i in range(0,10001):
    total+=i
print(total)
print(time.time()-start_time) """





