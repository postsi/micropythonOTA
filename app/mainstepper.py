# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from machine import Pin, I2C, SoftI2C
import time
from esp32 import Partition
import ssd1306
import adafruit_sht31d
#import base_stepper
from AccelStepper import AccelStepper



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def read_temp():
    try:
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        sensor = adafruit_sht31d.SHT31D(i2c)
        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(2)
        i2c1 = SoftI2C(scl=Pin(22), sda=Pin(19), freq=100000)
        sensor1 = adafruit_sht31d.SHT31D(i2c1)
        print("\nTemperature1: %0.1f C" % sensor1.temperature)
        print("Humidity1: %0.1f %%" % sensor1.relative_humidity)

    except:
        print("Temp error")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    print_hi('PyCharm')
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    oled.text('Hello, World 1!', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Hello, World 3!', 0, 20)

    oled.show()
    print("loading stepper")
    stepper = AccelStepper(1,18,5)
    stepper.enable_outputs()
    stepper.set_max_speed(10000)
    stepper.set_acceleration(5000)
    stepper.move(8000)
    while stepper.run():
        stepper.run()
    stepper.move(-8000)
    while stepper.run():
        stepper.run()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
