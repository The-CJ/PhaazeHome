import asyncio
import RPi.GPIO as GPIO

async def pins(self, request):
	p = request.query.get('pin', None)
	if p == None:
		return self.response(status=400)

	current_status = self.pin_status.get(p, None)
	if current_status == None:
		return self.response(status=400)

	if current_status == True:
		self.pin_status[p] = False
		GPIO.output(int(p), False)
		s = True
	else:
		self.pin_status[p] = True
		GPIO.output(int(p), True)
		s = False

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
