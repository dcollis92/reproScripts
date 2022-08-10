####################################################################
# Skeleton for Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from time import sleep
import os
import urllib3
import json
import random
from colorama import Fore, Back, Style


###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Pull a random Pokemon name to use as the test name
###################################################################
pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
random_pokemon = random.choice(pokemon_names)

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'

###################################################################
# Common parameters (desired capabilities)
###################################################################
sauceParameters = {
    'tags':['Case', 'Experiment',],
    'platformName': 'Windows 10',
    'browserName': 'Chrome',
    # The following are not required
    'browserVersion': '102',
    # 'safariIgnoreFraudWarning': 'true',
    # 'seleniumVersion': '3.141.59',
    # 'chromedriverVersion': '89.0.4389.23',
    # 'iedriverVersion': '3.141.0',
    # 'ensureCleanSession': 'true',
    # Sauce Specific Options
    'sauce:options': {
        'screenResolution':'1400x1050',
        'tunnelIdentifier': 'qa_proxy',
        'extendedDebugging': True,
        'name': 'Snagajob Repro',
        },

    # 'capturePerformance': 'true',
    # 'idleTimeout': 180,
    # 'commandTimeout': 600,
    # 'prerun':{
    #     'executable': 'storage:fbce4621-56d2-4748-bada-49a2c8cec648',
    #     'args': ['--silent'],
    #     'timeout': 500,
    #     'background': 'false',
    # },
    # safari auth prerun
    # 'prerun':{
    # 'executable':'https://gist.githubusercontent.com/nicole-daugereaux/fecb3bdd1042692a8d1834ca2e7d6ba1/raw/894b04523779d13321c2e8a094e97c515aa5141c/disable_fraud.sh',
    # 'background': 'false',
    # },

    # Browser Specific Options
    # 'chromeOptions':{
    #     # 'mobileEmulation':{'deviceName':'iPhone X'},
    #     'prefs':{"profile.default_content_setting_values.notifications": 2},
    #         # 'profile': {
    #         #     'password_manager_enabled': 'false',
    #         #     },
    #         #     'credentials_enable_service': 'false',
    #         # },
    #     # 'args': ['start-fullscreen'],
    #     # 'perfLoggingPrefs': {'enableNetwork': True, 'traceCategories': 'browserdevtools.timeline,devtools'}
    #
    #
    # # 'moz:firefoxOptions':{
    # #     'log': {'level': 'trace'},
    # },
}
# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'EU'

if region == 'US':
    print(Fore.MAGENTA + 'You are using the US data center for a Desktop test, rockstar!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://saj-runner-bot:f032a72b-7c7e-41a2-9b96-eefe715486d1@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print (Fore.CYAN + 'You are using the EU data center for a Desktop test, you beautiful tropical fish!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'APAC':
    print (Fore.BLUE + 'You are using the APAC data center for a Desktop test! Shiny and new!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.apac-southeast-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
driver.get('https://seeker.snagqa.com/search')
driver.find_element_by_css_selector("[data-snagtag=\"app-header\"]")
signin = driver.find_element_by_css_selector("[data-snagtag=\"sign-in\"]")
sleep(3)
signin.click()
driver.find_element_by_css_selector("subnav-item")
workers = driver.find_element_by_css_selector("[data-snagtag=\"workers\"]")
sleep(3)
workers.click()
childWindow = driver.window_handles[0]
#to switch focus the first child window handle
driver.switch_to.window(childWindow)
# driver.find_element_by_css_selector("social-register-modal")
driver.find_element_by_css_selector("[data-snagtag=\"userid\"]").send_keys("newseeker_6636757@snagatest.com")
driver.find_element_by_css_selector("button[data-snagtag=\"signin\"]").click()

# driver.find_element_by_css_selector("social-register-modal")
childWindow = driver.window_handles[0]
#to switch focus the first child window handle
driver.switch_to.window(childWindow)
driver.find_element_by_css_selector("[data-snagtag=\"psw\"]").send_keys("1234567890")
# driver.find_element_by_css_selector("social-register-modal")
driver.find_element_by_css_selector("button[data-snagtag=\"signin\"]").click()

# Setting the job status to passed
driver.execute_script('sauce:job-result=passed')

# Ending the test session
driver.quit()
