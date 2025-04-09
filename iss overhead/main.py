import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
EMAIL_TO="venkatakartheeks2005@gmail.com"

def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude-5 < MY_LAT < iss_latitude+5 and iss_longitude-5 < MY_LONG < iss_longitude+5:
        return True
    return False

def is_night():
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
    time_now = datetime.now().hour

    if time_now>= sunset or time_now<=sunrise:
        return True

myemail="srmap999@gmail.com"
passw="fblq qwax wtci aijl"

while True:
    time.sleep(60)
    if is_night() and check_pos():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(myemail,passw)
            connection.sendmail(from_addr=myemail,to_addrs=EMAIL_TO,msg=f"Subject: See the SKY\n\n Iss is over head see up")



