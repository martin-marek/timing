import timing
from time import sleep


# test function timing
@timing.func
def dummy_func():
    sleep(0.01)
dummy_func()

# test lambda timing
timing.func(lambda: sleep(0.02))()

# test context timing
with timing.context('context label'):
    sleep(0.03)
