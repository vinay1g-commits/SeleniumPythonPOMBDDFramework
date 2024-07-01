import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from utilities import configreader
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


def before_scenario(context, scenario):
    browser_name = configreader.reading_data_ini("basic info", "browser")

    if browser_name == "chrome":
        chrome_driver_path = "/home/vinay/Downloads/finalchromedriver/chromedriver-linux64"
        options = ChromeOptions()
        service = ChromeService(executable_path=chrome_driver_path)
        context.driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        firefox_binary_path = "/usr/bin/firefox"  # Verify this path using `which firefox`
        options = FirefoxOptions()
        options.binary_location = firefox_binary_path

        profile_path = "/home/vinay/snap/firefox/common/.mozilla/firefox/dt11429s.autop"  # Replace with the actual path to your new profile
        options.profile = profile_path

        service = FirefoxService(executable_path='/usr/local/bin/geckodriver')  # Path to geckodriver

        context.driver = webdriver.Firefox(options=options, service=service)

    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    context.driver.maximize_window()
    context.driver.set_page_load_timeout(10)  # Set page load timeout to 10 seconds
    try:
        context.driver.get(configreader.reading_data_ini("basic info", "url"))
    except TimeoutException:
        print("Page load timed out, proceeding with the next steps")
    time.sleep(3)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_step(context, step):
    if step.status == 'failed' or step.status == 'skipped':
        status = 'failed' if step.status == 'failed' else 'skipped'
        allure.attach(context.driver.get_screenshot_as_png(),
                      name=f'{status}_step_screenshot',
                      attachment_type=AttachmentType.PNG)
