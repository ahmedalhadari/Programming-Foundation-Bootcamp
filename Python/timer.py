# D-C2: Timer
# -----------
# Write a decorator `timer` that prints how many seconds the
# wrapped function took.

# Apply to `slow()` which does `time.sleep(2)` and returns "done".
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        time_took = time.time() - start
        print (f"It Tooks {time_took} Seconds")
        return result
    return wrapper

@timer
def slow():
    time.sleep(2)
    return "Done"
print (slow())