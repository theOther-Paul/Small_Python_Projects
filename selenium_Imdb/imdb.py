from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('https://www.imdb.com/')
    driver.implicitly_wait(3)

    try:
        driver.find_element(By.ID, 'imdbHeader-navDrawerOpen--desktop').click()
    except AttributeError:
        print('Not found!')
    else:
        driver.find_element(By.XPATH, '/html/body/div[2]/nav/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span').click()

    driver.get_full_page_screenshot_as_file('captures/top_250_movies.png')
    print('Movies screenshot succeeded')
    driver.implicitly_wait(3)

    try:
        driver.find_element(By.XPATH, '/html/body/section[1]/nav/div[2]/label[2]/div').click()
    except AttributeError:
        print('Not found!')

    driver.find_element(By.XPATH, '/html/body/section[1]/nav/div[2]/aside/div/div[2]/div/div[2]/div[1]/span/div/div/ul/a[2]').click()

    driver.get_full_page_screenshot_as_file('captures/top_250_TV_shows.png')
    print('TV series screenshot succeeded')

    driver.implicitly_wait(2)
    driver.quit()


if __name__ == '__main__':
    main()
