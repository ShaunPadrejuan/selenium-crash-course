# %% [markdown]
# ## Imports and Initializations

# %%
# %pip install import-ipynb
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import page

# %% [markdown]
# ## Define Classes and Test Cases

# %% [markdown]
# ## The Flow: setUp -> TestCase 1 -> TearDown -> Setup -> TestCase2 -> TearDown -> and so on

# %%
class PythonOrgSearch(unittest.TestCase): # Test multiple aspects of a website with just this
    def setUp(self): # like an __init__. First to get called
        self.driver = r"C:\Program Files (x86)\chromedriver.exe"
        service = Service(self.driver)
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.python.org/")
        
    # Define Test Cases
    # def not_a_test(self):
    #     print("This will not run since this is not a test. Test should be the first word in the function")
    
    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()  # assert = see if condition in the right is true. Tell if test case is passed or failed
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self): # once everything is done
        self.driver.close()

# %% [markdown]
# ## Run Main

# %%
if __name__ == "__main__":
    unittest.main()


