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
capabilities = {
    # These Screener capablities are required. You'll find the apiKey and group name in the Screener.io dashboard
    'browserName': 'chrome',
    'browserVersion': '102.0',
    'sauce:visual': {
        'apiKey': '5555d962-5e7d-491e-b319-4c578c1cdd7b',        # 'group': os.environ['SCREENER_GROUP_KEY'],
        'projectName': 'exampleTest',
        'viewportSize': '1280x1024'
    },
    'sauce:options': {
        'username' : os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
    }


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

###################################################################
# Connect to Screener
###################################################################
command_executor = 'https://hub.screener.io/wd/hub',

driver = webdriver.Remote(command_executor, capabilities)
# self.driver = webdriver.Remote(host, capabilities)

###################################################################
# Test logic goes here
###################################################################
# Navigating to a website
def test_take_snapshot(self):
  driver.get('https://screener.io')
  driver.execute_script('/*@visual.init*/', 'My Visual Test')
  driver.execute_script('/*@visual.snapshot*/', 'Home')
# driver.get('https://www.google.com')
#
# # Taking a screenshot on Screener
# # Syntax dictates the screener.snapshop takes the picture
# #   and the 'Homepage' part is what the screenshot is called
# driver.execute_script('/*@visual.snapshot*/', 'Google Homepage')
#
# # Finding an element
# interact = driver.find_element_by_name('q')
#
# # Using the selected element
# interact.send_keys('chupacabra')
# interact.submit()
# # interact.click()
#
# driver.execute_script('/*@visual.snapshot*/', 'Chupacabra Results')

# Using Action chains
# ActionChains(driver).move_to_element(interact).perform()

# Ending the test session
driver.quit()
