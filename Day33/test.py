import requests
from datetime import datetime
MY_LAT=22.572645
MY_LONG=88.363892

def is_iss_overhead():
    respons=requests.get("http://api.open-notify.org/iss-now.json")

    data=respons.json()
    longitude=data["iss_position"]["longitude"]
    latitude=data["iss_position"]["latitude"]
    if MY_LONG-5<= longitude <=MY_LONG+5 and MY_LAT-5<=latitude<=MY_LAT+5:
        return True

def is_night():
    paramaters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }


    respons=requests.get(" https://api.sunrise-sunset.org/json",params=paramaters)

    respons.raise_for_status()

    data=respons.json()
    sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
    time_now=datetime.now().hour
    if time_now>=sunset and time_now<=sunrise:
        return True

