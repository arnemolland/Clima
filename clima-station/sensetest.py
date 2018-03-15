from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.clear()
    pressure = sense.get_pressure()
    sense.show_message('p: ')
    sense.show_message('{:.4}'.format(pressure))

    sense.clear()
    temp = sense.get_temperature()
    sense.show_message('t: ')
    sense.show_message('{:.4}'.format(temp))

    sense.clear()
    humidity = sense.get_humidity()
    sense.show_message('h: ')
    sense.show_message('{:.4}'.format(humidity))


