import json
import os
import sys
import random

import discord

intents = discord.Intents.default()
intents.message_content = True

def load_configs():
    if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
        sys.exit(" Configuration file 'config.json' not found.")

    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as f:
        config = json.load(f)

    return config

async def handle_algo_topic(message: discord.Message):
    algo_topic = [
            "graphs",
            "geometry",
            "dynamic programming",
            "implementation problem",
            "number theory",
            "probability",
            "schedules",
            "queries",
            "bitwise operations",
            "interactive",
            "string",
            "meet-in-the-middle",
            "2sat"
        ]
    
    response = random.choice(algo_topic)
    await message.channel.send(f"Trening czas zacząć!\nDzisiejsza tematyka to :\n************\n{response}\n************\n")
    