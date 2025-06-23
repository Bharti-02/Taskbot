import os
import time
import requests
from decouple import config
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskbot.settings")
django.setup()

from django.contrib.auth.models import User
from core.models import TelegramUser

TOKEN = config("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        print(" Reply status:", response.status_code)
        print(" Reply body:", response.text)
    except Exception as e:
        print(" Failed to send message:", e)


    try:
        response = requests.post(url, data=payload)
        print(" Reply status:", response.status_code)
        print(" Reply body:", response.text)
    except Exception as e:
        print(" Failed to send message:", e)


def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    username = message["from"].get("username", f"user_{message['from']['id']}")

    print(f" Message from chat_id: {chat_id}, username: {username}")

    user = User.objects.first()
    if user:
        TelegramUser.objects.update_or_create(
            user=user,
            defaults={"telegram_username": username}
        )
        print(" Saving username to DB worked")
        print("out to send reply to user...")
        send_message(chat_id, f"Hi @{username}, you are now registered with TaskBot ")

def run_bot():
    print("🤖 Telegram bot is running...")
    offset = None
    while True:
        try:
            updates = get_updates(offset)
            if updates.get("ok"):
                for update in updates["result"]:
                    print("Update:", update)
                    handle_update(update)
                    offset = update["update_id"] + 1
            time.sleep(2)
        except Exception as e:
            print(" Bot error:", e)
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
