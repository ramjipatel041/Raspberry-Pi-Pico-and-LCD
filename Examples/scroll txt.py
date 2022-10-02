from machine import Pin
from gpio_lcd import GpioLcd
import utime

lcd = GpioLcd(rs_pin = Pin(0),
              enable_pin = Pin(1),
              d4_pin = Pin(2),
              d5_pin = Pin(3),
              d6_pin = Pin(4),
              d7_pin = Pin(5),
              num_lines = 2, num_columns = 16)
while True:
    for i in range(0,11):
        lcd.clear()
        lcd.move_to(i, 0)
        lcd.putstr("hello")
        utime.sleep(0.2)
    utime.sleep(0.001)
    for j in range(11,-1,-1):
        lcd.clear()
        lcd.move_to(j, 0)
        lcd.putstr("hello")
        utime.sleep(0.2)
    utime.sleep(0.001)
    




