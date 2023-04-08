# ServiceNow-PDI-Scheduled-Wakeup
This script logs into one or more ServiceNow instances at a specified time every day using a headless Chrome browser, provided by Selenium. This is useful for ensuring that the instances are active and ready for use at a certain time each day. Wakeup your ServiceNow PDI from hibernation so you're ready to get to work!

## Requirements
* Python 3.x
* Selenium
* ChromeDriver
* PyVirtualDisplay

You can install the required packages using pip:
```bash
pip install selenium pyvirtualdisplay
```
Additionally, you need to download ChromeDriver and make sure it's executable and available in your system's PATH or specified in the script.

## Usage
Open the script and modify the instances list with your ServiceNow instances' URLs, usernames, and passwords.

```python
instances = [
    {
        "instance": "https://devXXXX.service-now.com",
        "username": "admin",
        "pass": "yourpassword",
    },
    {
        "instance": "https://devYYYY.service-now.com",
        "username": "admin",
        "pass": "anotherpassword",
    },
]
```

Set the wakeuptime variable to the desired wakeup time. The time format is in 24-hour format (e.g., '07:00' for 7:00 AM).

If ChromeDriver is not in your system's PATH, update the following line with the correct path to the ChromeDriver executable:
```python
driver = webdriver.Chrome("path to chromedriver")
````

# Run the Script
```bash
python wakeup_script.py
```

The script will log into each instance daily at the specified wakeup time. A screenshot will be saved as capture.png for each instance after login, which can be used as proof of a successful login.

Note: Please make sure to keep your credentials secure and not to share the script with sensitive information.

# Running the Script Continuously
To keep the script running continuously, you can use different methods based on your operating system:

## Unix-based Systems (Linux and macOS)
You can use the nohup command to run the script in the background. Open a terminal and navigate to the directory containing the script. Then, run the following command:

```bash
nohup python wakeup_script.py &
```

This command will run the script in the background, and it will continue running even if you close the terminal. The nohup command redirects the script's output to a file called nohup.out in the same directory by default. If you want to check the script's output, you can view this file.

To stop the background script, first find its process ID (PID) using the following command:

```bash
ps aux | grep wakeup_script.py
```

Take note of the PID, and then use the kill command to stop the process:

```bash
kill <PID>
```
Replace <PID> with the process ID you obtained earlier.

## Windows
On Windows, you can run the script in the background using the start command. Open a command prompt and navigate to the directory containing the script. Then, run the following command:

```batch
start /B python wakeup_script.py
```

To stop the background script, open Task Manager, go to the "Details" tab, find the python.exe process associated with the script, right-click on it, and select "End task."
    
# FAQs
## What is this script for?
This script is for automatically logging in to a list of ServiceNow instances and taking a screenshot of the home page. This can be useful for monitoring the availability of these instances.

## How do I configure the script?
To configure the script, open the instances list in the script and add the URL, username, and password for each instance you want to wake up. You can also configure the logging settings and Chrome options.

## How do I view the screenshots taken by the script?
The screenshots taken by the script are saved in the logs directory, in a file with the format instance_name-capture_yyyy-mm-dd_HH-MM-SS.png. You can view these screenshots using any image viewer.

## What do I do if the script doesn't work?
If the script doesn't work, you can try the following troubleshooting steps:
* Check that you've configured the instances list correctly
* Check that you have the correct version of ChromeDriver installed
* Check that you have the correct permissions to run the script
* Check that you're running the script from the correct directory
