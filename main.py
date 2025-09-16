import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ROASTS = open('roasts.txt').read().splitlines()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    await member.send(f'u r a failure, {member.mention}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    roast = random.choice(ROASTS)
    await message.channel.send(roast)

    await bot.process_commands(message)

bot.run(TOKEN)