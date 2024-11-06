# In  telegram, look for BotFather (with the checkmark)
# press start
# do the command: /newbot
# give him a name like: luigi
# chose a username like: cool_abc_bot

# do the command: /setuserpic
# select the bot
# send a picture

# do the command: /setabouttext
# select the bot
# enter the text you want like: I am luigi bot, i will respond to you!

# do the command: /setdescription
# select the bot
# enter the text you want like: I can answer your messages and make your life easier.-Luigi

# do the command: /setjoingroups
# select the bot
# select enable

# do the command: /setcommands
# select the bot
# enter commands like: 
#   start - Starts the bot.
#   help - Type something to chat with the bot!
#   custom - This is a custom command!

#If you want to add the bot to a group
#invite him
#give add him as administrator

# pip install python-telegram-bot


from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Constants
TOKEN: Final[str]= '585303001:AAHQCgo-fKd7ksVZZJ-eIpsAopasGAyziCQ' #this token probably wont work
BOT_USERNAME: Final[str] = '@cool_abc_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! Nice to meet you. Let\'s chat!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just type something and I will respond to you!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command.')

# Create your own response logic
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good, thanks!'
    
    if 'i love python' in processed:
        return 'Pythin is cooooool'
    
    return 'I do not understand...'

# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.txt

    # Log users
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    # Handle message type
    if message_type == 'group':
        if BOT_USERNAME in text: #only call bot when name is mentioned
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # Reply
    print('Bot:', response)
    await update.message.reply_text(response)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error: {context.error}')

def main():
    print('Starting up bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Define a poll interval
    print('Polling...')
    app.run_polling(poll_interval=5)


if __name__ == '__main__':
    main()    

# Improvements:
#   - Make more commands and functionality