
MY_LAT = 23.424076
MY_LNG = 53.847816

from email.message import EmailMessage
import requests
from datetime import datetime
import smtplib
import time

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
    "tzid":"Asia/Dubai",
}

my_email = "raphaelcreer@gmail.com"
my_password = "otbnhpfxuqcmsqlm"

def send_msg(iss_latitude, iss_longitude, sunset, hour, sunrise):
    if (int(float(iss_latitude)) == int(float(MY_LAT)) and
        int(float(iss_longitude)) == int(float(MY_LNG)) and
            int(sunset) < hour != int(sunrise)):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            email = EmailMessage()
            connect.starttls()
            connect.login(user=my_email, password=my_password)
            email['To'] = "raphawesomeburg@gmail.com"
            email['From'] = "Raphael"
            email['Subject'] = "Look up!"
            email.set_content("The International space station is close by!\nLook up!\n" +
                              f"ISS longitude: {iss_longitude}\n" + f"ISS latitude: {iss_latitude}\n" +
                              f"Current longitude and latitude: {(MY_LNG, MY_LAT)}\n" + f"Current Date and Time: {time_now}\n")
            connect.send_message(email)
            print("message sent!")
    else:
        print("Not even close lol")

timer = 60
while 1:
    print(timer)
    if timer == 0:
        #Datetime
        time_now = datetime.now()

        #Sunset, Sunrise API
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
        sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
        print(time_now.hour)
        print((sunrise, sunset))

        #ISS API
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        iss_longitude = response.json()["iss_position"]["longitude"]
        iss_latitude = response.json()["iss_position"]["latitude"]
        print((MY_LNG, MY_LAT))
        print((iss_longitude, iss_latitude))

        send_msg(iss_latitude, iss_longitude, sunset, time_now.hour, sunrise)
        timer = 61
    timer -= 1
    time.sleep(1)