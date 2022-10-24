# thread = a flow of execution. Like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock),
#               allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

def eat():
  time.sleep(3)
  print("You eat breakfast")

def drink():
  time.sleep(4)
  print("You drink tea")

def study():
  time.sleep(5)
  print("You finish studying")


x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat()
# drink()
# study()

# active count of threads running in our program
print(threading.active_count())
# print a list of all threads that are running
print(threading.enumerate())

print(time.perf_counter())