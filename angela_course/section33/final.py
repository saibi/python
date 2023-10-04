import requests
from datetime import datetime
import time

MY_LAT = 37.566536
MY_LNG = 126.977966


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_longitude, iss_latitude)
    print(iss_position)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        print("ISS is close to you.")
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    print(sunrise)
    print(sunset)

    time_now = datetime.utcnow().hour
    print(time_now.hour)

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time_now = datetime.utcnow()
    print(time_now)

    if is_iss_overhead and is_night:
        print("Look up!")

    time.sleep(60)
