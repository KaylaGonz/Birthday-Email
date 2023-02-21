import datetime as dt
import random
import pandas
import smtplib


my_email = "test@gmail.com"   # Replace with your email
password = "abc123"  # Replace with App password
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)


data = pandas.read_csv("birthdays.csv")  # Now a dataframe
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in bday_dict:
    birthday_person = bday_dict[today]
    random_num = random.randint(1,3)
    with open(f"letter_templates/letter_{random_num}.txt") as letter_file:
        letter = letter_file.read()
        name_replace = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{name_replace}")
