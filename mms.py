import requests
import telegram
from telegram import Bot
from telegram.error import TelegramError
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler

TELEGRAM_BOT_TOKEN = '7307218518:AAEVqs0-IK43WeAPmAIBmcSWTmgzDIfkj_U'

TELEGRAM_CHAT_ID = '7102839502'

def telegram_mms(path):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto?"
    files = {'photo': open(path, 'rb')}
    data = {'chat_id': TELEGRAM_CHAT_ID}
    try:
        response = requests.post(url, files=files, data=data)
        response_data = response.json()
        if not response_data.get("ok"):
            print(f"Failed to send Telegram message: {response_data}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


# mesg = "sample"
# telegram_sms(mesg)