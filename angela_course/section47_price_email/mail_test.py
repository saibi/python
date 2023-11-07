import smtplib

MY_EMAIL = "hotmail.com account"
MY_PASSWD = ""

SMTP_ADDR = "smtp-mail.outlook.com"


def send_mail(to_email, subject, message):
    with smtplib.SMTP(SMTP_ADDR) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWD)
        ret = connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:{subject}\n\n{message}")
        print(ret)

# send_mail(to_email="receiver", subject="Hello", message="How are you?")
