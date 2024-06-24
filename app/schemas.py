from pydantic import BaseModel


class JobOfferingSchema(BaseModel):
    title: str
    company: str
    location: str
    description: str
    salary: float
    remote: bool
