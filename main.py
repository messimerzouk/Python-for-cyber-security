import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# creating an smtp server
server = smtplib.SMTP('smtp.gmail.com', 465)

server.ehlo()
server.login('email', 'password')

msg = MIMEMultipart()
msg['From'] = 'MESSI'
msg['To'] = 'm_merzouk@estin.dz'

msg['Subject'] = 'Test Script'

msg.attach(MIMEText('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'), 'plain')

filename = 'image.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename={filename}')
text = msg.as_string()
server.sendmail('messimerzouk0@gmail.com', 'm_merzouk@estin.dz', text)
