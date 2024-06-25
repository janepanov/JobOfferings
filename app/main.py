"""
Main FastAPI application and endpoints.
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import SessionLocal, engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/job-offerings/", response_model=schemas.JobOfferingSchema)
def create_job_offering(job_offer: schemas.JobOfferingSchema, db: Session = Depends(get_db)):
    """Create a job offering."""
    return crud.create_job_offering(db=db, schema=job_offer)


@app.get("/job-offerings/{job_id}", response_model=schemas.JobOfferingSchema)
def read_job_offering(job_id: int, db: Session = Depends(get_db)):
    """Read a job offering."""
    db_job = crud.read_job_offering(db=db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job Offering not found")
    return db_job


@app.put("/job-offerings/{job_id}", response_model=schemas.JobOfferingSchema)
def update_job_offering(job_id: int, job_offer: schemas.JobOfferingSchema, db: Session = Depends(get_db)):
    """Update a job offering."""
    db_job = crud.update_job_offering(db=db, job_id=job_id, schema=job_offer)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job Offering not found")
    return db_job


@app.delete("/job-offerings/{job_id}", response_model=schemas.JobOfferingSchema)
def delete_job_offering(job_id: int, db: Session = Depends(get_db)):
    """Delete a job offering."""
    db_job = crud.delete_job_offering(db=db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job Offering not found")
    return db_job


@app.get("/job-offerings/", response_model=list[schemas.JobOfferingSchema])
def list_job_offerings(db: Session = Depends(get_db)):
    """List all job offerings."""
    return crud.list_job_offerings(db=db)
