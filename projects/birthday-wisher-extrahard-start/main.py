##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random

import pandas
import datetime as dt
import smtplib
from email.message import EmailMessage

my_email = "raphaelcreer@gmail.com"
my_password = "otbnhpfxuqcmsqlm"
csv_file = pandas.read_csv("birthdays.csv")
my_dict = {val.Name:[val.Name,val.email,val.year,val.month,val.day] for _,val in csv_file.iterrows()}
bday_messages = {}
email = EmailMessage()

for i in range(1,4):
    with open(f"letter_templates/letter_{i}.txt", mode="r+") as file:
        lines = file.readlines()
        bday_messages[str(i)] = []
        for val in lines:
            bday_messages[str(i)].append(val)

while 1:
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    print(f"{year}/{month}/{day}")

    for key,val in my_dict.items():
        if year in val and month in val and day in val:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connect:
                connect.starttls()
                connect.login(user=my_email, password=my_password)
                message = "".join(bday_messages[str(random.randint(1,3))])
                email['From'] = "Raphael"
                email['To'] = f"{val[1]}"
                email['Subject'] = "A Birthday greeting!"
                update_msg = message.replace("[NAME]", key)
                update_name = update_msg.replace("Angela", "Raphael")
                email.set_content(update_name)
                connect.send_message(email)
                print("message sent!")
                break
    break