"""
Pydantic schemas for job offerings.
"""


from pydantic import BaseModel


class JobOfferingSchema(BaseModel):
    """Schema representing a job offering."""

    title: str
    company: str
    location: str
    description: str
    salary: float
    remote: bool
