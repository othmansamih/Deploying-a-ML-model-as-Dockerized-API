import pickle
from fastapi import FastAPI
from pydantic import BaseModel

model_path = "Trained_model/diabetes_model.pkl"
model = pickle.load(open(model_path, "rb"))

app = FastAPI()

class InputModel(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

@app.post("/diabetes_model")
def diabetes_pred(input_model: InputModel):
    pre = input_model.Pregnancies
    glu = input_model.Glucose
    bp = input_model.BloodPressure
    st = input_model.SkinThickness
    ins = input_model.Insulin
    bmi = input_model.BMI
    dpf = input_model.DiabetesPedigreeFunction
    age = input_model.Age

    input_data = [pre, glu, bp, st, ins, bmi, dpf, age]
    prediction = model.predict([input_data])

    if prediction[0] == 0:
        return {
            "label": 0,
            "result": "This person is not diabetic!"
        }
    else:
        return {
            "label": 1,
            "result": "This person is diabetic!"
        }