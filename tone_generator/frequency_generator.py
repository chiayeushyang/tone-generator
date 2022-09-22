from machine import Pin, PWM, ADC
from time import sleep
from LCD_I2C import *

adc = ADC(2)

button = Pin(21, Pin.IN, Pin.PULL_DOWN)
button_set = Pin(22, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(18))

lcd = LCD(sda=2, scl=3)  # Create LCD object with LCD's sda pin connected to PICO's sda pin 2, LCD's sck pin connected to Pico's scl pin 3
lcd.clear()
lcd.set_cursor(0,0)
lcd.set_cursor(0,1) 
lcd.write("#Cytron Festival")
sleep(1)
lcd.write("Freq = " + "set GP22")
lcd.set_cursor(0,1) 
lcd.write("#Cytron Festival")

    
while True:   
    value = adc.read_u16()
    str_value = str(round(value / 7))
    frequency = str_value

    first = frequency
    sleep(0.01)
    second = frequency

    while button_set.value() == False:
        value = adc.read_u16()
        str_value = str(round(value / 7))
        frequency = str_value
        lcd.clear()
        lcd.set_cursor(2,0)
        lcd.write("Freq = " + frequency)
        sleep(1) 
    
    while button_set.value() == True:
        lcd.clear()
        lcd.set_cursor(0,0)
        lcd.set_cursor(0,1) 
        lcd.write("#Cytron Festival")
        sleep(1)
        lcd.write("Freq = " + frequency)
        lcd.set_cursor(0,1) 

        while button.value() == False:
            buzzer.duty_u16(1800)
            buzzer.freq(round(value / 7))

        else :
            buzzer.duty_u16(0)
        
        sleep(1.5)
