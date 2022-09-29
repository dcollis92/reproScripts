####################################################################
# Skeleton for Selenium tests on Screener
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
# Common parameters (desired capabilities)
###################################################################
sauceParameters = {
    # These Screener capablities are required. You'll find the apiKey and group name in the Screener.io dashboard
    'browserName': 'chrome',
    'browserVersion': '102.0',
    'sauce:visual': {
        'apiKey': '5555d962-5e7d-491e-b319-4c578c1cdd7b',        # 'group': os.environ['SCREENER_GROUP_KEY'],
        'projectName': 'puppyTest',
        'viewportSize': '1280x1024'
    },
    'sauce:options': {
        'username' : os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
    }
}
print(type(sauceParameters))
###################################################################
# Connect to Screener
###################################################################
# command_executor = 'https://hub.screener.io/wd/hub',


driver = webdriver.Remote(
    desired_capabilities=sauceParameters,
    command_executor='https://hub.screener.io/wd/hub'
    )
    # self.driver = webdriver.Remote(host, capabilities)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
driver.get('https://www.google.com')
sleep(5)

# Inititializing Visual Test
driver.execute_script('/*@visual.init*/', 'My Puppy Test')

# Visual Snapshot No. 1
driver.execute_script('/*@visual.snapshot*/', 'Home')

# # Finding an element
interact = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#
# # Using the selected element
interact.send_keys('puppies')
interact.submit()

#Snapshot No. 2
driver.execute_script('/*@visual.snapshot*/', 'Puppy Results')

# Setting Job Status to Passed
driver.execute_script('sauce:job-result=passed')

# Using Action chains
# ActionChains(driver).move_to_element(interact).perform()

# Ending the test session
driver.quit()
