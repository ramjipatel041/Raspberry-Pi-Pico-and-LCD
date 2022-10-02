from machine import Pin, ADC
from gpio_lcd import GpioLcd
import utime

temp_sensor = ADC(4)
conversion_factor = 3.3 / 65535
lcd = GpioLcd(rs_pin = Pin(0),
              enable_pin = Pin(1),
              d4_pin = Pin(2),
              d5_pin = Pin(3),
              d6_pin = Pin(4),
              d7_pin = Pin(5),
              num_lines = 2, num_columns = 16)

degree = bytearray([0x00, 0x06, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00])

while True:
    voltage = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (voltage - 0.706) / 0.001721
    lcd.move_to(0, 0)
    lcd.putstr("Temperature:")
    lcd.move_to(0, 1)
    lcd.putstr(str(temperature))
    lcd.move_to(8, 1)
    lcd.custom_char(0, degree)
    lcd.putchar(chr(0))
    lcd.move_to(9, 1)
    lcd.putchar("C")
    utime.sleep(0.1)
