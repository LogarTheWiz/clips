from flask_mail import Message

def send_email(mail, subject, recipients, body, html=None, sender=None):
    if not sender:
        sender = "noreply@aserinakava.online"
    msg = Message(subject, sender=sender, recipients=recipients, body=body, html=html)
    mail.send(msg)