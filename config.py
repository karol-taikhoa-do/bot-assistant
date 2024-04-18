import discord

BOT_PREFIX='!'

INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True