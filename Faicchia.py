import discord
import random
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='!')

class Faicchia(discord.Client):
	global client

	# Preparing the BOT
	async def on_ready(self):
		global client
		print('Logged in as {0}!'.format(self.user))

	# BOT response to a user.client message
	async def on_message(self, message):
		try:
			# Checks if the author of the message is the BOT itself
			if message.author == self.user:
				return
		
			# Commands
			if message.content.startswith('!saluto'):
				await message.channel.send('Salve uomini')
			elif message.content.startswith('!foto'):
				# Sends a random image
				images = []

				try:
					with open('files/immagini.txt') as f:
						images = f.read().splitlines()
					
					random_image = random.choice(images)
					print("Image name: ", random_image)
					await message.channel.send('', file=discord.File(f"images/{random_image}"))
				except FileNotFoundError as error:
					print(error)

			elif message.content.startswith('!faicchia'):
				# Sends a random quote from frasi.txt
				quotes = []

				try:
					with open('files/frasi.txt') as f:
						for quote in f:
							quotes.append(quote)
				
					random_quote = random.choice(quotes)
					await message.channel.send(random_quote)
				except FileNotFoundError:
					print('File doesn\'t exist')
		except Exception as error:
			print(error)

	

'''
	********* Main *********
'''

faicchia = Faicchia()

# BOT token
TOKEN = 'NjkzMTk2NTMzNzg4ODM1OTUw.Xn5jlA.Iz2Y62qi4-qLGqAUrX6BuFV7KdE'

# Joins a channel

# Starting the bot
faicchia.run(TOKEN)
