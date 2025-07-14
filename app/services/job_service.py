from sqlalchemy.orm import Session
from ..db import models
from ..schemas.job import JobCreate
from ..core.scheduler import scheduler, dummy_job
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

def create_job(db: Session, job: JobCreate):
    db_job = models.Job(
        name=job.name,
        schedule=job.schedule
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    # Parse cron schedule
    cron_expr = job.schedule.replace("cron:", "")
    trigger = CronTrigger.from_crontab(cron_expr)

    scheduler.add_job(
        dummy_job,
        trigger,
        args=[db_job.id, db_job.name],
        id=str(db_job.id),
        replace_existing=True
    )
    return db_job

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def list_jobs(db: Session):
    return db.query(models.Job).all()
