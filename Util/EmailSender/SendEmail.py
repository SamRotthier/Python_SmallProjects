import smtplib, ssl 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
try:
    from . import Credentials  # Relative import for package execution
except ImportError:
    import Credentials   # Direct execution


def create_image_attachment(path: str) -> MIMEImage:
   """Create an image type for our email and add a header to it."""

   with open(path,'rb') as image: # rb= read bitemode
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'Attachment; filename={path}')
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    # Specify the host and the port
    host: str= 'smtp-mail.outlook.com'
    port: int= 587

    # Validates the host name and its certificates and optimizes the security of the connection.
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        # Login
        print('Logging in ...')
        server.ehlo() # Used to greet the server and identify who we are
        server.starttls(context=context)
        server.ehlo()
        server.login(Credentials.EMAIL, Credentials.PASSWORD) # NEVER INCLUDE SENSITIVE VALUES IN YOUR SCRIPTS!!!

        #Prepare the email
        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = Credentials.EMAIL
        message['To']= to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # If there is an attachment, attach it to the e-mail
        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)
        
        # Send the email
        server.sendmail(from_addr=Credentials.EMAIL, to_addrs=to_email, msg=message.as_string())

        #Success!
        print('Sent!')


if __name__ == '__main__':
        send_email(to_email='test_email@fastmail.com', 
                   subject='Hey there buddy', 
                   body='Hello there! I send you an image of my cat!',
                   image='cat.png')
        
# Improvements:
#   - Automatically send an email when there is something wrong with a server or pc (like a service that has stopped)