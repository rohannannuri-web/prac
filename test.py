from machine import Pin
import time
r1  = Pin(0,Pin.OUT)
r2=Pin(1,Pin.OUT)
r3=Pin(2,Pin.OUT)
r4=Pin(3,Pin.OUT)


while True:
    r1.value(1)
    r2.value(1)
    r3.value(1)
    r4.value(1)
    print("All Open")
    time.sleep(20)
    r1.value(0)
    r2.value(0)
    r3.value(0)
    r4.value(0)
    print("All closed")
    time.sleep(20)