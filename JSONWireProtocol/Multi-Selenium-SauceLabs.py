####################################################################
# Skeleton for Multi Testing Selenium tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from selenium import webdriver
from time import sleep
import multiprocessing
import os
import urllib3
import json
import random

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################

###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################
run = 30

###################################################################
# Declare as a function in order to do multiple runs
###################################################################
def run_sauce_test():
    ###################################################################
    # Pull a random Pokemon name to use as the test name
    ###################################################################
    pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
    pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
    random_pokemon = random.choice(pokemon_names)

    # Random names from heroku app
    # URL='https://random-word-api.herokuapp.com/word?number='
    #
    # def get_words(num):
    #     response=requests.get(URL+str(num)).text
    #     return json.loads(response)
    # names = get_words(1)
    # test_name = ' '.join(names)
    ###################################################################
    # Common parameters (desired capabilities)
    ###################################################################
    sauceParameters = {
        'tags':['Case', 'NUM',],
        'platform': 'MacOS 10.15',
        'browserName': 'safari',
        # The following are not required
        'name': random_pokemon,
        # 'screenResolution':'1920x1080',
        'version': 'latest',
        'seleniumVersion': '3.141.59',
        # 'iedriverVersion': '3.150.1',

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
    # Connect to Sauce Labs
    ###################################################################
    try:
        region
    except NameError:
        region = 'US'

    if region != 'EU':
        print('You are using the US data center')
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)
    elif region == 'EU':
        print ('You are using the EU data center')
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    ###################################################################
    # Test logic goes here
    ###################################################################
    # Navigating to a website
    driver.get('https://www.google.com')
    sleep(5)

    # Finding an element
    interact = driver.find_element_by_name('q')

    # Using the selected element
    interact.send_keys('chupacabra')
    interact.submit()

    sleep(5)

    # interact.click()

    # Saving an extra screenshot
    # driver.save_screenshot('screenshot.png')

    # Using Action chains
    # ActionChains(driver).move_to_element(interact).perform()

    # Sauce Labs specific executors
    # driver.execute_script('sauce: break')
    # driver.execute_script('sauce:context=Notes here')

    # Setting the job status to passed
    driver.execute_script('sauce:job-result=passed')

    # Ending the test session
    driver.quit()


###################################################################
# This is the command to use multiprocessing to run the desired
# amount of times
###################################################################
if __name__ == '__main__':
    jobs = [] # Array for the jobs
    for i in range(run): # Run the amount of times set above
        jobRun = multiprocessing.Process(target=run_sauce_test) # Define what function to run multiple times.
        jobs.append(jobRun) # Add to the array.
        jobRun.start() # Start the functions.
        # print('this is the run for: '+ str(i))
