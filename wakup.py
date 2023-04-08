# ServiceNow-PDI-Scheduled-Wakeup
# This script logs in to one or more instances of a service management tool
# using Selenium and takes a screenshot of the home page. The instances to be
# woken up are specified in the 'instances' list below.
#
# Configuration:
#   - Set the URL, username, and password for each instance in the 'instances' list.
#   - Customize the options for Chrome and the virtual display as needed.
#   - Update the path to chromedriver_autoinstaller and chromedriver if necessary.
#
# Requirements:
#   - Python 3.x
#   - selenium
#   - pyvirtualdisplay
#   - chromedriver_autoinstaller
#
# Usage:
#   - Run the script with Python to wake up all instances in the 'instances' list.
#
# Example(s)
#   python wakeup.py
#   python3 wakeup.py
#
# Note: Make sure that the 'logs' directory exists and the user running the script has
#       write permission to it.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
import os
import time
from datetime import datetime
import chromedriver_autoinstaller

# Set up instances to be woken up
instances = [
    {
        "instance": "https://{INSTANCE}.service-now.com",
        "username": "{USERNAME}",
        "pass": "{PASSWORD}",
    },
]

# Start virtual display and headless Chrome
display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-webgl")

# Set user agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Start Chrome driver service
# Example Chromedriver Path: /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/chromedriver_autoinstaller/112/chromedriver
chrome_service = Service(executable_path="{CHROMEDRIVER PATH}")
# Create a Chrome driver instance with the service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Disable the "webdriver" property to prevent detection
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# The wake function logs in to an instance and takes a screenshot of the home page
def wake(instance, username, password):
    # Extract the instance name from the login URL
    instance_name = instance.split("://")[1].split(".")[0]
    
    # Load the login page for the instance
    driver.get(f"{instance}/login.do")
    
    # Find the username, password, and login button elements
    name_input = driver.find_element(By.ID, "user_name")
    pass_input = driver.find_element(By.ID, "user_password")
    loginButton = driver.find_element(By.ID, "sysverb_login")

    # Enter the username
    name_input.send_keys(username)
    time.sleep(1)
    
    # Enter the password
    pass_input.send_keys(password)
    time.sleep(1)
    
    # Click the login button
    loginButton.click()
    time.sleep(10)

    # Take a screenshot of the page
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_file = f"logs/{instance_name}-capture_{timestamp}.png"
    driver.get_screenshot_as_file(screenshot_file)

    # Log out of the instance
    driver.get(f"{instance}/logout.do")

    # Quit the driver and stop the virtual display
    driver.quit()
    display.stop()

# The sunsup function wakes up all instances listed in the 'instances' list
# by logging into each instance and taking a screenshot of the home page
def sunsup():
    # Loop over each instance and wake it up
    for instance in instances:
        # Call the wake function with the instance details
        wake(instance["instance"], instance["username"], instance["pass"])

# Call the sunsup function to start waking up instances
sunsup()
