print("Starting...")

import sys
import asyncio
import json
import os
import RPi.GPIO as GPIO
from aiohttp import web

class PhaazeHome(object):
	def __init__(self):
		self.version = "0.5"
		self.out_pins = [3, 5, 7, 11, 13, 15, 19, 21]
		self.setup_pins()

	from pin_controll import pins, setup_pins

PH = PhaazeHome()

SERVER = web.Application()
SERVER.router.add_route('GET', '/pins{useless:.*}', PH.pins)

web.run_app(SERVER, port=80)
GPIO.cleanup()