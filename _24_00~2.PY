
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# setup env vars based on EnvVarMaster:
LINKEDIN_LOGIN_URL = os.environ.get('LINKEDIN_LOGIN_URL', 'Custom Message / Key does not exist')
FILTER_SEARCH_URL = os.environ.get('FILTER_SEARCH_URL', 'Custom Message / Key does not exist')
FIRST_NAME = os.environ.get('FIRST_NAME', 'Custom Message / Key does not exist')
LAST_NAME = os.environ.get('LAST_NAME', 'Custom Message / Key does not exist')
EMAIL = os.environ.get('EMAIL', 'Custom Message / Key does not exist')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD', 'Custom Message / Key does not exist')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER', 'Custom Message / Key does not exist')
COLLEGE_OR_UNIVERSITY_ATTENDED = os.environ.get('COLLEGE_OR_UNIVERSITY_ATTENDED', 'Custom Message / Key does not exist')
DEGREE = os.environ.get('DEGREE', 'Custom Message / Key does not exist')
LINKED_IN_PROFILE_URL = os.environ.get('LINKED_IN_PROFILE_URL', 'Custom Message / Key does not exist')
GIT_OR_GITHUB_REPO = os.environ.get('GIT_OR_GITHUB_REPO', 'Custom Message / Key does not exist')


def setup_chrome_driver_for_selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(LINKEDIN_LOGIN_URL)
    return driver

driver = setup_chrome_driver_for_selenium()

# constants:
linkedin_dictionary = {
    "first_name": FIRST_NAME,
    "last_name": LAST_NAME,
    "email": EMAIL,
    "linkedin_password": LINKEDIN_PASSWORD,
    "phone_number": PHONE_NUMBER,
    "college_or_university_attended": COLLEGE_OR_UNIVERSITY_ATTENDED,
    "degree": DEGREE,
    "linked_in_profile_url": LINKED_IN_PROFILE_URL,
    "git_or_github_repo": GIT_OR_GITHUB_REPO
}

# -------------------------- beginning at the website ---------------------------#

time.sleep(0.1)

email_or_phone_id = driver.find_element(By.ID, "username")
email_or_phone_id.send_keys(linkedin_dictionary["email"])

password_id = driver.find_element(By.ID, "password")
password_id.send_keys(linkedin_dictionary["linkedin_password"] + Keys.ENTER)

# sign in button: (not needed, if pressing enter anyhow)
# sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# sign_in_button.click()

# wait for the visibility of the profile photo by its id before navigating away
# WebDriverWait(driver, 0).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Photo of Gavin Martin']"))
# )

#
# driver.implicitly_wait(0)

driver.get(FILTER_SEARCH_URL)

# the easy apply button:
'''
<span class="artdeco-button__text">
    easy apply
</span>
'''

# close the browser
# driver.quit()
