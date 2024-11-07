#pip install discord

import os
from discord import Intents, Client
try:
    from . import Responses  # Relative import for package execution
except ImportError:
    import Responses   # Direct execution


def run_bot(token: str):
    """Run our Discord Bot with the token provided"""

    # Basic setup
    intents=Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = Responses.load_knowledge(os.path.join(os.path.dirname(__file__), 'Knowledge.json'))

    @client.event
    async def on_ready():
        """Print a startup message for our bot when it goes online."""
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        """Handle incoming messages from our server."""

        # client.user is the bot, the bot shouldn't respond to itself
        if message.author == client.user: #this will prevent an infinit loop where the bot will answer itself
            return
        
        #example of addition:
        #if message.content == 'roll':
        #   roll = dice_roll()
        #   await message.channel.send(roll)
        
        # If the user wrote something, send a response to the channel
        if message.content:
            print(f'({message.channel}) {message.author}: "{message.content}"')
            response: str = Responses.get_response(message.content, knowlegde=knowledge)
            await message.channel.send(response)
        else:
            print('!!!Could not read the message, make sure you have intents enabled!!!')

    # Run the bot with our token
    client.run(token=token)

if __name__ == '__main__':
    run_bot(token='TOKEN')


# Improvements:
#   - Make more commands and functionality