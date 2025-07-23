"""Simple scheduler using APScheduler."""

from apscheduler.schedulers.background import BackgroundScheduler
from .bot_runner import run_all

scheduler = BackgroundScheduler()

scheduler.add_job(run_all, 'interval', minutes=5)


def start():
    scheduler.start()
