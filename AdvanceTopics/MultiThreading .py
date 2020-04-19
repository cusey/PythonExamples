#python 3.5.2

from threading import Thread
import time

def timer(name, delay, repeat):

    print("Timer: " + name + "Started")
    while repeat > 0:
        time.sleep(delay)
        print(name + " : " + str(time.ctime(time.time())))
        repeat -= 1
        
    print("Timer: " + name + "Completed")
    
def Main():

    t1 = Thread( target=timer, args=("Timer1", 1, 5))
    t2 = Thread( target=timer, args=("Timer2", 2, 5))
    
    t1.start()
    t2.start()
    
    print("Main Completed")


if __name__ == '__main__':
    Main()
    
'''
OUTPUT:

Timer: Timer1 Started
Timer: Timer2 Started
Main Completed
Timer1 : Mon Sep 24 16:09:41 2018
Timer1 : Mon Sep 24 16:09:42 2018
Timer2 : Mon Sep 24 16:09:42 2018
Timer1 : Mon Sep 24 16:09:43 2018
Timer1 : Mon Sep 24 16:09:44 2018
Timer2 : Mon Sep 24 16:09:44 2018
Timer1 : Mon Sep 24 16:09:45 2018
Timer: Timer1 Completed
Timer2 : Mon Sep 24 16:09:46 2018
Timer2 : Mon Sep 24 16:09:48 2018
Timer2 : Mon Sep 24 16:09:50 2018
Timer: Timer2 Completed

'''