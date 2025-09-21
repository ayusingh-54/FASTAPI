from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import List

class PathModel(BaseModel):
    name : str 
    email : str
    age : int
    weight : float
    allergies : List[str] = Field(default_factory=list)
    contact_details : dict = Field(default_factory=dict)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        valid_domains = ["example.com", "test.com"]
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
       

patient_info = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "weight": 70.5,
    "allergies": ["peanuts", "shellfish"],
    "contact_details": {
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    }
}

patient_1 = PathModel(**patient_info)
print(patient_1)