"""
Module containing CRUD operations for job offerings.
"""

from sqlalchemy.orm import Session
from . import models
from . import schemas


def create_job_offering(db: Session, schema: schemas.JobOfferingSchema):
    """Create a new job offering."""

    # Implementation
    job_offering = models.JobOffering(**schema.dict())
    db.add(job_offering)
    db.commit()
    db.refresh(job_offering)
    return job_offering


def read_job_offering(db: Session, job_id: int):
    """Retrieve a job offering by ID."""

    # Implementation
    return db.query(models.JobOffering).filter(models.JobOffering.id == job_id).first()


def update_job_offering(db: Session, job_id: int, schema: schemas.JobOfferingSchema):
    """Update a job offering."""

    # Implementation
    job_offering = read_job_offering(db, job_id)
    if job_offering:
        for field, value in schema:
            setattr(job_offering, field, value)
        db.commit()
        db.refresh(job_offering)
    return job_offering


def delete_job_offering(db: Session, job_id: int):
    """Delete a job offering."""

    # Implementation
    job_offering = read_job_offering(db, job_id)
    if job_offering:
        db.delete(job_offering)
        db.commit()
    return job_offering


def list_job_offerings(db: Session):
    """List all job offerings."""

    # Implementation
    return db.query(models.JobOffering).all()
