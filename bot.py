from discord.ext import commands
import discord
import platform
import os
import random

from bot_logging import setup_logger
from utils import intents

class BotAssistant(commands.Bot):
    def __init__(self, config, name='bot_assistant'):
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["bot_prefix"]),
            intents=intents,
            help_command=None
        )
        self.config=config
        self.logger = setup_logger(name)


    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"discord.py API version: {discord.__version__}")
        self.logger.info(f"Python version: {platform.python_version()}")
        self.logger.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name})"
        )
        
        guild = discord.utils.get(self.guilds, name=self.config["guild_name"])
        self.logger.info(f"Joined guild : {guild.name}")
        

    async def on_message(self, message: discord.Message):
        
        if message.author == self.user:
            return
        
        self.logger.info(f"Catched a message {message.content}")

        if message.content == self.config["bot_prefix"] + "algo-topic": # need fixing - without self.config
            from utils import handle_algo_topic
            await handle_algo_topic(message)
            self.logger.info("Algo topic chosen")
    
    async def on_member_join(self, member):
        await member.create_dm()
        welcome_message = '\n'.join(self.config["welcome_message"].format(member.name))
        await member.dm_channel.send(welcome_message)
        self.logger.info(f"{member.name} has been welcomed to the community")
    
    async def on_command_error(self, context: commands.Context, error) -> None:
        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                description="You are not the owner of the bot!", color=0xE02B2B
            )
            await context.send(embed=embed)
            if context.guild:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the guild {context.guild.name} (ID: {context.guild.id}), but the user is not an owner of the bot."
                )
            else:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the bot's DMs, but the user is not an owner of the bot."
                )
        else:
            raise error