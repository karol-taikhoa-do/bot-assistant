import os

from bot import BotAssistant
from utils import load_configs

def main():
    config = load_configs()

    eexor_assistant = BotAssistant(
        config=config,
        name="eexor assistant"
    )

    eexor_assistant.run(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    main()






