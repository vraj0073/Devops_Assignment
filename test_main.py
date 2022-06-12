import main
import pytest

def test_car_on_hold():
	obj = main.Car()
	assert obj.isMoving() == False

def test_car_moving():
	obj = main.Car()
	obj.moveForward()
	assert obj.isMoving() == True

def test_car_Reverse():
	obj = main.Car()
	obj.moveBackward()
	assert obj.isMoving() == True

def test_car_Stop():
	obj = main.Car()
	obj.stop()
	assert obj.isMoving() == False
