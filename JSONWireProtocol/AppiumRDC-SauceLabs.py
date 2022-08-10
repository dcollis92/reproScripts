####################################################################
# Skeleton for Appium tests on Sauce Labs Real Devices - Unified Platform
# This is currently in BETA and will only work for private devices
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
import requests
from time import sleep
import os
import urllib3
import json
import random
import sys
from colorama import Fore, Back, Style


androidTest = True
iosTest = False
useApp = False
appLocation = 'storage:ecfbfc89-597e-4438-bca2-3c96087a3345'
# appLocation = 'storage:filename=NetworkSpeed 2.zip'

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
# pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
# pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
# random_pokemon = random.choice(pokemon_names)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
# iosTest = True

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'

###################################################################
# Common parameters (desired capabilities)
###################################################################
projectParameters = {
    # 'tags':['Case', 'Investigation',],
    # The following are not required
    # ''tunnelIdentifier': 'exampletunnel'
    # 'app': 'storage:610f9e00-9415-44a2-94f1-a1f418663cd3',
    # 'app': 'storage:8a8b7702-f4fb-4788-93fa-8a8a3e631c74',
    }

androidParameters = {
    # 'browserName': 'Chrome',
    'platformName': 'Android',
    # 'platformVersion': '12',
    'name': 'Test',
    # 'phoneOnly': 'true',
    # Define Android parameters here
    # 'deviceName' : 'Samsung Galaxy S10\+',
    # 'deviceName' : '(Samsung.*)|(Huawei.*)|(Xiaomi.*)|(OnePlus.*)|(Google.*)',
    'deviceName' : 'Samsung_Galaxy_S21_FE_5G_POC103',
    # 'orientation' : 'LANDSCAPE',
    # 'platformName' : 'Android',
    # 'browserName' : 'Chrome',
    # 'platformVersion' : '11',
    # 'otherApps': 'storage:5471e3e8-5be6-48f7-8968-47ffc574b2f6',
    # 'appiumVersion': '1.22.0',
    # 'deviceOrientation': 'portrait',
}

iosParameters = { # Define iOS Parameters here
    # 'deviceName' : 'iPhone [6-8]',
    'name': 'Missing Commands Repro',
    'deviceName' : 'iPhone.*',
    'platformVersion' : '12',
    'platformName' : 'iOS',
    # 'orientation': 'LANDSCAPE',    # 'automationName' : 'XCUITest',
    # 'tabletOnly': 'true',
    # 'phoneOnly': 'true',
    # 'name': 'Orientation Test',
    # 'appiumVersion': '1.22.0',
    # 'autoDismissAlerts': 'true',
    # 'connectHardWareKeyboard' : 'true',
    'browserName' : 'safari',
    # 'newCommandTimeout' : '0',
    # 'nativeWebTap': 'true',
}

###################################################################
# Merge parameters into a single capability dictionary

###################################################################
sauceParameters = {}
if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)
    if useApp:
        sauceParameters['app'] = appLocation # Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
        #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
elif iosTest:
    sauceParameters.update(iosParameters)
    if useApp:
        sauceParameters['app'] = appLocation
    else:
        sauceParameters['browserName'] = 'safari'



# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': 'Investigation'})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print(Fore.MAGENTA + 'You are using the US data center for an RDC test, so a bald eagle is obviously running your tests.' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://arun.prakash:3a587203-355d-41f3-981c-cabaf068a962@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        # command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print (Fore.CYAN + 'You are using the EU data center for an RDC test, you beautiful tropical fish!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################

# Native Demo App Logic
# driver.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
# driver.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
# driver.find_element_by_accessibility_id("test-LOGIN").click()
#
# # # Navigating to a website
driver.get_window_size()
# driver.get('https://www.google.com')
# # #
# # # # Finding an element
# interact = driver.find_element_by_name('q')
sleep(2)
#
# #
# # # # Using the selected element
# interact.send_keys('puppies')
# interact.submit()
# # interact.click()

# # # Saving an extra screenshot
driver.save_screenshot('screenshot.png')
# #
# # # Using Action chains
# # # ActionChains(driver).move_to_element(interact).perform()
# #
# # # Sauce Labs specific executors
# # # driver.execute_script('sauce: break')
# # # driver.execute_script('sauce:context=Notes here')
#
#
# # Setting the job status to passed
# driver.execute_script('sauce:job-result=passed')
#
# # Ending the test session
driver.quit()
