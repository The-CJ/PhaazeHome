import asyncio, json
import RPi.GPIO as GPIO

async def pins(self, request):
	_POST = await request.post()
	p = _POST.get('pin', None)
	status = _POST.get('status', None)

	multiple_pins = p.split(',')

	if p == None:
		return self.response(status=400)

	for pin in multiple_pins:

		current_status = self.pin_status.get(pin, None)
		if current_status == None:
			return self.response(status=400, body=json.dumps(dict(msg=f"pin '{pin}' not found")))

		if status in ['true', 'false']:
			ss = True if status == "true" else False
			GPIO.output(int(pin), ss)
			s = ss
			self.pin_status[pin] = ss
		else:
			if current_status == True:
				self.pin_status[pin] = False
				GPIO.output(int(pin), False)
				s = False
			else:
				self.pin_status[pin] = True
				GPIO.output(int(pin), True)
				s = True

	res = dict(
		code=200,
		pin=p,
		state=s
	)
	return self.response(status=200, body=json.dumps(res))

def setup_pins(self):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	for pin in self.out_pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, False)

pin_status = dict()

pin_status['3'] = False
pin_status['5'] = False
pin_status['7'] = False
pin_status['11'] = False
pin_status['13'] = False
pin_status['15'] = False
pin_status['19'] = False
pin_status['21'] = False
