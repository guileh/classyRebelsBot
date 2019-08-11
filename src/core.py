import json
import requests
import traceback

# Command list modules
from search_player_name import *

# Telegram and config modules
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_URI


def start(bot, update):
    response_message = "Voce esta em casa guardiao!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def unknown(bot, update):
    response_message = "Que? Tendi nada..."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    #USER START
    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    #USER COMMAND INTERFACE
    dispatcher.add_handler(
        CommandHandler('buscargt', search_player_name, pass_args=True)
    )
    #IF COMMAND IS FALSE
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
