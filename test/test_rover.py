import pytest
from unittest.mock import patch
from hadrian.connections.rover import Rover

@pytest.fixture
def rover():
    return Rover()

def test_start_motor_left(rover):
    with patch('RPi.GPIO.output') as mock_output, patch('RPi.GPIO.PWM') as mock_pwm:
        rover.start_motor_left(speed=1.0, direction='FORWARD')
        mock_pwm.assert_called_once()
        mock_output.assert_any_call(rover.pins['ain2'], 1)
        mock_output.assert_any_call(rover.pins['ain1'], 0)

def test_start_motor_right(rover):
    with patch('RPi.GPIO.output') as mock_output, patch('RPi.GPIO.PWM') as mock_pwm:
        rover.start_motor_right(speed=1.0, direction='BACKWARD')
        mock_pwm.assert_called_once()
        mock_output.assert_any_call(rover.pins['bin1'], 0)
        mock_output.assert_any_call(rover.pins['bin2'], 1)

def test_stop_motor_left(rover):
    with patch('RPi.GPIO.output') as mock_output:
        rover.stop_motor_left()
        mock_output.assert_any_call(rover.pins['ain1'], 0)
        mock_output.assert_any_call(rover.pins['ain2'], 0)

def test_stop_motor_right(rover):
    with patch('RPi.GPIO.output') as mock_output:
        rover.stop_motor_right()
        mock_output.assert_any_call(rover.pins['bin1'], 0)
        mock_output.assert_any_call(rover.pins['bin2'], 0)

def test_turn(rover):
    with patch('time.sleep') as mock_sleep:
        rover.turn(degrees=90, direction='CLOCKWISE')
        mock_sleep.assert_called_once_with(0.45)  

def test_move(rover):
    with patch('time.sleep') as mock_sleep:
        rover.move(metres=1.0, direction='FORWARD')
        mock_sleep.assert_called_once_with(2)  
