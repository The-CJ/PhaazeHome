import asyncio, discord

class pheeze(discord.Client):
	def __init__(self, BASE):
		BASE.pheeze = self
		self.BASE = BASE
		super().__init__()

	async def on_ready(self):
		try:
			await self.BASE.pheeze.change_presence(	game=discord.Game(	
											type=0,
											name=self.BASE.version_nr),
								status=discord.Status.online)
		except:
			await asyncio.sleep(3)
			await self.on_ready()

	#message management
	async def on_message(self, message):
		if message.author.id != "117746512380952582": return

		if message.content == "!alloff":
			for x in range(1,8):
				setattr(self.BASE.STATUS, "_"+str(x), False)

		if message.content == "!allon":
			for x in range(1,8):
				setattr(self.BASE.STATUS, "_"+str(x), True)

		if message.content == "!1":
			if self.BASE.STATUS._1:
				self.BASE.STATUS._1 = False
			else:
				self.BASE.STATUS._1 = True

		if message.content == "!2":
			if self.BASE.STATUS._2:
				self.BASE.STATUS._2 = False
			else:
				self.BASE.STATUS._2 = True

		if message.content == "!3":
			if self.BASE.STATUS._3:
				self.BASE.STATUS._3 = False
			else:
				self.BASE.STATUS._3 = True

		if message.content == "!4":
			if self.BASE.STATUS._4:
				self.BASE.STATUS._4 = False
			else:
				self.BASE.STATUS._4 = True

		if message.content == "!5":
			if self.BASE.STATUS._5:
				self.BASE.STATUS._5 = False
			else:
				self.BASE.STATUS._5 = True

		if message.content == "!6":
			if self.BASE.STATUS._6:
				self.BASE.STATUS._6 = False
			else:
				self.BASE.STATUS._6 = True

		if message.content == "!7":
			if self.BASE.STATUS._7:
				self.BASE.STATUS._7 = False
			else:
				self.BASE.STATUS._7 = True

		if message.content == "!8":
			if self.BASE.STATUS._8:
				self.BASE.STATUS._8 = False
			else:
				self.BASE.STATUS._8 = True
