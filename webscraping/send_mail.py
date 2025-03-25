import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send():
    from_address = "a.mirzaye@gmail.com"
    to_address = "josixih877@x1post.com"
    password = "xytdudbwcpywnrzm"
    subject = "this is my email subject"

    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject

    body = "<b>Hi tis has been sent from python<b>"
    msg.attach(MIMEText(body, 'html'))


    my_file = open("scrape.csv", "rb")
    part = MIMEBase("application", "octet-stream" )
    part.set_payload(my_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + "scrape.csv")
    msg.attach(part)

    message = msg.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_address, password)

    server.sendmail(from_address, to_address, message)

    server.quit()