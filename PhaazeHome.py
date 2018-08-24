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
		self.response = self.send_back_response

	from pin_controll import pins, setup_pins
	from interface import web_interface

	def send_back_response(self, **kwargs):
		already_set_header = kwargs.get('headers', dict())
		kwargs['headers'] = already_set_header
		kwargs['headers']['server'] =f"PhaazeHome v{self.version}"

		if kwargs['headers'].get('Content-Type', None) == None:
			kwargs['headers']['Content-Type'] ="Application/json"

		return web.Response(**kwargs)


PH = PhaazeHome()

SERVER = web.Application()
SERVER.router.add_route('*', '/pins{useless:.*}', PH.pins)
SERVER.router.add_route('GET', '/web{path:.*}', PH.web_interface)

web.run_app(SERVER, port=80)
GPIO.cleanup()