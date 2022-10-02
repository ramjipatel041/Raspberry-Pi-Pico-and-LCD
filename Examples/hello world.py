from machine import Pin
from gpio_lcd import GpioLcd
import utime

#Configure the Gpio pin of the Raspberry pi pico
lcd = GpioLcd(rs_pin = Pin(0),
              enable_pin = Pin(1),
              d4_pin = Pin(2),
              d5_pin = Pin(3),
              d6_pin = Pin(4),
              d7_pin = Pin(5),
              num_lines = 2, num_columns = 16)
#print the string on the display
lcd.putstr('hello world!')

#create an infinite loop 
while True:
    for i in range(1000):
        lcd.move_to(0,1)    #set the curstor location to (0,1)
        lcd.putstr(str(i))  #convert the i into string and print it
        utime.sleep(0.5)    #create a delay of 0.5 second

