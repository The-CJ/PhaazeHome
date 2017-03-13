print("Starting...")

import sys

class BASE: 
	version_nr = "PhaazeHome v1"
	Aouth = #removed for github

	class STATUS:
		_1 = False
		_2 = False
		_3 = False
		_4 = False
		_5 = False
		_6 = False
		_7 = False
		_8 = False

import discord
import asyncio
import json
import os
import time
import requests
import threading
import socket
import RPi.GPIO as GPIO

################################################################################

class __DISCORD__(threading.Thread):
	def __init__(self):
		super(__DISCORD__, self).__init__()
		self.loop = asyncio.new_event_loop()

	def run(self):
		try:
			asyncio.set_event_loop(self.loop)

			from Main_discord import pheeze
			pheeze = pheeze(BASE)
			pheeze.run(BASE.Aouth)
		except Exception as e:
			print(str(e))
			pass

_discord_ = __DISCORD__()

##################################

class __GPIO__(threading.Thread):
	def __init__(self):
		super(__GPIO__, self).__init__()
		self.loop = asyncio.new_event_loop()

	def run(self):
		try:
			asyncio.set_event_loop(self.loop)

			GPIO.setmode(GPIO.BOARD)

			OUTS = [3, 5, 7, 11, 13, 15, 19, 21]
			for PIN in OUTS:
				GPIO.setup(PIN, GPIO.OUT)
				GPIO.output(PIN, False)

			while True:
				if "" == "":
					if BASE.STATUS._1:
						GPIO.output(3, True)
					else:
						GPIO.output(3, False)

					if BASE.STATUS._2:
						GPIO.output(5, True)
					else:
						GPIO.output(5, False)

					if BASE.STATUS._3:
						GPIO.output(7, True)
					else:
						GPIO.output(7, False)

					if BASE.STATUS._4:
						GPIO.output(11, True)
					else:
						GPIO.output(11, False)

					if BASE.STATUS._5:
						GPIO.output(13, True)
					else:
						GPIO.output(13, False)

					if BASE.STATUS._6:
						GPIO.output(15, True)
					else:
						GPIO.output(15, False)

					if BASE.STATUS._7:
						GPIO.output(19, True)
					else:
						GPIO.output(19, False)

					if BASE.STATUS._8:
						GPIO.output(21, True)
					else:
						GPIO.output(21, False)

				time.sleep(1)


		except Exception as e:
			print(str(e))
			pass
		finally:
			GPIO.clearup()

_gpio_ = __GPIO__()

################################################################################

async def thread_saving(_d_: __DISCORD__, _g_: __GPIO__):
	while True:
		if not _d_.isAlive():
			try:
				print("INFO: Booting PhaazeOS-Home Discord...")
				_d_ = __DISCORD__()
				_d_.start()
			except:
				print("INFO: Crashed...")

		if not _g_.isAlive():
			try:
				print("INFO: Booting GPIO...")
				_g_ = __GPIO__()
				_g_.start()
			except:
				print("INFO: Crashed...")

		await asyncio.sleep(5)

class secure_of_all_treads(threading.Thread):
	def __init__(self):
		super(secure_of_all_treads, self).__init__()
		self.name = "Saving"
		self.xloop = asyncio.new_event_loop()

	def run(self):
		asyncio.set_event_loop(self.xloop)
		while True:
			self.xloop.run_until_complete(thread_saving(
									_discord_,
									_gpio_
									))

secure = secure_of_all_treads()
secure.start()
