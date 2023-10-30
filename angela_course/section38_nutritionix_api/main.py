import requests
import os
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
if APP_ID is None or API_KEY is None:
    raise Exception("Please set your NUTRITIONIX environment variable.")

APP_ID = APP_ID.strip()
API_KEY = API_KEY.strip()
print(APP_ID)
print(API_KEY)

answer = input("Tell me which exercise you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json'
}
end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
query_data = {
    "query": answer,
    "gender": "male",
    "weight_kg": 72.0,
    "height_cm": 176.0,
    "age": 48,
}
response = requests.post(url=end_point, json=query_data, headers=headers)
response.raise_for_status()
print(response.json())

field_exercise = response.json()["exercises"][0]["name"].title()
field_duration = response.json()["exercises"][0]["duration_min"]
field_calories = response.json()["exercises"][0]["nf_calories"]

now = datetime.now()
field_date = now.strftime("%Y/%m/%d")
field_time = now.strftime("%X")

parameters = {
    "workout": {
        "date": field_date,
        "time": field_time,
        "exercise": field_exercise,
        "duration": field_duration,
        "calories": field_calories,
    }
}

# dump sheety
# sheety_endpoint = 'https://api.sheety.co/5829f1049069e6e7c7f335cbcb39321e/myWorkouts/workouts'
# response = requests.get(url=sheety_endpoint)
# response.raise_for_status()
# print(response.json())

# append sheety
sheety_endpoint = "https://api.sheety.co/5829f1049069e6e7c7f335cbcb39321e/myWorkouts/workouts"
bearer_header = {
    "Authorization": f"Bearer {API_KEY}"
}
response = requests.post(
    url=sheety_endpoint, json=parameters, headers=bearer_header)
response.raise_for_status()
print(response.json())
