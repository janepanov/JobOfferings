"""
Database models for job offerings.
"""


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...

class JobOffering(Base):
    """Represents a job offering."""

    __tablename__ = "job_offerings"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    company: Mapped[str]
    location: Mapped[str]
    description: Mapped[str]
    salary: Mapped[float]
    remote: Mapped[bool] = mapped_column(default=False)
