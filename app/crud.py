from sqlalchemy.orm import Session
from . import models
from . import schemas


def create_job_offering(db: Session, schema: schemas.JobOfferingSchema):
    job_offering = models.JobOffering(**schema.dict())
    db.add(job_offering)
    db.commit()
    db.refresh(job_offering)
    return job_offering


def read_job_offering(db: Session, job_id: int):
    return db.query(models.JobOffering).filter(models.JobOffering.id == job_id).first()


def update_job_offering(db: Session, job_id: int, schema: schemas.JobOfferingSchema):
    job_offering = read_job_offering(db, job_id)
    if job_offering:
        for field, value in schema:
            setattr(job_offering, field, value)
        db.commit()
        db.refresh(job_offering)
    return job_offering


def delete_job_offering(db: Session, job_id: int):
    job_offering = read_job_offering(db, job_id)
    if job_offering:
        db.delete(job_offering)
        db.commit()
    return job_offering


def list_job_offerings(db: Session):
    return db.query(models.JobOffering).all()
