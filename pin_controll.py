import asyncio
import RPi.GPIO as GPIO

async def pins(self, request):
	try:
		print(request.query)
	except Exception as e:
		pass

def setup_pins(self):
	GPIO.clearup()
	GPIO.setmode(GPIO.BOARD)
	for pin in self.out_pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, False)
