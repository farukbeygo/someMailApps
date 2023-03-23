import smtplib
import datetime as dt
import random as rd

with open("quotes.txt") as quotes:
    lines_data = quotes.readlines()

my_gmail = "testcodefaruk@gmail.com"
password = "waysjuexxbyzsfjt"

now = dt.datetime.now()
hour = now.hour
min = now.minute

# some smtp objects

if min == 0 and hour == 0:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="whyoursad.gmail.com",
            msg=f"Subject:Daily Quote\n\n{rd.choice(lines_data)}"
        )



