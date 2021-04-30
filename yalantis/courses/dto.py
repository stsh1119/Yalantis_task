from pydantic import BaseModel, Field, validator
from datetime import datetime


class CourseDto(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    start_date: datetime
    end_date: datetime
    lectures_amount: int

    @validator('end_date')
    def end_date_must_be_later_than_start_date(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError('start_date must be less than end_date')
        return v
