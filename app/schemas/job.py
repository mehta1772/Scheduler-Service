from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobCreate(BaseModel):
    name: str
    schedule: str  # e.g., 'cron:0 9 * * 1'

class JobRead(BaseModel):
    id: int
    name: str
    schedule: str
    last_run: Optional[datetime]
    next_run: Optional[datetime]

    class Config:
        orm_mode = True
