import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():

    sender = "bhavya.sahithi@nineleaps.com"
    password = "ocgu hrnn bvmu ktnx"
    receiver = "sahithi.124282@gmail.com"

    msg = MIMEMultipart()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Daily Airbnb ETL Report"

    with open("/home/nineleaps/airflow/dags/output/summary.txt") as f:
        body = f.read()

    body += "\n\nPlease find the EDA charts attached."

    msg.attach(MIMEText(body, "plain"))

    attachments = [
        "/home/nineleaps/airflow/dags/output/price_distribution.png",
        "/home/nineleaps/airflow/dags/output/room_type.png",
        "/home/nineleaps/airflow/dags/output/price_by_area.png"
    ]

    for file in attachments:

        with open(file, "rb") as f:

            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())

        encoders.encode_base64(part)

        filename = file.split("/")[-1]

        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}"
        )

        msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.send_message(msg)

    server.quit()

    print("Email sent successfully")