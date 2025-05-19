import discord
from discord.ext import commands
import requests
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_NAME = "axel-feet"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.name == CHANNEL_NAME and message.attachments:
        for attachment in message.attachments:
            if attachment.content_type and attachment.content_type.startswith("image/"):
                payload = {
                    "username": message.author.name,
                    "image_url": attachment.url,
                    "timestamp": str(message.created_at)
                }
                try:
                    requests.post("http://localhost:5000/api/upload", json=payload)
                    print("Image sent to backend.")
                except Exception as e:
                    print("Failed to send image:", e)
    await bot.process_commands(message)

bot.run(TOKEN)
