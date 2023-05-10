from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    option = options.Options()
    option.add_experimental_option('detach', True)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://www.google.com/")
    driver.find_element(By.ID, "APjFqb")\
        .send_keys("asdf"+Keys.ENTER)
    driver.back()

    # time.sleep(3)
    # driver.quit()


if __name__ == '__main__':
    main()