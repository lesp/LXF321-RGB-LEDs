import time
from machine import Pin, PWM

r_pwm = PWM(Pin(13))
g_pwm = PWM(Pin(14))
b_pwm = PWM(Pin(15))
r_pwm.freq(1000)
g_pwm.freq(1000)
b_pwm.freq(1000)
# Use a # to comment out one of the pwm.duty_u16 lines for each for loop. For example
# Do this for both for loops #g_pwm.duty_u16(duty) and then save and run the code.
# The RGB LED will glow purple, by mixing the red and blue LEDs inside the RGB LED.

for duty in range(65025):
    r_pwm.duty_u16(duty)
    #g_pwm.duty_u16(duty)
    b_pwm.duty_u16(duty)
    time.sleep(0.0001)
for duty in range(65025, 0, -1):
    r_pwm.duty_u16(duty)
    #g_pwm.duty_u16(duty)
    b_pwm.duty_u16(duty)
    time.sleep(0.0001)