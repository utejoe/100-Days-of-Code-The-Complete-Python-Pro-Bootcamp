import yagmail

def send_email(subject, body, to_email, from_email, password):
    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(to=to_email, subject=subject, contents=body)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Example usage
from_email = "joeuyiobazee@gmail.com"
password = "rjsk obub hoqw htgs"
to_email = "obazeeuyijoe@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."

send_email(subject, body, to_email, from_email, password)
