import json
import requests
import traceback


from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN, HTTP_URI, HTTP_PLAYER_NAME


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

def search_player_name(bot, update, args):
    response_message = "Localizei esses guardioes: \n\n"
    try:
        response = requests.get(HTTP_PLAYER_NAME+args[0])
        data = json.loads(response.content)

        if len(data) > 0:
            for value in data:
                if value['platform'] == 1 :
                    platform = "XBX"
                elif value['platform'] == 2 :
                    platform = "PS4"
                elif value['platform'] == 4:
                    platform = "_PC"
                else:
                    platform = "___"
                response_message = response_message + "  - [" + platform + "] " + value['name'] + "\n"
        else:
            response_message = "Nao existem guardioes com esse padrao, procure por NinoKusanagi que eh um nome muito mais comum."

    except Exception:
        traceback.print_exc()

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
        CommandHandler('buscar', search_player_name, pass_args=True)
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
