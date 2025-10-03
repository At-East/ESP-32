from machine import Pin, PWM
import time

#创建引脚对象
led_r = Pin(5, Pin.OUT)
led_g = Pin(18, Pin.OUT)
led_b = Pin(19, Pin.OUT)

#创建PWM对象
pwm_led_r = PWM(led_r)
pwm_led_r.freq(100)
pwm_led_r.duty(1023 - int(255 / 255 * 1023))

pwm_led_g = PWM(led_g)
pwm_led_g.freq(100)
pwm_led_g.duty(1023 - int(200 / 255 * 1023))

pwm_led_b = PWM(led_b)
pwm_led_b.freq(100)
pwm_led_b.duty(1023 - int(2 / 255 * 1023))

print("sleep 1...")
time.sleep(10)

