# Simple Sauce Lab Examples
Very simple tests for Sauce Labs that don't require huge frameworks.

# Installing requirements
You may not need all the packages in the requirements file, but you can install them to your python like so (update the path as needed):

```
pip install -r requirements.txt
```

# W3C
The minimum Selenium version that supports W3C is 3.8.0. If your test is erroring with incompatible browsers or infrastructure errors, then make sure you specify the `seleniumVersion` parameter.
Additionally, you'll need Safari 11+, Firefox 53+, or Chrome 61+.

# Appium usage
These don't require an Appium server installed. There are two ways to use Appium that I've found.

* You can add the Appium library to your execution so that it can be imported.
* Install the [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/) and not have to worry about it.
  *  Installation can be done with in your execution directory with:
  
  ```
  pip install Appium-Python-Client
  ```
