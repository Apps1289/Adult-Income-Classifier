from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated
import pandas as pd

class UserInput(BaseModel):
    
    age: Annotated[int, Field(ge=0, le=100, description="Age of the individual in years")]
    workclass: Annotated[str, Field(description="Type of employment or work class")]
    education: Annotated[str, Field(description="Highest level of education attained")]
    education_num: Annotated[int, Field(ge=0, le=40, description="Numerical representation of education level")]
    marital_status: Annotated[str, Field(description="Marital status of the individual")]
    occupation: Annotated[str, Field(description="Occupation of the individual")]
    relationship: Annotated[str, Field(description="Relationship status of the individual")]
    race: Annotated[str, Field(description="Race of the individual")]
    sex: Annotated[str, Field(description="Sex of the individual")]
    capital_gain: Annotated[int, Field(ge=0, description="Capital gains for the individual")]
    capital_loss: Annotated[int, Field(ge=0, description="Capital losses for the individual")]
    hours_per_week: Annotated[int, Field(ge=0, le=100, description="Hours worked per week")]
    native_country: Annotated[str, Field(description="Native country of the individual")]
    
    @field_validator('workclass', 'education', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country')
    def validate_fields(cls, value: str) -> str:
        value = value.strip().lower()
        return value
    
    
