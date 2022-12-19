import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # using MIME to help with email features like heading subject .
from email.mime.multipart import MIMEMultipart


def send(filename):
    from_mail_addr = "darksharma3@gmail.com"
    from_passwd = "dsvvnyneemmydnqk"
    to_mail_addr = "kapadiya.darsheeldk@gmail.com"
    subject = "Invoice PDF Report"

    # # Some MIME multipart for email
    msg = MIMEMultipart()
    msg["From"] = from_mail_addr
    msg["To"] = to_mail_addr
    msg["Subject"] = subject

    # #you can even sent this as plain text or html text. Both showm here
    # body = "Hi there! Sent a message through python script"
    # msg.attach(MIMEText(body, "plain"))
    body = "<b>Hi there!</b> Today's Finance Report Attached."  # Use html bold text
    msg.attach(MIMEText(body, "html"))


    # to read and send the csv file ->>>>>>>>>>>>>
    # To read
    my_file = open(filename, 'rb')  # rb is read binary method to read file
    # To send
    part = MIMEBase('application', 'octet-stream')  # to obey our command and upload file to send
    part.set_payload((my_file).read())
    encoders.encode_base64(part)  # read byte stream and encode the bytestream
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_mail_addr, from_passwd)  # created an app password from Google account

    # Required now To , from, body
    server.sendmail(from_mail_addr, to_mail_addr, message)

    server.quit()
