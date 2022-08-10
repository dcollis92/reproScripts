####################################################################
# Skeleton for Appium Virtual Tests on Sauce Labs
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
from time import sleep
import os
import urllib3
import requests
import json
import multiprocessing
import random
import sys
from colorama import Fore, Back, Style


###################################################################
# This makes the functions below execute 'run' amount of times
###################################################################
run = 5

###################################################################
# Declare as a function in order to do multiple runs
###################################################################
def run_sauce_test():

    androidTest = True
    iosTest = False
    useApp = False

    ###################################################################
    # Selenium with Python doesn't like using HTTPS correctly
    # and displays a warning that it uses Unverified HTTPS request
    # The following disables that warning to clear the clutter
    # But I should find a way to do the proper requests
    ###################################################################
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    ###################################################################
    # Pull a random Pokemon name to use as the test name
    ###################################################################
    # pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
    # pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
    # random_pokemon = random.choice(pokemon_names)
    URL='https://random-word-api.herokuapp.com/word?number='

    def get_words(num):
        response=requests.get(URL+str(num)).text
        return json.loads(response)
    names = get_words(1)
    test_name = ' '.join(names)
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
    # Uncomment if this is an app test
    # Add in the location to the stored app too
    ###################################################################
    # useApp = True
    appLocation = 'storage:7e6ec537-95ed-46ab-bc8f-2301527c76d9'

    ###################################################################
    # Common parameters (desired capabilities)
    ###################################################################
    projectParameters = {
        'build':'reproduction',
        # The following are not required
        # 'deviceOrientation' : 'landscape',
        # 'appiumVersion': '1.20.2',
        # 'extendedDebugging': 'true',
        # 'autoGrantPermissions' : 'true',
        # 'autoAcceptAlerts':'true',
        # 'tunnelIdentifier': 'rdc-on-sauce-tunnel',
    }

    androidParameters = { # Define Android parameters here
        'deviceName' : 'Android GoogleAPI Emulator',
        'platformVersion' : '11.0',
        'platformName' : 'Android',
        'browserName' : 'chrome',
        'name': test_name,
        # 'automationName' : 'UIAutomator2',
    }


    iosParameters = { # Define iOS Parameters here
        'deviceName' : 'iPhone 12 Pro Simulator',
        'platformVersion' : '14.5',
        'platformName' : 'iOS',
        'enableAsyncExecuteFromHttps': 'true',
        'simpleIsVisibleCheck': 'true',
        'automationName': 'XCUITest',
        'newCommandTimeout':'10800',
        'idleTimeout': '10800',
        'autoWebview':'false',
        'shouldUseCompactResponses':'false',
        'elementResponseAttributes':'rect',
        'useJSONSource': 'true',
        'includeSafariInWebviews': 'true',
        'maxDuration': '10800',

        # 'browserName' : 'Safari',
        # 'nativeWebTap': 'true',
        # 'locationServicesEnabled':'true',
        # 'locationServicesAuthorized':'true',
    }


    ###################################################################
    # Merge parameters into a single capability dictionary
    ###################################################################
    sauceParameters = {}
    sauceParameters.update(projectParameters)
    # sauceParameters.update({'build': '-'.join(projectParameters.get('tags'))}) # This concatenates the tags key above to add the build parameter

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

    ###################################################################
    # Connect to Sauce Labs
    ###################################################################
    try:
        region
    except NameError:
        region = 'US'

    if region == 'US':
        print(Fore.MAGENTA + 'You are using the US data center for an EMUSIM test. Look at you!' + Style.RESET_ALL)
        driver = webdriver.Remote(
            command_executor='http://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:80/wd/hub',
            desired_capabilities=sauceParameters)
    elif region == 'EU':
        print (Fore.CYAN + 'You are using the EU data center for an EMUSIM test, you beautiful tropical fish!' + Style.RESET_ALL)
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)
    elif region == 'APAC':
        print (Fore.BLUE + 'You are using the APAC data center for an EMUSIM test! Shiny and new!' + Style.RESET_ALL)
        driver = webdriver.Remote(
            command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.apac-southeast-1.saucelabs.com:443/wd/hub',
            desired_capabilities=sauceParameters)

    ###################################################################
    # Test logic goes here
    ###################################################################
    # Navigating to a website


    driver.get("https://www.google.com/");


    # Finding an element
    interact = driver.find_element_by_xpath('//input[@name="q"]')
    # driver.save_screenshot('screenshot.png')


    # Using the selected element
    interact.send_keys('puppies')
    driver.press_keycode(66)

    # interact.submit()

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
