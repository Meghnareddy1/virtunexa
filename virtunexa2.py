import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurationurl
API_KEY = "8d5e52f0410b619c6a4f6b86571d7d42"
lat = 21.0000
lon = 78.0000

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "pagillameghana07@gmail.com"
EMAIL_PASSWORD = "ygsa nxsh ykau fhoi"  
RECIPIENT_EMAIL = "pagillapavan161@gmail.com"
LOCATION = "India"  # Replace with your desired location

def get_weather_data(location):
   url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
   response = requests.get(url)
    
   response.raise_for_status()
   return response.json()

def format_weather_message(weather_data):
    location = weather_data["name"]
    temp = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    message = f"Weather Update for {location}:\n\nTemperature: {temp}°C\nCondition: {weather.capitalize()}"
    return message

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    try:
        weather_data = get_weather_data(LOCATION)
        weather_message = format_weather_message(weather_data)
        send_email("Daily Weather Update", weather_message)
        print("Weather update sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()