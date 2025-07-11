from machine import Pin, PWM
import time


led2 = PWM(Pin(2))
led2.freq(1000)


while True:  #while True：#Control the overall brightness(1,Slowly change from bright to non-bright;2,Slowly change from non-bright to bright)
   
    # 1，Slowly change from non-bright to bright
    for i in range(0, 1024, 1):
        led2.duty(i)
        time.sleep_ms(2)
    # 2,Slowly change from bright to non-bright
    for i in range(1023, -1, -1):
        led2.duty(i)
        time.sleep_ms(2)
        
        
    
 

