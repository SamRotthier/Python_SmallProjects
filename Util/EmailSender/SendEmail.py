import smtplib, ssl 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Credentials

def create_image_attachment(path: str) -> MIMEImage:
   with open(path,'rb') as image: # rb= read bitemode
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'Attachment; filename={path}')
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str= 'smtp-mail.outlook.com'
    port: int= 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('Logging in ...')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(Credentials.EMAIL, Credentials.PASSWORD)

        #Prepare the email
        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = Credentials.EMAIL
        message['To']= to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)
        
        server.sendmail(from_addr=Credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        #Success!
        print('Sent!')


if __name__ == '__main__':
        send_email(to_email='test_email@fastmail.com', 
                   subject='Hey there buddy', 
                   body='Hello there! I send you an image of my cat!',
                   image='cat.png')