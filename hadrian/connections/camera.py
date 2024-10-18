import time
from picamera2 import Picamera2
from dataclasses import dataclass

@dataclass
class Camera:
    save_path: str

    def take_image(self):
        """Take photo on RPi camera module, save to save_path."""
        picam2 = Picamera2()
        picam2.start()
        time.sleep(1)  # Allow time for the camera to adjust
        picam2.capture_file(self.save_path)
        picam2.stop()