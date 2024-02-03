import conf
from boltiot import Bolt, Sms
import json  # Import the json module
import time

# Replace with your API key and Device ID

# Create Bolt and Sms objects
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

# Thresholds for temperature and light levels
TEMP_THRESHOLD_HIGH = 20  # Set your desired temperature threshold
TEMP_THRESHOLD_LOW = 10   # Set your desired temperature threshold
LIGHT_THRESHOLD_HIGH = 800  # Set your desired light threshold
LIGHT_THRESHOLD_LOW = 200   # Set your desired light threshold

# Pin configuration
LED_PIN = 0  # Assuming pin 0 functions as a digital pin
# ...

# Function to check sensor values and trigger alert
def check_and_alert():
    # Read sensor values
    temperature_response = mybolt.analogRead('A0')
    light_response = mybolt.analogRead('A0')  # Adjusted to read from A0 for the light sensor

    # Convert JSON strings to Python dictionaries
    temperature_data = json.loads(temperature_response)
    light_data = json.loads(light_response)

    # Extract analog readings from the JSON response
    temperature = int(temperature_data['value'])
    light = int(light_data['value'])

    # Check temperature and light levels
    if temperature > TEMP_THRESHOLD_HIGH or temperature < TEMP_THRESHOLD_LOW:
        alert_message = "Temperature Alert! Current Temperature: {} C".format(temperature)
        send_alert(alert_message)

    if light > LIGHT_THRESHOLD_HIGH or light < LIGHT_THRESHOLD_LOW:
        alert_message = "Light Alert! Current Light Intensity: {}".format(light)
        send_alert(alert_message)

# Function to send alert SMS and control LED
def send_alert(message):
    response = sms.send_sms("Alert: " + message)
    print("SMS Response: ", response)

    # Turn on the LED
    mybolt.digitalWrite(LED_PIN, 'HIGH')
    time.sleep(2)  # Wait for 2 seconds
    # Turn off the LED
    mybolt.digitalWrite(LED_PIN, 'LOW')
    time.sleep(2) 

# Main loop to continuously check and alert
while True:
    check_and_alert()
    time.sleep(5)  # Adjust the sleep duration based on your needs
