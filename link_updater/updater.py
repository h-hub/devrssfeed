from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from link_updater import retrieve_links_api

def start():
    print("--start")
    scheduler = BackgroundScheduler()
    scheduler.add_job(retrieve_links_api.scheduled_job, 'interval', hours=12)    
    scheduler.start()