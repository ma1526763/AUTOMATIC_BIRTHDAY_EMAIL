from smtplib import SMTP
import os
from datetime import datetime
from birthday_wish_using_pandas import check_birthday, add_birthday
from random_letter_and_quote import random_quote, random_letter
from birthday_wish_using_json import check_birthday, add_birthday

# different ways for getting environment variables
SENDER_MAIL = os.environ["SENDER_MAIL"]
PASSWORD = os.environ.get('PASSWORD')
# send mail
def send_mail(name, mail, age):
    message = f"{random_letter(name)}\n\n Always Remember:\n{random_quote()}\n"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_MAIL, to_addrs=mail, msg=f"Subject:Happy {age} years\n\n{message}")
        print(f"mail sent to {name} at {mail}")

# use only one either through pandas or json
# using pandas
add_birthday(name="anas", email="ali@gmail.com", birthday=datetime(day=12, month=11, year=1992).strftime("%d-%m-%Y"))
today_birthday = check_birthday()

# using json
add_birthday(name="Shah", email="ahmed@gmail.com", birthday=datetime(day=12, month=11, year=1992).strftime("%d-%m-%Y"))
# today_birthday = check_birthday()
if today_birthday:
    for birthday in today_birthday:
        send_mail(birthday["name"], birthday["email"], datetime.now().year - int(birthday["birthday"][-4:]))
