from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText  

def build_email(email_address, message, attachments=None):
    msg = MIMEMultipart()
    msg['To'] = email_address
    msg.attach(MIMEText(message))
    for attachment in attachments:
        f = open(attachment, "rb") 
        msg.attach(MIMEApplication(
                f.read(),
                Content_Disposition='attachment; filename="%s"' % attachment
            ))
        f.close()
        
    return msg