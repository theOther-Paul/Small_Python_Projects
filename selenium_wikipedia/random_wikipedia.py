import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('https://en.wikipedia.org/wiki/Main_Page')
    driver.implicitly_wait(3)

    for i in range(10):
        print(i)
        try:
            driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/nav[1]/div/ul/li[4]/a').click()
        except AttributeError:
            print("No such element")

        driver.implicitly_wait(2)
        screenshot_name = driver.current_url.lower()
        screenshot_name = screenshot_name.replace('https://en.wikipedia.org/wiki/', '')
        driver.get_full_page_screenshot_as_file(f"captures/{screenshot_name}.png")

        print(f"Screenshot is named {screenshot_name}.png")
        i += 1

    driver.quit()


if __name__ == '__main__':
    main()
