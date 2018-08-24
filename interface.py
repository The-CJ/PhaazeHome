import asyncio, mimetypes

async def web_interface(self, request):
	path = request.path

	if path == "/web":
		path = "/web/html/master.html"

	path = path.replace("..", "")
	path = path.strip('/')

	try:
		r = open(path, "rb").read()
		return self.response(status=200, body=r, headers={'Content-Type': mimetypes.guess_type(path)[0]})

	except:
		return self.response(status=400)
