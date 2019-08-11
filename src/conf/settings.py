import os

from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HTTP_URI = os.getenv("BASE_HTTP_URL")


HTTP_PLAYER_NAME="https://search-api.tracker.network/d2players?q="
