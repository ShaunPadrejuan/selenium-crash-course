# Selenium Crash Course
Source codes and notes on a Selenium Crash Course

```
https://www.youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ
```

The link below has the resources for the WebDriver and the Test Chrome browser.

```
https://googlechromelabs.github.io/chrome-for-testing/
```

For easier access, place the chromedriver in the Program Files (x86)

```
"C:\Program Files (x86)\chromedriver.exe"
```

Official Selenium-Python Documentation

```
https://selenium-python.readthedocs.io/
```

# Selenium IDE Crash Course

```
https://www.youtube.com/playlist?list=PLaDALgeX9grpP0CkpMqymSmGPvHNjkSIw
```

### Phase 1: Install Selenium IDE for Chrome/Firefox and Install Selenium-Side-Runner for CLI
1. Access the extensions marketplace for your browser and download Selenium IDE
2. For more information, please access this link

```
https://www.selenium.dev/selenium-ide/
```
3. For CLI, first install node and npm

```
https://nodejs.org/en/download
```

4. Then, install your browser's specific driver. For more information, please access this link

```
https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner
```

### Phase 2: Running from CLI
1. To run in CLI, add node and the driver for the browser in your PATH variables. Here are some samples"

```
C:\Users\{USER}\AppData\Roaming\npm\node_modules\chromedriver\lib\chromedriver
```

```
C:\Users\{USER}\AppData\Roaming\npm
```

2. Here is a sample command in CLI:

```
selenium-side-runner C:\Selenium\MySecondProject\MySecondProject.side
```

Use "selenium-side-runner" as the call to the extensions, and use the PATH going to the .side file as the argument

3. You can also configure .yaml files. Here is a sample command in CLI with the --config-file additional argument

```
selenium-side-runner --config-file C:\Selenium\MySecondProject\config.yaml C:\Selenium\MySecondProject\MySecondProject.side
```

For a sample of a yaml file, check the official documentations or the sample file in the source code.

NOTE: Apparently, if blocks in the selenium code causes the test case to fail, will look into this.

4. To activate Parallel configuration, go to your test suites, click on settings, and check the box for parallel running.

### Phase 3: How to export the Selenium IDE test to multiple languages
1. Click on the settings of either a test or a test suite.
2. Select export, and from there, there are multiples ways to export as seen below:

![Sample picture of exports](/images/image.png)

3. In the case of Python, make sure to use this command

```
pip install pytest
```

to run the test cases.
