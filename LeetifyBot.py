import discord
import os
from leetify_data_scrape import *

token = os.environ.get('LEETIFY_BOT_TOKEN')
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        print("Received a message!")
        await message.channel.send('Hello!')

    if message.content.startswith('!leetify'):
        print("Received a message!")
        if "HorzaBora" in message.content:
            print("Trying to find HorzaBora")
            get_profile_page("Steve")
            await message.channel.send(file=discord.File(f"{path}/croppedscreenshot.png"))
        if "Dougle" in message.content:
            print("Trying to find Dougle")
            get_profile_page("Jamie")
            await message.channel.send(file=discord.File(f"{path}/croppedscreenshot.png"))
        if "Delelith" in message.content:
            print("Trying to find Delelith")
            get_profile_page("Jordan")
            await message.channel.send(file=discord.File(f"{path}/croppedscreenshot.png"))
        if "Pariah" in message.content:
            print("Trying to find Pariah")
            get_profile_page("Ed")
            await message.channel.send(file=discord.File(f"{path}/croppedscreenshot.png"))

client.run(token)