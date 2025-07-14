from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

scheduler = BackgroundScheduler()

def dummy_job(job_id: int, job_name: str):
    print(f"[{datetime.utcnow()}] Executing job {job_id}: {job_name}")
