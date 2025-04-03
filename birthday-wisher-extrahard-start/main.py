##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import datetime
import random

df=pandas.read_csv("birthdays.csv")
today=datetime.datetime.now()
today_month=today.month
today_day=today.day


myemail="srmap999@gmail.com"
passw="fblq qwax wtci aijl"

for index,row in df.iterrows():
    if today_month==row["month"] and today_day==row["day"]:
        name=row["name"]
    
        with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            content=file.read()
            message = content.replace("[NAME]", name)   


        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(myemail,passw)
            connect.sendmail(from_addr=myemail,to_addrs=row["email"],msg=f"Subject: Happy Birthdayyy!\n\n{message}")


