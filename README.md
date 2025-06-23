
# Project Title

A Django-powered Telegram bot that uses Celery to handle background tasks like scheduling, automation, and real-time updates.


## Features

- 🤖 Telegram Bot integration
- ⏱ Scheduled background tasks using Celery
- 🔌 Django modular architecture
- 🌐 Async support with ASGI
- 🔐 Uses `.env` for secrets and configs


##  Tech Stack
- Python 3
- Django
- Celery
- Redis (as broker)
- Telegram Bot API

---
## Setup Instructions

1.Clone this repository

git clone https://github.com/your-username/taskbot.git
cd taskbot.

2.Create a virtual environment and install dependencies

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

3.Create .env file

DEBUG=True

SECRET_KEY=your_secret_key

TELEGRAM_TOKEN=your_telegram_bot_token


4.Run migrations

python manage.py migrate

5.Start Django development server

python manage.py runserver

6.Start Celery worker (in a new terminal)

celery -A taskbot worker --loglevel=info

##  API Documentation (Basic)

Since this is a Telegram bot, it interacts with users via messages.

bot.py: handles incoming messages using Telegram APIs

get_updates.py: can use polling to fetch updates

check_bot.py: test bot responses

tasks.py: background jobs using Celery


##  How to Run Locally

git clone https://github.com/your-username/taskbot.git

cd taskbot

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

In a new terminal:

celery -A taskbot worker --loglevel=info

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.


Variable = Description

DEBUG = Debug mode (True/False)

SECRET_KEY = Django secret key

TELEGRAM_TOKEN =Your Telegram bot token
