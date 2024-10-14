from enum import Enum

import RPi.GPIO as GPIO
import time

class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2

class TurnDirection(Enum):
    CLOCKWISE = 1
    ANTICLOCKWISE = 2

CONTROL_FREQUENCY = 100000

def cleanup():
    GPIO.cleanup()

class Rover:
    def __init__(self):
        # Set up pins. Note we're going by physical pin numbers, not
        # the GPIO numbers.
        self.pins: dict[str, int] = {
            "ain1": 11,
            "ain2": 13,
            "bin1": 29,
            "bin2": 31,
            "stby": 37,
            "pwma": 33,
            "pwmb": 35,
        }

        # Set so we're using physical pin numbers.
        GPIO.setmode(GPIO.BOARD)

        # All these pins are set as outputs.
        for _, pin_number in self.pins.items():
            GPIO.setup(pin_number, GPIO.OUT)

        # Take the motor driver off standby and initialize the pwm pins
        self.enable()
        self.pwma = GPIO.PWM(self.pins["pwma"], CONTROL_FREQUENCY)
        self.pwmb = GPIO.PWM(self.pins["pwmb"], CONTROL_FREQUENCY)

    def start_motor_left(self, speed: float = 1.0, direction: Direction = Direction.FORWARD):
        self.pwma.start(100 * speed)

        match direction:
            case Direction.FORWARD:
                GPIO.output(self.pins["ain2"], GPIO.HIGH)
                GPIO.output(self.pins["ain1"], GPIO.LOW)
            case Direction.BACKWARD:
                GPIO.output(self.pins["ain2"], GPIO.LOW)
                GPIO.output(self.pins["ain1"], GPIO.HIGH)

    def start_motor_right(self, speed: float = 1.0, direction: Direction = Direction.FORWARD):
        self.pwmb.start(100 * speed)

        match direction:
            case Direction.FORWARD:
                GPIO.output(self.pins["bin1"], GPIO.HIGH)
                GPIO.output(self.pins["bin2"], GPIO.LOW)
            case Direction.BACKWARD:
                GPIO.output(self.pins["bin1"], GPIO.LOW)
                GPIO.output(self.pins["bin2"], GPIO.HIGH)

    def stop_motor_left(self):
        GPIO.output(self.pins["ain1"], GPIO.LOW)
        GPIO.output(self.pins["ain2"], GPIO.LOW)
        self.pwma.stop()

    def stop_motor_right(self):
        GPIO.output(self.pins["bin1"], GPIO.LOW)
        GPIO.output(self.pins["bin2"], GPIO.LOW)
        self.pwmb.stop()

    def turn(self, degrees: int, direction: TurnDirection = TurnDirection.CLOCKWISE):
        match direction:
            case TurnDirection.CLOCKWISE:
                self.start_motor_left()
            case TurnDirection.ANTICLOCKWISE:
                self.start_motor_right()
        
        time.sleep(degrees / 200)

        self.stop_motor_left()
        self.stop_motor_right()


    def move(self, metres: float = 1.0, direction: Direction = Direction.FORWARD):
        self.start_motor_left(direction=direction)
        self.start_motor_right(direction=direction)

        time.sleep(metres * 2)

        self.stop_motor_left()
        self.stop_motor_right()

    def enable(self, enabled: bool = True):
        if enabled:
            GPIO.output(self.pins["stby"], GPIO.HIGH)
        else:
            GPIO.output(self.pins["stby"], GPIO.LOW)
