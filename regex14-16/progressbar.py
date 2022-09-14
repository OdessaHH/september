
#1
"""
import time   


h = "#"
for i in range(10):
    time.sleep(1)
    print(f"Progress:  {10*i}%", h*i)

print("Progress done!")
"""

#stopwatch

"""
import time
print(input("press enter to start"))
cur = time.time() # saves current time in unix

print(f"Start time: {cur}")

print(input("press enter to stop"))
anot = time.time() #another time
print(f"End time: {anot}")

time.sleep(1)
dif = anot -cur #difference between two times
print(f"Time has passed: {dif}")



"""
#countdown  
"""

import time

inp = int(input("enter integer: ")) #enter integer

start = time.ctime()                  #begin time
print("Countdown begins.", start)   #prints out begin time


for i in range(inp): #countdown loop
    time.sleep(1)
    print(inp-i)

print("Countdown ends. \n" #print all the needed results
        f"Begin time: {start}\n"
        f"End time: {time.ctime()}\n"
        f"Countdown int: {inp}")
"""