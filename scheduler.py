import xbox

from apscheduler.schedulers.blocking import BlockingScheduler

def iwantanxbox():
    xbox.findXBOX()

scheduler = BlockingScheduler()
scheduler.add_job(iwantanxbox, 'interval', hours =1)
scheduler.start()
