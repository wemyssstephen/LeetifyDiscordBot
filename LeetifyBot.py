import discord
import os
from leetify_data_scrape import *
from create_tables import *

token = os.environ.get('LEETIFY_BOT_TOKEN')
client = discord.Client(intents=discord.Intents.all())


async def _send_table(name, stats, match_history, messageContent, message):
    """Sends the stats table to discord."""
    stats_table = create_stats_table(stats)
    if "match" in messageContent:
        match_history_table = create_match_history_table(match_history)
        await message.channel.send(f"### {name}'s last 15 matches:")
        await message.channel.send("```" + match_history_table + "```")
    else:
        await message.channel.send(f"### {name}'s Stats")
        await message.channel.send("```" + stats_table + "```")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    messageContent = message.content.lower()
    if message.author == client.user:
        return

    if messageContent.startswith('!hello'):
        print("Received a greeting!")
        await message.channel.send('Hello!')

    if messageContent.startswith('!leetify'):
        print("Received a leetify request!")

        if "horzabora" in messageContent:
            print("Trying to find HorzaBora")
            stats, match_history = get_profile_page("Steve")
            print("HorzaBora found!")
            await _send_table("HorzaBora", stats, match_history, messageContent, message)
            print("Sent table!")

        if "dougle" in messageContent:
            print("Trying to find Dougle")
            stats, match_history = get_profile_page("Jamie")
            print("Dougle found!")
            await _send_table("Dougle", stats, match_history, messageContent, message)
            print("Sent table!")

        if "delelith" in messageContent:
            print("Trying to find Delelith")
            stats, match_history = get_profile_page("Jordan")
            print("Delelith found!")
            await _send_table("Delelith", stats, match_history, messageContent, message)
            print("Sent table!")

        if "pariah" in messageContent:
            print("Trying to find PariahtyBit")
            stats, match_history = get_profile_page("Ed")
            print("PariahtyBit found!")
            await _send_table("PariahtyBit", stats, match_history, messageContent, message)
            print("Sent table!")


client.run(token)
