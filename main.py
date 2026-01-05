
import smtplib
import os
from dotenv import load_dotenv

# variables for the smtp email
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

try:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # connection.connect("smtp.gmail.com", 465)
        connection.starttls()
        submit = True
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: message sent!\n\nMessage sent\n\n")

except Exception as e:
    print(e)
