import requests
from datetime import datetime, timedelta
import time
import yagmail  # Import yagmail library

MY_LAT = 6.5965  # Replace with your latitude
MY_LONG = 3.342  # Replace with your longitude

MY_EMAIL = "joeuyiobazee@gmail.com"  # Your Gmail address
RECEIVER_EMAIL = "utejoe.ju@gmail.com"  # Email address to receive notifications

yag = yagmail.SMTP(MY_EMAIL, 'rjsk obub hoqw htgs')  # Initialize yagmail with your credentials

def get_iss_position():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        return iss_latitude, iss_longitude
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS position: {e}")
        return None, None

def is_iss_overhead():
    iss_latitude, iss_longitude = get_iss_position()
    if iss_latitude is None or iss_longitude is None:
        return False
    
    # Check if ISS is within +5 or -5 degrees of my position
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

def is_night():
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        now = datetime.now()
        current_hour = now.hour

        if current_hour >= sunset or current_hour <= sunrise:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sunrise-sunset data: {e}")
        return False

def get_iss_passover():
    try:
        iss_latitude, iss_longitude = get_iss_position()
        if iss_latitude is None or iss_longitude is None:
            return None
        
        parameters = {
            "lat": iss_latitude,
            "lon": iss_longitude,
            "n": 1  # Number of passes to predict
        }
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        response.raise_for_status()
        data = response.json()

        if data and data["response"]:
            pass_time = data["response"][0]["risetime"]
            pass_time = datetime.fromtimestamp(pass_time)
            pass_time = pass_time + timedelta(hours=1)  # Adjusting for UTC to local time difference
            return iss_latitude, iss_longitude, pass_time
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS passover data: {e}")
        return None

def send_email():
    subject = "Look Up 👆"
    content = "The ISS is above you in the sky!"
    yag.send(to=RECEIVER_EMAIL, subject=subject, contents=content)

def main():
    while True:
        time.sleep(60)  # Run every 60 seconds
        if is_iss_overhead() and is_night():
            send_email()
        else:
            iss_info = get_iss_passover()
            if iss_info:
                iss_latitude, iss_longitude, pass_time = iss_info
                print(f"The ISS is currently at latitude {iss_latitude} and longitude {iss_longitude}.")
                print(f"It will be overhead at approximately {pass_time.strftime('%Y-%m-%d %H:%M:%S')} local time.")

if __name__ == "__main__":
    main()
