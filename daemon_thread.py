# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, they stay alive until task is complete

#                 e.g background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
  print()
  count = 0
  while True:
    time.sleep(1)
    count += 1
    print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)       # sets thread as daemon thread
# or
# x.setDaemon(True)                                   # also sets thread to a daemon thread
x.start()

# check if thread is daemon
print(x.isDaemon())

answer = input("Do you wish to exit?")