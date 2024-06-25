"""
Database models for job offerings.
"""


from sqlalchemy import Column, Integer, String, Boolean, Float
from .db import Base


class JobOffering(Base):
    """Represents a job offering."""

    __tablename__ = "job_offerings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    description = Column(String)
    salary = Column(Float)
    remote = Column(Boolean, default=False)
