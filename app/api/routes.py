from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import models
from ..schemas import job as schemas
from ..services import job_service
from ..core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

router = APIRouter()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs", response_model=schemas.JobRead)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, job)

@router.get("/jobs", response_model=list[schemas.JobRead])
def list_all_jobs(db: Session = Depends(get_db)):
    return job_service.list_jobs(db)

@router.get("/jobs/{job_id}", response_model=schemas.JobRead)
def get_single_job(job_id: int, db: Session = Depends(get_db)):
    job = job_service.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
