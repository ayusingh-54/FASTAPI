from fastapi import FastAPI , Path ,HTTPException, Query 
import json


app = FastAPI()
def load_data():
    with open("patients.json" , "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def hello_world():
    return {"message": "\patient Management System API is running."}

@app.get("/about")
def about():
    return {"message": "This is the about page."}



@app.get("/view")
def view_patients():
    data = load_data()
    return {"patients": data}



# Patient Management System 
@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data = load_data()
    if patient_id in data:
        return  data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")





@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Attribute to sort by", example="age") , order: str = Query("asc", description="Sort order: asc or desc", example="asc")):
    data = load_data()
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in  valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort attribute. Valid attributes are: {', '.join(valid_fields)}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Valid orders are: asc, desc")
    sorted_patients = dict(sorted(data.items(), key=lambda item: item[1][sort_by], reverse=(order=="desc")))
    return {"sorted_patients": sorted_patients}