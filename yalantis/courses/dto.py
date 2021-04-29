from pydantic import BaseModel, Field
from datetime import datetime


class CreateCourseDto(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    start_date: datetime
    end_date: datetime
    lectures_amount: int
