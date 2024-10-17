from picamera2 import Picamera2
import time

# Takes an image and stores it at /home/pi/Projects/hadrian/current_image.jpg
def take_image():
  picam2 = Picamera2()
  picam2.start()
  time.sleep(2)
  picam2.capture_file("/home/pi/Projects/hadrian/current_image.jpg")
