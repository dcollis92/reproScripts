###################################################################
# This is a list of easy to copy and to use functions
###################################################################

###################################################################
# Imports used in the tests
###################################################################
from selenium import webdriver
from time import sleep
import os
import urllib3
import json
import random

###################################################################
# Common parameters (desired capabilities)
# For Sauce Labs tests
###################################################################
sauceParameters = {
    'tags':['Case', 'NUM',],
    'name': 'TEST NAME',
    'platform': 'Windows 10',
    'browserName': 'chrome',
    # The following are not required
    # 'version': 'latest',
    'screenResolution':'1920x1080',
    # 'seleniumVersion': '3.141.59',

    # Sauce Specific Options
    # 'extendedDebugging': 'true',
    # 'capturePerformance': 'true',
    # 'idleTimeout': 180,
    # 'commandTimeout': 600,
    # 'prerun':{
    #     'executable': 'https://raw.githubusercontent.com/phillsauce/saucelabs-import-files/master/WinDownloadFiles.bat',
    #     'args': ['--silent'],
    #     'timeout': 500,
    #     'background': 'false',
    # },

    # Browser Specific Options        
    # 'chromeOptions':{
    #     'mobileEmulation':{'deviceName':'iPhone X'},
    #     'prefs': {
    #         'profile': {
    #             'password_manager_enabled': 'false',
    #             },
    #             'credentials_enable_service': 'false',
    #         },
    #     'args': ['test-type', 'disable-infobars'],
    # },

    # 'moz:firefoxOptions':{
    #     'log': {'level': 'trace'},
    # },
}
# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': '-'.join(sauceParameters.get('tags'))})

###################################################################
# onnect to Sauce Labs using OS environment variables
###################################################################
driver = webdriver.Remote(
    command_executor='http://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:80/wd/hub',
    desired_capabilities=sauceParameters)

driver = webdriver.Remote(
    command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',
    desired_capabilities=sauceParameters)

###################################################################
# This will search for an element. If it doesn't find the element (gets an exception)
# Then it will perform a task.
# It loops until there is no exception (break)
###################################################################
driver.get('https://www.dryzz.com')
while True:
    try: # Try to do the below
        driver.find_element_by_link_text('Projects')
        break # If element found then break out of while loop
    except: # Perform these actions if there is an exception
        interact = driver.find_element_by_name('username')
        interact.send_keys('test_user_mcgoo')
        interact = driver.find_element_by_name('password')
        interact.send_keys('test_user_mcgoo')
        interact.submit()

###################################################################
# Set a breakpoint in your test
# This will stop the test at this point and allow manual
# control on the Sauce Labs website
###################################################################
driver.execute_script('sauce: break')

###################################################################
# This adds notes to the command window in Sauce Labs dashboard
###################################################################
driver.execute_script('sauce:context=Place words here for notes')

###################################################################
# Take screenshot
###################################################################
driver.save_screenshot('screenshot.png')

###################################################################
# Mark a test pass or failed in execution
###################################################################
driver.execute_script('sauce: job-result=passed')
driver.execute_script('sauce: job-result=failed')

###################################################################
# This opens a file to increment the number
###################################################################
countFilePath = Path('countFile.txt')

def getNumber(filename = countFilePath):
        with open(countFilePath, 'r+') as countingFile:
                val = int(countingFile.read() or 0) + 1
                countingFile.seek(0)
                countingFile.truncate()
                countingFile.write(str(val))
                countingFile.close()
                # print ('This is test run: ' + str(val))
                return str(val)

###################################################################
# Stop test
###################################################################
driver.quit()

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# This is a list of the data center URLs.
# Mainly for reference, but you're welcome to use the variables
###################################################################
us_west_dc = 'ondemand.saucelabs.com/wd/hub'
us_east_dc = 'ondemand.eu-central-1.saucelabs.com/wd/hub'
eu_west_dc = 'ondemand.us-east-1.saucelabs.com/wd/hub'

###################################################################
# Taking a screenshot on Screener
###################################################################
driver.execute_script('/*@screener.snapshot*/', 'Google Homepage')

###################################################################
# Back up URL for Pokemon names
###################################################################
https://gist.github.com/phillram/1e710297e700d9b82dbcc64b6415253e
https://gist.githubusercontent.com/phillram/1e710297e700d9b82dbcc64b6415253e/raw/8b4c3aa15ec865af6db0bfa33bff70f6bd3c01c9/pokemon_names.json


