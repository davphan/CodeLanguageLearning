import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ACTIVE_CHANNEL = os.getenv('DISCORD_CHANNEL')

client = discord.Client()

@client.event
async def on_ready():
  # check which server the bot is being ran in
  guild = discord.utils.get(client.guilds, name=GUILD)

  print(
    f'{client.user} has connected to Discord!\n'
    f'Server: {guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
  # prevent looping
  if message.author == client.user:
    return

  # list of usable words
  NATO = ['ALPHA', 'BRAVO', 'CHARLIE', 'DELTA', 'ECHO', 'FOXTROT', 'GOLF',
          'HOTEL', 'INDIA', 'JULIETT', 'KILO', 'LIMA', 'MIKE', 'NOVEMBER',
          'OSCAR', 'PAPA', 'QUEBEC', 'ROMEO', 'SIERRA', 'TANGO', 'UNIFORM',
          'VICTOR', 'WHISKEY', 'XRAY', 'YANKEE', 'ZULU']

  # court marshall role object
  guild = discord.utils.get(client.guilds, name=GUILD)
  CMrole = discord.utils.get(guild.roles, name="COURT MARSHALLED")

  # check if already court marshalled
  if CMrole in message.author.roles:
    await message.delete()
    await message.channel.send(f"{message.author.mention} Court Marshalled soldiers may not speak, you may ask a higher ranking officer for forgiveness")
    return

  # set which channel NATO bot is active on
  if int(message.channel.id) == int(ACTIVE_CHANNEL):

    # check messages for court marshalling
    message_words = message.content.split()
    for word in message_words:

      # get rid of periods in between words
      if word[-1] == '.':
        word = word[:-1]

      # invalid message passed
      if word.upper() not in NATO:
        await message.channel.send(f"{message.author.mention} You've been COURT MARSHALLED")
        await message.author.add_roles(CMrole)
        return

client.run(TOKEN)