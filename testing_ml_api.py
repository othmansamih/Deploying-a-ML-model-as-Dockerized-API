import json
import requests

input_data = {
  "Pregnancies": 0,
  "Glucose": 0,
  "BloodPressure": 0,
  "SkinThickness": 0,
  "Insulin": 0,
  "BMI": 0,
  "DiabetesPedigreeFunction": 0,
  "Age": 0
}

input_data_json = json.dumps(input_data)

url = "http://localhost/diabetes_model"

response = requests.post(url, input_data_json)

print(response.text)