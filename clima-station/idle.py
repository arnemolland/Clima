from random import randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

while True:
    x = randint(0,7)
    y = randint(0,7)
    r = randint(100,255)
    g = randint(100,255)
    b = randint(100,255)
    sense.set_pixel(x, y, r, g, b)
    sense.set_pixel(randint(0,7), randint(0,7), 0, 0, 0)
    sleep(0.1)
