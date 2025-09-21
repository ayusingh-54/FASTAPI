from pydantic import BaseModel, Field

class Patient(BaseModel):
    name :str 
    age : int 

def insert_patient_data(Patient: Patient):
    print(Patient.name)
    print(Patient.age)
    print("Data inserted successfully")
Patient_info = { 'name': 'John', 'age': 30 }
Patient1 = Patient(**Patient_info)
insert_patient_data(Patient1)