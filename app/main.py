from fastapi import FastAPI
from .api import routes
from .core.scheduler import scheduler
from .db import base
from sqlalchemy import create_engine
from .core.config import settings

app = FastAPI(
    title="Scheduler Microservice",
    description="Microservice for scheduling jobs",
    version="1.0"
)

app.include_router(routes.router)

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
base.Base.metadata.create_all(bind=engine)

scheduler.start()
