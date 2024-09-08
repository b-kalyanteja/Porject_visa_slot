import requests
from telegram import Bot
from telegram.error import TelegramError
import time


def phone_alert(message):
    TELEGRAM_BOT_TOKEN = '7307218518:AAEVqs0-IK43WeAPmAIBmcSWTmgzDIfkj_U' # blavk phone
    TELEGRAM_CHAT_ID = '7102839502' # black phone

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    try:
        response = requests.get(url)
        response_data = response.json()
        if not response_data.get("ok"):
            print(f"Failed to send Telegram message: {response_data}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    #For samsung Phone 

    TELEGRAM_BOT_TOKEN_S = '7212614662:AAFfv9I-9uzr40n04AZvJZNeB676Y8vSXz0' # blavk phone
    TELEGRAM_CHAT_ID_S = '778338184' # black phone

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN_S}/sendMessage?chat_id={TELEGRAM_CHAT_ID_S}&text={message}"
    try:
        response = requests.get(url)
        response_data = response.json()
        if not response_data.get("ok"):
            print(f"Failed to send Telegram message: {response_data}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
