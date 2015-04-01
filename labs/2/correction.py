#!/usr/bin/python2
import random
import threading
import time
class Correction:
    def __init__(self):
        self.x = 0
        self.cont = True
        self.corrthrd = threading.Thread(target=self.run)
        self.corrthrd.start()

    def report(self, d):
        self.x += d

    def run(self):
        while(self.cont):
            corr = 0
            if self.x < 0:
                corr = 1
            elif(self.x > 0):
                corr = -1
            if(corr != 0):
                print "Disturbance: " + str(self.x) + ", correcting by: " + str(corr)
                self.x += corr
            time.sleep(1)

    def term(self):
        self.cont = False

if __name__ == "__main__":
    random.seed()
    c = Correction()
    try:
        while True:
            direction = random.randint(0, 1)
            val = random.randint(0, 25)
            if(direction == 0):
                val = -val
            c.report(val)
            time.sleep(5)
    except KeyboardInterrupt:
        c.term()