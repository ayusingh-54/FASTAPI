def insert_data(name :str , age :int):
    print(name)
    print(age)
    print("Data inserted successfully")

insert_data("John", "30")



def updated_patient_data(name : str , age :int):
    if type(name) == str and type(age) == int:
        print("Data is valid")
        print(name)
        print(age)
        print("Data updated successfully")
    else:
        raise TypeError("Invalid data type")
    
updated_patient_data("John", "30")
# updated_patient_data("John", "30")  # This will raise TypeError# Example without type hints