from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import os
import time
import schedule

display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("path to chromedriver")

instances = [
    {
        "instance": "https://devXXXX.service-now.com",
        "username": "admin",
        "pass": "yourpassword",
    },
]

wakeuptime = '07:00'


# Signin to instance via headless chromium to wake up.
def wake(instance, username, passwerd):
    driver.get(instance)
    # Wait for Login iFrame to ready up.
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#gsft_main"))
    )

    # Collect HTML Elements we'll be using
    name_input = driver.find_element(By.ID, "user_name")
    pass_input = driver.find_element(By.ID, "user_password")
    loginButton = driver.find_element(By.ID, "sysverb_login")

    # Sign In
    name_input.send_keys(username)
    print("{} - Filled in Username".format(instance))
    time.sleep(3)
    pass_input.send_keys(passwerd)
    print("{} - Filled in Pass".format(instance))
    time.sleep(3)
    loginButton.click()
    print("{} - Clicked Login Button".format(instance))
    time.sleep(5)

    # Save Img of signin proof.
    driver.get_screenshot_as_file("capture.png")
    print("{} - Done, cleaning up.".format(instance))
    # Cleanup active browser.
    driver.quit()
    display.stop()


# Loop through instances to wake.
def sunsup():
    for inst in instances:
        wake(inst["instance"], inst["username"], inst["pass"])


# Set Schedule for continuous waking.
schedule.every().day.at(wakeuptime).do(sunsup)
while True:
    schedule.run_pending()
    time.sleep(1)
