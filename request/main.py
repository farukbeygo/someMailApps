import requests
import DateTime as dt
import smtplib


# functions
def is_night():
    if time_now > sunset and time_now > sunrise:
        return True
    elif sunset > time_now and sunrise > time_now:
        return True
    return False


def is_iss_close():
    if is_night() and abs(MY_LAT - latitude) < 5 and abs(MY_LON - longitude) < 5:
        send_mail()


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="whyoursad.gmail.com",
            msg="Subject:ISS report\n\nLook at the sky, to see ISS!!"
        )


# my data
MY_LAT = 39.916899
MY_LON = 32.778773
my_gmail = "testcodefaruk@gmail.com"
password = "************"


# iss data
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

longitude = iss_response.json()["iss_position"]["longitude"]
latitude = iss_response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)


# day data
parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}

day_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
day_response.raise_for_status()
data = day_response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# my data
time_now = dt.DateTime().hour()


