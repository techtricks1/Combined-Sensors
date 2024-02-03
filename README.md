# Combined Sensors IoT Project
<p align="center">
<img src="https://www.canva.com/design/DAF7sWE_8JQ/CLJgn5KO57s7CKenZHB6Jg/edit?utm_content=DAF7sWE_8JQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" alt="logo">
</p>

## Introduction

The Combined Sensors IoT Project is a versatile system that utilizes Bolt IoT devices along with temperature and light sensors to monitor environmental conditions. It triggers alerts via SMS and controls an LED based on predefined threshold values.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Applications](#applications)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project is designed to continuously monitor temperature and light levels using sensors connected to a Bolt WiFi Module. When predefined thresholds are exceeded, the system triggers alerts via SMS using Twilio and visually indicates alerts using an LED.

## Key Features

- Real-time monitoring of temperature and light levels
- SMS alerts via Twilio when thresholds are crossed
- LED indicator for visual alerts
- Customizable threshold values and sleep duration

## Applications

The Combined Sensors IoT Project has various potential applications, including:

- Environmental Monitoring: It can monitor temperature and light levels in various environments such as homes, offices, warehouses, or agricultural settings.
- Alert System: The project triggers alerts via SMS when predefined thresholds for temperature and light levels are exceeded. This can be particularly useful in scenarios where maintaining specific environmental 
  conditions are crucial, such as in server rooms or storage facilities.
- Resource Optimization: By monitoring environmental conditions, the project can help optimize resource usage. For example, it can provide insights into energy consumption patterns based on light levels or help 
  optimize heating and cooling systems based on temperature fluctuations.
- Security: The project can be integrated into a security system to detect changes in ambient light levels. Sudden changes in light intensity, especially during specific times of the day, could indicate potential 
  security breaches or unauthorized access.
- Education and Learning: This project serves as an educational tool for learning about IoT (Internet of Things) concepts, sensor integration, data monitoring, and alert systems. It can be used in educational 
  settings to teach students about practical applications of IoT technology.

## Setup

1. Connect the sensors and components according to the provided documentation.
2. Update the `conf.py` file with your actual Bolt IoT API key, device ID, and Twilio credentials for SMS alerts.
3. Ensure that the necessary Python libraries (`boltiot`, `twilio`) are installed.

## Usage

Run the `combined_sensors.py` script using Python. The system will continuously monitor the sensor values and trigger alerts via SMS and LED indicators when the predefined thresholds are exceeded.

```bash
python combined_sensors.py
```

## Customization

- Adjust the threshold values (`TEMP_THRESHOLD_HIGH`, `TEMP_THRESHOLD_LOW`, `LIGHT_THRESHOLD_HIGH`, `LIGHT_THRESHOLD_LOW`) in the code based on your specific requirements.
- Modify the sleep duration (`time.sleep(5)`) in the main loop to change the frequency of sensor readings.
  
### Note 

- if you would like to use the code replace the ```conf.py``` credentials with your actual credentials.
  
## Contributing

Contributions to this project are welcome! Feel free to open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
