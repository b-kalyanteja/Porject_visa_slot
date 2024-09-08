import requests
from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = '7307218518:AAEVqs0-IK43WeAPmAIBmcSWTmgzDIfkj_U'

TELEGRAM_CHAT_ID = '7102839502'

def telegram_sms(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    try:
        response = requests.get(url)
        response_data = response.json()
        if not response_data.get("ok"):
            print(f"Failed to send Telegram message: {response_data}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


# mesg = "sample"
# telegram_sms(mesg)