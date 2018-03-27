import time

def time_count(function):
    start_time = time.time()
    print(start_time)
    function
    end_time = time.time()
    print(end_time)
    print(end_time-start_time)
