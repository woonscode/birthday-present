import os
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext


# Configure and start logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Get environment variables from Heroku config
TOKEN = os.environ.get("TOKEN")
PORT = int(os.environ.get("PORT", "8443"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

def start(update: Update, context: CallbackContext):
    reply = "Hello! This is a bot created by Woon Hao. Enter /help for assistance. Also, happy birthday!"
    update.message.reply_text(reply)
    input = "please key in your school email"
    update.message.reply_text(input)
    return 1

def end(update: Update, context: CallbackContext):
    update.message.reply_text("BYE!")
    return ConversationHandler.END

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to restart or /end to finish the conversation at any point in time!")
    update.message.reply_text("you can text me (woon hao) if there's any issues with the bot, thank you!")

def get_email(update: Update, context: CallbackContext):
    input_email = update.message.text
    correct_email = "email"
    if input_email == correct_email:
        update.message.reply_text("now, key in your password!")
        return 2
    elif input_email == "/end":
        update.message.reply_text("BYE!")
        return -1
    else:
        update.message.reply_text("incorrect email, please try again")
        return 1

def get_password(update: Update, context: CallbackContext):
    input_password = update.message.text
    correct_password = "password"
    url = "URL of website"
    
    if input_password == correct_password:
        update.message.reply_text("ok, identity confirmed")
        update.message.reply_text(url)
        update.message.reply_text("the link above is best accessed using a laptop")
        return ConversationHandler.END
    elif input_password == "/end":
        update.message.reply_text("BYE!")
        return -1
    else:
        update.message.reply_text("incorrect password, please try again")
        return 2

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    birthday_conv = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            1: [
                MessageHandler(Filters.text, get_email)
            ],
            2: [
                MessageHandler(Filters.text, get_password)
            ]
        },
        fallbacks=[CommandHandler('end', end)],
        allow_reentry= True
    )
    # Adding required handlers
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(birthday_conv)

    # Webhook config
    updater.start_webhook(listen="0.0.0.0",
                            port=PORT,
                            url_path=TOKEN,
                            webhook_url="https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
    updater.idle()

if __name__ == '__main__':
    main()