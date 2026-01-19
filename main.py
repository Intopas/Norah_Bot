import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


load_dotenv()  # ← FIXED

token = os.getenv("DISCORD_TOKEN")

if not token:
    raise ValueError("DISCORD_TOKEN not found in environment variables")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f"Ready, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Dont talk to me im taken {member.name}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "max" in content:
        await message.channel.send(
            f"{message.author.mention} Dont talk to him he has a girlfriend"
        )

    if "norah" in content:
        await message.channel.send(
            f"{message.author.mention} Dont talk to me I have a boyfriend"
        )

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)


