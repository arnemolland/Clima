from sense_hat import SenseHat

sense = SenseHat()

while True:

    sense.clear()
    pressure = sense.get_pressure()
    sense.show_message('p: {0}'.format(pressure))

    sense.clear()
    temp = sense.get_temperature()
    sense.show_message('t: {0}'.format(temp))

    sense.clear()
    humidity = sense.get_humidity()
    sense.show_message('h: {0}'.format(humidity))


