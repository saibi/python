import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "use hotmail.com"  # smtp works
PASSWORD = "password"


def send_mail(to_email, message):
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_email, msg=message)


def load_letter_template(filename):
    with open(filename) as letter_file:
        return letter_file.read()


letters = []
letters.append(load_letter_template("letter_1.txt"))
letters.append(load_letter_template("letter_2.txt"))

now = dt.datetime.now()
print(now)

data = pandas.read_csv("birthday.csv")
print(data)

dict = data.to_dict(orient="records")
print(dict)

for item in dict:
    if item["month"] == now.month and item["day"] == now.day:
        print(item)
        letter = random.choice(letters)
        letter = letter.replace("[NAME]", item["name"])
        letter = "Subject:Happy Birthday\n\n" + letter
        print(letter)
        send_mail(item["email"], letter)
