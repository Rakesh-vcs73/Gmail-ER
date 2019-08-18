import smtplib
from email.mime.text import MIMEText

body ="""Lets test if this message is really sent"""
msg = MIMEText(body)

fromaddr = "raki.vvv.777@gmail.com"

toaddr = "chinni.vvv.777@gmail.com"

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hi"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(fromaddr,"9343655497")

server.send_message(msg)
print('Mail Sent...')
server.quit()
