from functools import wraps
import tracemalloc
import time 
def measure_performance(func):
    """Measure performance of a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("executing before")
        start_time = time.perf_counter()
        tracemalloc.start()
        func()
        snapshot = tracemalloc.take_snapshot()
        print("executing after")
        end_time = time.perf_counter()
        print("elapsed time",end_time-start_time)
        for stat in snapshot.statistics("lineno"):
            print(stat)
        tracemalloc.stop()
    return wrapper
@measure_performance
def make_list1():
    my_list = list(range(100000))
make_list1()    
@measure_performance
def make_list2():
    my_list = [l for l in range(100000)]
make_list2()    
@measure_performance
def make_list3():
    my_list = []
    for item in range(100000):
        my_list.append(item)
make_list3()
@measure_performance
def make_list4():
    my_list = []
    for item in range(100000):
        my_list = my_list + [item]
make_list4()        
