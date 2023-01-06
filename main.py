import requests
from datetime import datetime
import smtplib
import time
my_email = YOUR_EMAIL_HERE
password = YOUR_GENERATED_PASSWORD_FOR_EMAIL_LOGIN_HERE
MY_LAT = YOUR_LATITUDE_HERE
MY_LONG = YOUR_LONGITUDE_HERE


def over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    print(iss_latitude)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        go_outside()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position


def go_outside():
    if time_now.hour <= sunset or time_now.hour >= sunrise:
        with smtplib.SMTP(YOUR_EMAIL_SMTP_ADDRESS_HERE, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"LOOK UP!!!\n\nGO OUTSIDE AND LOOK UP!!")
while True:
    time.sleep(60)
    over_head()