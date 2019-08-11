import json
import requests
import traceback

def search_player_name(bot, update, args):
    url="https://search-api.tracker.network/d2players?q="+args[0]+"&platform=1"
    try:
        response = requests.get(url)
        data = json.loads(response.content)

        if len(data) > 0:
            response_message = "Localizei esses guardioes: \n\n"  
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
