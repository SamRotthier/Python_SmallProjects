#pip install discord

import os
from discord import Intents, Client
import Responses

def run_bot(token: str):
    #basic setup
    intents=Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = Responses.load_knowledge(os.path.join(os.path.dirname(__file__), 'Knowledge.json'))

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user: #this will prevent an infinit loop where the bot will answer itself
            return
        
        #example of addition:
        #if message.content == 'roll':
        #   roll = dice_roll()
        #   await message.channel.send(roll)
        
        if message.content:
            print(f'({message.channel}) {message.author}: "{message.content}"')
            response: str = Responses.get_response(message.content, knowlegde=knowledge)
            await message.channel.send(response)
        else:
            print('!!!Could not read the message, make sure you have intents enabled!!!')

    client.run(token=token)

if __name__ == '__main__':
    run_bot(token='MTEyMDYwMTA3NjQwNDYwNDk10A.GlK5hZ.ZHzZd7tuEBRJATmtpduvjhtveLukx6H1DeQQGk')