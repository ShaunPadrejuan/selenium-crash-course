# %% [markdown]
# ## Imports

# %%
from selenium.webdriver.common.by import By

# %% [markdown]
# ## Define locators

# %%
## any CSS selectors or attributes will be changed here. So that all will be in one file for convenience.
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass


