import board
import busio
import adafruit_pca9685 as adafruit
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit.PCA9685(i2c)

#Testing the Servo Hat to make sure that the Raspberry Pi accurately detects it.

hat.frequency = 60 #60hz
led = hat.channels[10] #Targeting Pin 0

led.duty_cycle = 0xffff #Turn on the LED