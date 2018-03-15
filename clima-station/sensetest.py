from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.show_message("Hello world", scroll_speed=0.2, text_colour=[255, 255, 0])
