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

heart   =  bytearray([0x00, 0x0A, 0x1F, 0x1F, 0X1F, 0X0E, 0x04, 0x00])
smile   =  bytearray([0x00, 0x00, 0x0A, 0x00, 0X00, 0X11, 0x0E, 0x00])
frownie =  bytearray([0x00, 0x00, 0x0A, 0x00, 0X00, 0X00, 0x0E, 0x11])
armsUp  =  bytearray([0x04, 0x0A, 0x04, 0x15, 0X0E, 0X04, 0x04, 0x0A])
armsDown = bytearray([0x04, 0x0A, 0x04, 0x04, 0X0E, 0X15, 0x04, 0x0A])



lcd.move_to(0, 0)
lcd.putstr("I")
lcd.custom_char(0, heart)
lcd.putchar(chr(0))
lcd.putstr("Raspberry Pi ")
lcd.move_to(5, 1)
lcd.putstr("Pico")

while True:
    lcd.move_to(2, 1)
    lcd.custom_char(1, smile)
    lcd.putchar(chr(1))
    lcd.move_to(11, 1)
    lcd.custom_char(2, armsUp)
    lcd.putchar(chr(2))
    utime.sleep(1)
    lcd.move_to(2, 1)
    lcd.custom_char(3, frownie)
    lcd.putchar(chr(3))
    lcd.move_to(11, 1)
    lcd.custom_char(4, armsDown)
    lcd.putchar(chr(4))
    utime.sleep(1)
    
    