import datetime as dt
import random
import yagmail

def get_quotes(file_path):
    try:
        with open(file_path, 'r') as file:
            quotes = file.readlines()
        return quotes
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def send_motivational_email():
    # Get the current day of the week
    now = dt.datetime.now()
    current_weekday = now.weekday()  # Monday is 0, Sunday is 6
    print(f"Current day of the week: {current_weekday}")

    # Check if today is Monday (for testing, you can change the condition)
    if current_weekday == 0:  # 0 means Monday
        print("Today is Monday. Preparing to send email.")
        quotes = get_quotes('quotes.txt')
        
        if quotes:
            quote = random.choice(quotes).strip()

            # Email details
            from_email = "your_email@gmail.com"
            password = "your_password"
            to_email = "recipient_email@gmail.com"
            subject = "Monday Motivation"  # Subject for the email

            # Send email
            try:
                yag = yagmail.SMTP(from_email, password)
                yag.send(to=to_email, subject=subject, contents=quote)
                print(f"Email sent successfully to {to_email}")
            except Exception as e:
                print(f"Failed to send email: {str(e)}")
        else:
            print("No quotes found to send.")
    else:
        print("Today is not Monday. No email will be sent.")

if __name__ == "__main__":
    send_motivational_email()
