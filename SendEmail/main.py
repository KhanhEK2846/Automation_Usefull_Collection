import os,ssl,smtplib
from email.message import EmailMessage

receiver = input("Input receiver email: ")
subject = "Email from python"
body="""
Hello and Hola from Python
"""

mail = EmailMessage()
mail['From'] = os.getenv("EMAIL")
mail['To'] = receiver
mail["Subject"] = subject
mail.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(os.getenv("EMAIL"),os.getenv("PASSWORD"))
    smtp.sendmail(os.getenv("EMAIL"),receiver,mail.as_string())
