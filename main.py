# a highly functional complex math solver with quantum mechanics abilities totally not made for fun
# made for discord, an app made for educational and scientific purposes, btw

import discord
import discord.ext
from discord.utils import get
import os
import random
import time
import datetime
import discord.ext

client=discord.Client()

@client.event
async def on_ready():
  print ("SidBot is running")


@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith("//hello"):
    await message.channel.send("Hello vat ees up. Dis ees SidBot")

  if message.content.startswith("//Abhi"):
    await message.channel.send("vy are yu using dis bot")

  if message.content.startswith("//sendmessage"):
    userMessage=message.content[12:]
    await message.channel.send(userMessage)
  
  if message.content.startswith("//flip"):
    answer = random.randint(1,2)
    if answer==1:
      await message.channel.send("heads")
    elif answer==2:
      await message.channel.send("tails")

  if message.content.startswith("//calc"):
    await message.channel.send("Type your problem below. . .")
    calcProblem = message.content[12:]
    almostDone = eval(calcProblem)
    print(almostDone)


    

  

client.run(os.getenv('TOKEN'))