import requests
from decouple import config

TOKEN = config("TELEGRAM_BOT_TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())
