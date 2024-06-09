import discord
import os
from leetify_data_scrape import *
from create_tables import *

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
            stats, match_history = get_profile_page("Steve")
            print("HorzaBora found!")
            stats_table = create_stats_table(stats)
            match_history_table = create_stats_table(match_history)
            await message.channel.send("```" + stats_table + "```")
        if "Dougle" in message.content:
            print("Trying to find Dougle")
            stats, match_history = get_profile_page("Jamie")
            print("Dougle found!")
            stats_table = create_stats_table(stats)
            match_history_table = create_stats_table(match_history)
            await message.channel.send("```" + stats_table + "```")
        if "Delelith" in message.content:
            print("Trying to find Delelith")
            stats, match_history = get_profile_page("Jordan")
            print("Delelith found!")
            stats_table = create_stats_table(stats)
            match_history_table = create_stats_table(match_history)
            await message.channel.send("```" + stats_table + "```")
        if "Pariah" in message.content:
            print("Trying to find Pariah")
            stats, match_history = get_profile_page("Ed")
            print("Pariah found!")
            stats_table = create_stats_table(stats)
            match_history_table = create_stats_table(match_history)
            await message.channel.send("```" + stats_table + "```")

client.run(token)