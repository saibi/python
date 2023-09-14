import smtplib
import datetime as dt
import random

your_email = "email address"

test_msg = "Subject:Hello\n\nThis is the body of my email."
my_email = "use hotmail.com"
password = "password"


def send_mail(to_email, message):
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email, msg=message)


def load_quotes():
    with open("quotes.txt") as file:
        quotes = file.readlines()
    return quotes


now = dt.datetime.now()
print(now)
day_of_week = now.weekday()
print(day_of_week)

# date_of_birth = dt.datetime(year=1976, month=2, day=3)
# print(date_of_birth)


quotes = load_quotes()

today_quote = random.choice(quotes)
print(today_quote)

THURSDAY = 3

if day_of_week == THURSDAY:
    print("send email")
    send_mail(your_email, f"Subject:today's quote\n\n{today_quote}")
